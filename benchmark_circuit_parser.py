#!/usr/bin/env python3
"""
CircuitParser 性能测试脚本

用于测试 CircuitParser 的性能，包括：
- 处理时间（总体和各阶段）
- 内存使用
- 不同规模文件的性能
- 批量处理性能

用法:
    python benchmark_circuit_parser.py [options]
"""

import os
import sys
import time
import psutil
import statistics
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import json
from datetime import datetime

# 添加路径以便导入 CircuitParser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from CircuitParser import CircuitParser
except ImportError:
    print("错误: 无法导入 CircuitParser")
    print("请确保 CircuitParser.py 在同一目录下")
    sys.exit(1)


class PerformanceProfiler:
    """性能分析器"""
    
    def __init__(self):
        self.timings = {}
        self.memory_usage = []
        self.process = psutil.Process(os.getpid())
    
    def start_timer(self, name: str):
        """开始计时"""
        self.timings[name] = {'start': time.perf_counter()}
    
    def end_timer(self, name: str):
        """结束计时"""
        if name in self.timings:
            self.timings[name]['end'] = time.perf_counter()
            self.timings[name]['duration'] = (
                self.timings[name]['end'] - self.timings[name]['start']
            )
    
    def record_memory(self):
        """记录当前内存使用"""
        mem_info = self.process.memory_info()
        self.memory_usage.append({
            'rss': mem_info.rss / 1024 / 1024,  # MB
            'vms': mem_info.vms / 1024 / 1024,  # MB
            'time': time.perf_counter()
        })
    
    def get_peak_memory(self) -> float:
        """获取峰值内存使用（MB）"""
        if not self.memory_usage:
            return 0.0
        return max(m['rss'] for m in self.memory_usage)
    
    def get_timings(self) -> Dict[str, float]:
        """获取所有计时结果"""
        return {k: v.get('duration', 0.0) 
                for k, v in self.timings.items() 
                if 'duration' in v}


