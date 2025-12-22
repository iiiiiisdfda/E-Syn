import os
import sys
import pandas as pd
import re
from tqdm import tqdm
import concurrent.futures

# Tool paths - modify these according to your environment
ABC_PATH = "../abc/abc"
AIGTOAIG_PATH = "../sym_reg/aiger_tool_util/aigtoaig"
AIGFUZZ_PATH = "../sym_reg/aiger_tool_util/aigfuzz"

# The current network is not in a topo order (run "topo").?


def run_aigfuzz_parallel(i):
    """并行处理单个电路的生成"""
    os.system(f"{AIGFUZZ_PATH} -c -s > aigfuzz/simple_circuit_{i}.aig 2>&1")
    os.system(
        f"{ABC_PATH} -c \"read_aiger aigfuzz/simple_circuit_{i}.aig; trim ; write_aiger aigfuzz/simple_circuit_{i}.aig\" 2>&1")

def run_aigfuzz(file_count, max_workers=None):
    # check aigfuzz/ is esist, if not, create it
    if not os.path.exists("aigfuzz"): os.mkdir("aigfuzz")
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(tqdm(
            executor.map(run_aigfuzz_parallel, range(file_count)),
            total=file_count,
            desc='Run circuit generator'
        ))

def load_circuits_parallel(i):
    """并行处理单个电路的加载和转换"""
    os.system(
        f"{ABC_PATH} -c \"read_aiger aigfuzz/simple_circuit_{i}.aig; write_eqn aigfuzz/simple_circuit_{i}.eqn\" 2>&1")
    os.system(
        f"{AIGTOAIG_PATH} aigfuzz/simple_circuit_{i}.aig aigfuzz/simple_circuit_{i}.aag 2>&1")

def load_circuits(file_count, max_workers=None):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(tqdm(
            executor.map(load_circuits_parallel, range(file_count)),
            total=file_count,
            desc='Loading circuits and convert to eqn'
        ))


def process_circuits_parallel(i):
    """并行处理单个电路的分析"""
    # 在子进程中导入模块
    import sys
    sys.path.append("..")
    import run
    from CircuitParser import CircuitParser
    from sexpr_feature_extractor import SExprFeatureExtractor
    
    try:
        parser = CircuitParser(
            f"aigfuzz/simple_circuit_{i}.eqn", f"aigfuzz/simple_circuit_{i}_processed.eqn")
        parser.process()
        with open(f"aigfuzz/simple_circuit_{i}_processed.eqn", "r") as myfile:
            data = myfile.readlines()
        _ = run.conver_to_sexpr(
            data, multiple_output=True, output_file_path=f"aigfuzz/simple_circuit_{i}.sexpr")
        os.system(
            f"analyzer/target/release/analyzer aigfuzz/simple_circuit_{i}.sexpr {i} > aigfuzz/simple_circuit_{i}.data 2>&1")
        
        # 使用 SExprFeatureExtractor 提取 graph 特征
        sexpr_file = f"aigfuzz/simple_circuit_{i}.sexpr"
        if os.path.exists(sexpr_file):
            try:
                extractor = SExprFeatureExtractor()
                # 先解析 S-expression 文件
                extractor.parse_sexpr_file(sexpr_file)
                # 然后提取 graph 特征
                graph_features = extractor.extract_graph_features()
                
                # 只保存 graph 相关的特征
                graph_info = {}
                if 'graph_nodes' in graph_features:
                    graph_info['graph_nodes'] = graph_features['graph_nodes']
                if 'graph_edges' in graph_features:
                    graph_info['graph_edges'] = graph_features['graph_edges']
                if 'graph_density' in graph_features:
                    graph_info['graph_density'] = graph_features['graph_density']
                if 'avg_degree' in graph_features:
                    graph_info['avg_degree'] = graph_features['avg_degree']
                
                # 保存图信息到文件
                if graph_info:
                    graph_info_file = f"aigfuzz/simple_circuit_{i}_graph_info.txt"
                    with open(graph_info_file, 'w') as f:
                        for key, value in graph_info.items():
                            f.write('%s:%s\n' % (key, value))
            except Exception as e:
                print(f"Warning: Failed to extract graph features for circuit {i}: {e}")
    except Exception as e:
        print(f"Error processing circuit {i}: {e}")

def process_circuits(file_count, max_workers=None):
    # 确保 out_dot 目录存在（analyzer 会在这里输出 .dot 文件）
    if not os.path.exists("out_dot"):
        os.makedirs("out_dot")
    
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(tqdm(
            executor.map(process_circuits_parallel, range(file_count)),
            total=file_count,
            desc='Processing circuits for analyzer'
        ))


def run_abc_parallel(i):
    """并行处理单个电路的 ABC 统计提取"""
    os.system(
        f"{ABC_PATH} -c \"read_eqn aigfuzz/simple_circuit_{i}_processed.eqn; strash; dch -f; print_stats -p; read_lib ../asap7_clean.lib ; map ; topo; upsize; dnsize; stime; \" > aigfuzz/simple_circuit_{i}.stats 2>&1")

def run_abc(file_count, max_workers=None):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(tqdm(
            executor.map(run_abc_parallel, range(file_count)),
            total=file_count,
            desc='Running abc to extract stats'
        ))


def parse_data(file_count):
    print("---------------------Final Step: Parsing Data---------------------")
    def parser(i):
        # 1. 从 .data 文件读取 analyzer 的输出
        with open(f"aigfuzz/simple_circuit_{i}.data", "r") as f:
            data = f.read().split('\n')
            op_dict = {line.split(':')[0]: (line.split(':')[1].strip()) for line in data[:] if line}
        
        # 2. 从 graph_info.txt 读取图指标（如果存在）
        graph_info_file = f"aigfuzz/simple_circuit_{i}_graph_info.txt"
        if os.path.exists(graph_info_file):
            try:
                with open(graph_info_file, "r") as f:
                    graph_data = f.read().split('\n')
                    graph_dict = {line.split(':')[0]: (line.split(':')[1].strip()) 
                                 for line in graph_data[:] if line}
                    op_dict.update(graph_dict)
            except Exception as e:
                print(f"Warning: Failed to read graph info for circuit {i}: {e}")
        
        # 3. 从 .stats 文件读取 ABC 映射结果
        with open(f"aigfuzz/simple_circuit_{i}.stats", "r") as f:
            stats = f.read()
            power_match = re.search(r"power =\s+(\d+\.\d+)", stats)
            power = float(power_match[1]) if power_match else None
            lev_match = re.search(r"lev =\s+(\d+)", stats)
            lev = int(lev_match[1]) if lev_match else None
            area_match = re.search(r"Area =\s+(\d+\.\d+)", stats)
            area = float(area_match[1]) if area_match else None
            delay_match = re.search(r"Delay =\s+(\d+\.\d+)", stats)
            delay = float(delay_match[1]) if delay_match else None
        return {"power": power, "lev": lev, "area": area, "delay": delay, **op_dict}

    df = pd.DataFrame([parser(i) for i in range(file_count)])
    # fill na with 0
    df = df.fillna(0)
    #print("Date count before removing 0s: ", len(df))
    # remove rows that `power` or `delay` or `lev` or `area` is 0
    df = df[(df.power != 0) & (df.delay != 0) & (df.lev != 0) & (df.area != 0)]
    # 构建列顺序（包含 graph 指标，如果存在）
    base_columns = ['+', '!', '*', '&', 
                    'ASTSize',
                    'ASTDepth',
                    'SUM_LIB',
                    'SUM_NODE',
                    'AVE_LIB']
    
    # 添加 graph 指标（如果存在）
    graph_columns = []
    if 'graph_density' in df.columns:
        graph_columns.append('graph_density')
    if 'graph_edges' in df.columns:
        graph_columns.append('graph_edges')
    if 'graph_nodes' in df.columns:
        graph_columns.append('graph_nodes')
    if 'avg_degree' in df.columns:
        graph_columns.append('avg_degree')
    
    # 添加其他列
    other_columns = ['lev', 'power', 'area', 'delay']
    
    # 合并所有列（只包含存在的列）
    all_columns = base_columns + graph_columns + other_columns
    existing_columns = [col for col in all_columns if col in df.columns]
    
    # 添加其他未列出的列（按字母顺序）
    other_existing_cols = sorted([col for col in df.columns if col not in existing_columns])
    final_columns = existing_columns + other_existing_cols
    
    df = df.reindex(columns=final_columns)
    
    
    df.to_csv("simple_circuit_analysis_large.csv", index=False)


if __name__ == "__main__":
    #print(sys.path)
    sys.path.append("..")
    #print(sys.path)
    import run 
    import run_beta
    from CircuitParser import CircuitParser
    
    # 设置全局变量，以便子进程可以访问
    globals()['run'] = run
    globals()['CircuitParser'] = CircuitParser
    
    print(run.__file__)
    
    # 可以通过命令行参数设置并行度，默认使用 CPU 核心数
    import argparse
    parser = argparse.ArgumentParser(description='Collect circuit data with parallel processing')
    parser.add_argument('--file_count', type=int, default=50000, help='Number of circuits to process')
    parser.add_argument('--max_workers', type=int, default=None, help='Maximum number of parallel workers (default: CPU count)')
    args = parser.parse_args()
    
    file_count = args.file_count
    max_workers = args.max_workers
    
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    print(f"Processing {file_count} circuits with {max_workers} workers")
    
    run_aigfuzz(file_count, max_workers=max_workers)
    load_circuits(file_count, max_workers=max_workers)
    process_circuits(file_count, max_workers=max_workers)
    run_abc(file_count, max_workers=max_workers)
    parse_data(file_count)