class CircuitParserBenchmark:
    """CircuitParser 性能测试"""
    
    def __init__(self, iterations: int = 3, warmup: int = 1):
        self.iterations = iterations
        self.warmup = warmup
        self.results = []
    
    def analyze_file(self, file_path: str) -> Dict:
        """分析文件特征"""
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        new_n_count = 0
        output_count = 0
        total_chars = sum(len(line) for line in lines)
        file_size = os.path.getsize(file_path)
        
        for line in lines:
            line_stripped = line.strip()
            if line_stripped.startswith('new_n'):
                new_n_count += 1
            elif '=' in line_stripped and not line_stripped.startswith('INORDER') and not line_stripped.startswith('OUTORDER'):
                output_count += 1
        
        return {
            'file_path': file_path,
            'file_size': file_size,
            'total_lines': total_lines,
            'new_n_count': new_n_count,
            'output_count': output_count,
            'total_chars': total_chars,
            'avg_line_length': total_chars / total_lines if total_lines > 0 else 0
        }
    
    def benchmark_single_file(self, input_file: str, output_file: str, 
                             profile: bool = False) -> Dict:
        """测试单个文件的性能"""
        profiler = PerformanceProfiler()
        
        # 分析文件特征
        file_info = self.analyze_file(input_file)
        if not file_info:
            return None
        
        # 预热（如果需要）
        if self.warmup > 0:
            for _ in range(self.warmup):
                parser = CircuitParser(input_file, output_file + ".warmup")
                parser.process()
                if os.path.exists(output_file + ".warmup"):
                    os.remove(output_file + ".warmup")
        
        # 记录初始内存
        profiler.record_memory()
        
        # 多次运行取平均值
        all_timings = []
        all_peak_memory = []
        
        for iteration in range(self.iterations):
            profiler_iter = PerformanceProfiler()
            profiler_iter.record_memory()
            
            # 创建解析器
            profiler_iter.start_timer('total')
            profiler_iter.start_timer('init')
            parser = CircuitParser(input_file, output_file)
            profiler_iter.end_timer('init')
            
            # 处理文件
            profiler_iter.start_timer('process')
            parser.process()
            profiler_iter.end_timer('process')
            profiler_iter.end_timer('total')
            
            # 记录内存
            profiler_iter.record_memory()
            
            # 收集结果
            timings = profiler_iter.get_timings()
            peak_memory = profiler_iter.get_peak_memory()
            
            all_timings.append(timings)
            all_peak_memory.append(peak_memory)
            
            # 清理输出文件（除了最后一次）
            if iteration < self.iterations - 1 and os.path.exists(output_file):
                os.remove(output_file)
        
        # 计算统计数据
        result = {
            'file_info': file_info,
            'iterations': self.iterations,
            'timings': {
                'total': {
                    'mean': statistics.mean([t['total'] for t in all_timings]),
                    'median': statistics.median([t['total'] for t in all_timings]),
                    'min': min([t['total'] for t in all_timings]),
                    'max': max([t['total'] for t in all_timings]),
                    'stdev': statistics.stdev([t['total'] for t in all_timings]) if len(all_timings) > 1 else 0.0
                },
                'init': {
                    'mean': statistics.mean([t.get('init', 0) for t in all_timings]),
                    'median': statistics.median([t.get('init', 0) for t in all_timings]),
                },
                'process': {
                    'mean': statistics.mean([t.get('process', 0) for t in all_timings]),
                    'median': statistics.median([t.get('process', 0) for t in all_timings]),
                }
            },
            'memory': {
                'peak_mean': statistics.mean(all_peak_memory),
                'peak_median': statistics.median(all_peak_memory),
                'peak_min': min(all_peak_memory),
                'peak_max': max(all_peak_memory),
            },
            'throughput': {
                'nodes_per_sec': file_info['new_n_count'] / statistics.mean([t['total'] for t in all_timings]),
                'lines_per_sec': file_info['total_lines'] / statistics.mean([t['total'] for t in all_timings]),
                'mb_per_sec': (file_info['file_size'] / 1024 / 1024) / statistics.mean([t['total'] for t in all_timings]),
            }
        }
        
        return result
    
    def benchmark_multiple_files(self, file_list: List[str], 
                                output_dir: Optional[str] = None) -> List[Dict]:
        """测试多个文件的性能"""
        results = []
        
        for i, input_file in enumerate(file_list):
            print(f"\n处理文件 {i+1}/{len(file_list)}: {input_file}")
            
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, 
                                          f"benchmark_output_{i}.eqn")
            else:
                output_file = input_file + ".benchmark_output"
            
            result = self.benchmark_single_file(input_file, output_file)
            if result:
                results.append(result)
                self.print_result(result)
        
        return results
    
    def print_result(self, result: Dict):
        """打印单个测试结果"""
        file_info = result['file_info']
        timings = result['timings']
        memory = result['memory']
        throughput = result['throughput']
        
        print(f"\n{'='*80}")
        print(f"文件: {file_info['file_path']}")
        print(f"{'='*80}")
        print(f"文件特征:")
        print(f"  - 文件大小: {file_info['file_size']:,} 字节 ({file_info['file_size']/1024:.2f} KB)")
        print(f"  - 总行数: {file_info['total_lines']}")
        print(f"  - 中间节点数: {file_info['new_n_count']}")
        print(f"  - 输出节点数: {file_info['output_count']}")
        print(f"  - 平均行长度: {file_info['avg_line_length']:.1f} 字符")
        
        print(f"\n处理时间 (运行 {result['iterations']} 次):")
        print(f"  总时间:")
        print(f"    平均: {timings['total']['mean']:.4f} 秒")
        print(f"    中位数: {timings['total']['median']:.4f} 秒")
        print(f"    最小: {timings['total']['min']:.4f} 秒")
        print(f"    最大: {timings['total']['max']:.4f} 秒")
        if timings['total']['stdev'] > 0:
            print(f"    标准差: {timings['total']['stdev']:.4f} 秒")
        
        print(f"  初始化: {timings['init']['mean']:.4f} 秒")
        print(f"  处理: {timings['process']['mean']:.4f} 秒")
        
        print(f"\n内存使用:")
        print(f"  峰值内存: {memory['peak_mean']:.2f} MB (平均)")
        print(f"  峰值内存: {memory['peak_median']:.2f} MB (中位数)")
        print(f"  范围: {memory['peak_min']:.2f} - {memory['peak_max']:.2f} MB")
        
        print(f"\n吞吐量:")
        print(f"  {throughput['nodes_per_sec']:.1f} 节点/秒")
        print(f"  {throughput['lines_per_sec']:.1f} 行/秒")
        print(f"  {throughput['mb_per_sec']:.2f} MB/秒")
    
    def print_summary(self, results: List[Dict]):
        """打印汇总统计"""
        if not results:
            return
        
        print(f"\n{'='*80}")
        print(f"性能测试汇总 ({len(results)} 个文件)")
        print(f"{'='*80}")
        
        # 计算总体统计
        total_times = [r['timings']['total']['mean'] for r in results]
        total_memory = [r['memory']['peak_mean'] for r in results]
        total_nodes = sum(r['file_info']['new_n_count'] for r in results)
        total_files_size = sum(r['file_info']['file_size'] for r in results)
        
        print(f"\n总体统计:")
        print(f"  总处理时间: {sum(total_times):.2f} 秒")
        print(f"  平均处理时间: {statistics.mean(total_times):.4f} 秒")
        print(f"  中位数处理时间: {statistics.median(total_times):.4f} 秒")
        print(f"  最快: {min(total_times):.4f} 秒")
        print(f"  最慢: {max(total_times):.4f} 秒")
        
        print(f"\n内存统计:")
        print(f"  平均峰值内存: {statistics.mean(total_memory):.2f} MB")
        print(f"  最大峰值内存: {max(total_memory):.2f} MB")
        
        print(f"\n总体吞吐量:")
        total_time = sum(total_times)
        print(f"  {total_nodes / total_time:.1f} 节点/秒")
        print(f"  {(total_files_size / 1024 / 1024) / total_time:.2f} MB/秒")
        
        # 按规模分类
        print(f"\n按规模分类:")
        small = [r for r in results if r['file_info']['new_n_count'] < 50]
        medium = [r for r in results if 50 <= r['file_info']['new_n_count'] < 200]
        large = [r for r in results if r['file_info']['new_n_count'] >= 200]
        
        if small:
            avg_time = statistics.mean([r['timings']['total']['mean'] for r in small])
            print(f"  小规模 (<50节点, {len(small)}个): 平均 {avg_time:.4f} 秒")
        if medium:
            avg_time = statistics.mean([r['timings']['total']['mean'] for r in medium])
            print(f"  中等规模 (50-200节点, {len(medium)}个): 平均 {avg_time:.4f} 秒")
        if large:
            avg_time = statistics.mean([r['timings']['total']['mean'] for r in large])
            print(f"  大规模 (>=200节点, {len(large)}个): 平均 {avg_time:.4f} 秒")
    
    def save_results(self, results: List[Dict], output_file: str):
        """保存结果到 JSON 文件"""
        output_data = {
            'timestamp': datetime.now().isoformat(),
            'iterations': self.iterations,
            'warmup': self.warmup,
            'results': results,
            'summary': {
                'total_files': len(results),
                'total_time': sum(r['timings']['total']['mean'] for r in results),
                'avg_time': statistics.mean([r['timings']['total']['mean'] for r in results]),
                'total_nodes': sum(r['file_info']['new_n_count'] for r in results),
            }
        }
        
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"\n结果已保存到: {output_file}")


def find_eqn_files(directory: str, pattern: str = "*.eqn") -> List[str]:
    """查找目录中的所有 EQN 文件"""
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.eqn') and not filename.endswith('_processed.eqn'):
                files.append(os.path.join(root, filename))
    return sorted(files)


def main():
    parser = argparse.ArgumentParser(
        description='CircuitParser 性能测试工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 测试单个文件
  python benchmark_circuit_parser.py -f input.eqn

  # 测试目录中的所有文件
  python benchmark_circuit_parser.py -d aigfuzz_medium

  # 测试多个文件，运行5次取平均
  python benchmark_circuit_parser.py -f file1.eqn file2.eqn -i 5

  # 保存结果到 JSON
  python benchmark_circuit_parser.py -d aigfuzz_medium -o results.json
        """
    )
    
    parser.add_argument('-f', '--files', nargs='+', 
                       help='要测试的文件列表')
    parser.add_argument('-d', '--directory', 
                       help='要测试的目录（会测试所有 .eqn 文件）')
    parser.add_argument('-i', '--iterations', type=int, default=3,
                       help='每个文件运行的次数（默认: 3）')
    parser.add_argument('-w', '--warmup', type=int, default=1,
                       help='预热次数（默认: 1）')
    parser.add_argument('-o', '--output', 
                       help='保存结果到 JSON 文件')
    parser.add_argument('--output-dir', 
                       help='输出文件目录（默认: 与输入文件同目录）')
    parser.add_argument('--max-files', type=int,
                       help='最多测试的文件数（用于限制测试范围）')
    
    args = parser.parse_args()
    
    # 确定要测试的文件
    files_to_test = []
    
    if args.files:
        for f in args.files:
            if os.path.exists(f):
                files_to_test.append(f)
            else:
                print(f"警告: 文件不存在: {f}")
    
    if args.directory:
        if os.path.exists(args.directory):
            found_files = find_eqn_files(args.directory)
            if args.max_files:
                found_files = found_files[:args.max_files]
            files_to_test.extend(found_files)
        else:
            print(f"错误: 目录不存在: {args.directory}")
            sys.exit(1)
    
    if not files_to_test:
        print("错误: 没有找到要测试的文件")
        print("请使用 -f 指定文件或 -d 指定目录")
        sys.exit(1)
    
    print(f"找到 {len(files_to_test)} 个文件进行测试")
    print(f"每个文件运行 {args.iterations} 次，预热 {args.warmup} 次")
    
    # 运行测试
    benchmark = CircuitParserBenchmark(
        iterations=args.iterations,
        warmup=args.warmup
    )
    
    results = benchmark.benchmark_multiple_files(
        files_to_test,
        output_dir=args.output_dir
    )
    
    # 打印汇总
    benchmark.print_summary(results)
    
    # 保存结果
    if args.output:
        benchmark.save_results(results, args.output)
    
    print(f"\n测试完成！")


if __name__ == "__main__":
    main()




