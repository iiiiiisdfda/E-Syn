import os
import sys
import pandas as pd
import re
from tqdm import tqdm
import random
import concurrent.futures

# Tool paths - modify these according to your environment
ABC_PATH = "../abc/abc"
AIGTOAIG_PATH = "../sym_reg/aiger_tool_util/aigtoaig"
AIGFUZZ_PATH = "../sym_reg/aiger_tool_util/aigfuzz"

# The current network is not in a topo order (run "topo").?


def run_aigfuzz_parallel(i):
    """并行处理单个电路的生成"""
    os.system(f"{AIGFUZZ_PATH} -c -s > aigfuzz_large/simple_circuit_{i}_large.aig 2>&1")
    os.system(
        f"{ABC_PATH} -c \"read_aiger aigfuzz_large/simple_circuit_{i}_large.aig; trim ; write_aiger aigfuzz_large/simple_circuit_{i}_large.aig\" 2>&1")

def run_aigfuzz(file_count, max_workers=None):
    # check aigfuzz_large/ is esist, if not, create it
    if not os.path.exists("aigfuzz_large"): os.mkdir("aigfuzz_large")
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(tqdm(
            executor.map(run_aigfuzz_parallel, range(file_count)),
            total=file_count,
            desc='Run circuit generator'
        ))

def run_generate_eqn_parallel(i):
    """并行处理单个电路的 EQN 生成"""
    import random
    import traceback
    try:
        # 复杂电路参数（推荐设置）
        in_num = random.randint(20, 40)      # 输入：20-100（增加输入复杂度）
        out_num = random.randint(20, 40)    # 输出：50-200（增加输出数量）
        node_num = random.randint(20, 40)  # 内部节点：100-500（增加电路规模）
        max_depth = random.randint(3, 5) 
            
        ret = os.system(
            f"python ./generate_eqn.py -o aigfuzz_large/simple_circuit_{i}_large.eqn -i {in_num} --outputs {out_num} -n {node_num} --max-depth {max_depth} 2>&1")
        
        if ret != 0:
            print(f"Warning: generate_eqn returned non-zero exit code {ret} for circuit {i}")
            return False
        
        # 检查文件是否成功创建
        if not os.path.exists(f"aigfuzz_large/simple_circuit_{i}_large.eqn"):
            print(f"Warning: EQN file not created for circuit {i}")
            return False
        
        return True
    except Exception as e:
        print(f"Error generating EQN for circuit {i}: {e}")
        traceback.print_exc()
        return False

def run_generate_eqn(file_count, max_workers=None, start_idx=0):
    if not os.path.exists("aigfuzz_large"): os.mkdir("aigfuzz_large")
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    # 使用 submit 而不是 map，以便更好地处理异常
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(run_generate_eqn_parallel, start_idx + i): start_idx + i for i in range(file_count)}
        
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=file_count, desc='Running generate eqn'):
            circuit_idx = futures[future]
            try:
                result = future.result(timeout=600)  # 10分钟超时
                results.append((circuit_idx, result))
            except concurrent.futures.TimeoutError:
                print(f"Circuit {circuit_idx} EQN generation timed out after 10 minutes")
                results.append((circuit_idx, False))
            except concurrent.futures.process.BrokenProcessPool:
                print(f"Circuit {circuit_idx} EQN generation: Process pool was broken (process terminated abruptly)")
                results.append((circuit_idx, False))
            except Exception as e:
                print(f"Circuit {circuit_idx} EQN generation raised an exception: {e}")
                import traceback
                traceback.print_exc()
                results.append((circuit_idx, False))
        
        success_count = sum(1 for _, result in results if result)
        print(f"\nEQN generation complete: {success_count}/{file_count} circuits generated successfully")

def load_circuits_parallel(i):
    """并行处理单个电路的加载和转换"""
    os.system(
        f"{ABC_PATH} -c \"read_aiger aigfuzz_large/simple_circuit_{i}_large.aig; write_eqn aigfuzz_large/simple_circuit_{i}_large.eqn\" 2>&1")
    os.system(
        f"{AIGTOAIG_PATH} aigfuzz_large/simple_circuit_{i}_large.aig aigfuzz_large/simple_circuit_{i}_large.aag 2>&1")

def load_circuits(file_count, max_workers=None):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(tqdm(
            executor.map(load_circuits_parallel, range(file_count)),
            total=file_count,
            desc='Loading circuits and convert to eqn'
        ))

def load_eqn_parallel(i):
    """并行处理单个电路的 EQN 加载和转换"""
    import traceback
    try:
        eqn_file = f"aigfuzz_large/simple_circuit_{i}_large.eqn"
        if not os.path.exists(eqn_file):
            print(f"Warning: {eqn_file} not found for circuit {i}, skipping")
            return False
        
        ret = os.system(
            f"{ABC_PATH} -c \"read_eqn {eqn_file}; strash; write_aiger aigfuzz_large/simple_circuit_{i}_large.aig\" 2>&1")
        
        if ret != 0:
            print(f"Warning: ABC load_eqn returned non-zero exit code {ret} for circuit {i}")
            return False
        
        return True
    except Exception as e:
        print(f"Error loading EQN for circuit {i}: {e}")
        traceback.print_exc()
        return False

def load_eqn(file_count, max_workers=None, start_idx=0):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    # 使用 submit 而不是 map，以便更好地处理异常
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(load_eqn_parallel, start_idx + i): start_idx + i for i in range(file_count)}
        
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=file_count, desc='Loading eqn in abc and convert to aig'):
            circuit_idx = futures[future]
            try:
                result = future.result(timeout=600)  # 10分钟超时
                results.append((circuit_idx, result))
            except concurrent.futures.TimeoutError:
                print(f"Circuit {circuit_idx} load_eqn timed out after 10 minutes")
                results.append((circuit_idx, False))
            except concurrent.futures.process.BrokenProcessPool:
                print(f"Circuit {circuit_idx} load_eqn: Process pool was broken (process terminated abruptly)")
                results.append((circuit_idx, False))
            except Exception as e:
                print(f"Circuit {circuit_idx} load_eqn raised an exception: {e}")
                import traceback
                traceback.print_exc()
                results.append((circuit_idx, False))
        
        success_count = sum(1 for _, result in results if result)
        print(f"\nLoad EQN complete: {success_count}/{file_count} circuits loaded successfully")

def process_circuits_parallel(i):
    """并行处理单个电路的分析"""
    # 在子进程中导入模块
    import sys
    import traceback
    sys.path.append("..")
    
    try:
        import run
        from CircuitParser import CircuitParser
        
        # 检查输入文件是否存在
        eqn_file = f"aigfuzz_large/simple_circuit_{i}_large.eqn"
        if not os.path.exists(eqn_file):
            print(f"Warning: {eqn_file} not found for circuit {i}")
            return False
        
        # 1. CircuitParser 处理
        try:
            parser = CircuitParser(
                eqn_file, f"aigfuzz_large/simple_circuit_{i}_large_processed.eqn")
            parser.process()
        except Exception as e:
            print(f"Error in CircuitParser for circuit {i}: {e}")
            traceback.print_exc()
            return False
        
        # 检查处理后的文件是否存在
        processed_eqn_file = f"aigfuzz_large/simple_circuit_{i}_large_processed.eqn"
        if not os.path.exists(processed_eqn_file):
            print(f"Warning: {processed_eqn_file} not created for circuit {i}")
            return False
        
        # 2. 转换为 S-expression
        try:
            with open(processed_eqn_file, "r") as myfile:
                data = myfile.readlines()
            _ = run.conver_to_sexpr(
                data, multiple_output=True, output_file_path=f"aigfuzz_large/simple_circuit_{i}_large.sexpr")
        except Exception as e:
            print(f"Error converting to S-expression for circuit {i}: {e}")
            traceback.print_exc()
            return False
        
        # 检查 S-expression 文件是否存在
        sexpr_file = f"aigfuzz_large/simple_circuit_{i}_large.sexpr"
        if not os.path.exists(sexpr_file):
            print(f"Warning: {sexpr_file} not created for circuit {i}")
            return False
        
        # 3. 运行 analyzer
        try:
            ret = os.system(
                f"analyzer/target/release/analyzer aigfuzz_large/simple_circuit_{i}_large.sexpr {i} > aigfuzz_large/simple_circuit_{i}_large.data 2>&1")
            if ret != 0:
                print(f"Warning: analyzer returned non-zero exit code {ret} for circuit {i}")
                # 不返回 False，因为 analyzer 可能输出了一些数据
        except Exception as e:
            print(f"Error running analyzer for circuit {i}: {e}")
            traceback.print_exc()
            return False
        
        return True
    except Exception as e:
        print(f"Unexpected error processing circuit {i}: {e}")
        traceback.print_exc()
        return False

def process_circuits(file_count, max_workers=None, start_idx=0):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    # 使用 submit 而不是 map，以便更好地处理异常
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_circuits_parallel, start_idx + i): start_idx + i for i in range(file_count)}
        
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=file_count, desc='Processing circuits for analyzer'):
            circuit_idx = futures[future]
            try:
                result = future.result(timeout=600)  # 10分钟超时
                results.append((circuit_idx, result))
            except concurrent.futures.TimeoutError:
                print(f"Circuit {circuit_idx} timed out after 10 minutes")
                results.append((circuit_idx, False))
            except concurrent.futures.process.BrokenProcessPool:
                print(f"Circuit {circuit_idx}: Process pool was broken (process terminated abruptly)")
                results.append((circuit_idx, False))
            except Exception as e:
                print(f"Circuit {circuit_idx} raised an exception: {e}")
                import traceback
                traceback.print_exc()
                results.append((circuit_idx, False))
        
        # 统计成功和失败的数量
        success_count = sum(1 for _, result in results if result)
        print(f"\nProcessing complete: {success_count}/{file_count} circuits processed successfully")

def run_abc_parallel(i):
    """并行处理单个电路的 ABC 统计提取"""
    import traceback
    try:
        processed_eqn_file = f"aigfuzz_large/simple_circuit_{i}_large_processed.eqn"
        if not os.path.exists(processed_eqn_file):
            print(f"Warning: {processed_eqn_file} not found for circuit {i}, skipping ABC")
            return False
        
        ret = os.system(
            f"{ABC_PATH} -c \"read_eqn {processed_eqn_file}; strash; dch -f; print_stats -p; read_lib ../asap7_clean.lib ; map ; topo; upsize; dnsize; stime; \" > aigfuzz_large/simple_circuit_{i}_large.stats 2>&1")
        
        if ret != 0:
            print(f"Warning: ABC returned non-zero exit code {ret} for circuit {i}")
            return False
        
        return True
    except Exception as e:
        print(f"Error running ABC for circuit {i}: {e}")
        traceback.print_exc()
        return False

def run_abc(file_count, max_workers=None, start_idx=0):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    # 使用 submit 而不是 map，以便更好地处理异常
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(run_abc_parallel, start_idx + i): start_idx + i for i in range(file_count)}
        
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=file_count, desc='Running abc to extract stats'):
            circuit_idx = futures[future]
            try:
                result = future.result(timeout=1200)  # 20分钟超时（ABC 可能需要更长时间）
                results.append((circuit_idx, result))
            except concurrent.futures.TimeoutError:
                print(f"Circuit {circuit_idx} ABC timed out after 20 minutes")
                results.append((circuit_idx, False))
            except concurrent.futures.process.BrokenProcessPool:
                print(f"Circuit {circuit_idx} ABC: Process pool was broken (process terminated abruptly)")
                results.append((circuit_idx, False))
            except Exception as e:
                print(f"Circuit {circuit_idx} ABC raised an exception: {e}")
                import traceback
                traceback.print_exc()
                results.append((circuit_idx, False))
        
        # 统计成功和失败的数量
        success_count = sum(1 for _, result in results if result)
        print(f"\nABC processing complete: {success_count}/{file_count} circuits processed successfully")


def parse_data(file_count):
    print("---------------------Final Step: Parsing Data---------------------")
    def parser(i):
        with open(f"aigfuzz_large/simple_circuit_{i}_large.data", "r") as f:
            data = f.read().split('\n')
            #print(data)
            op_dict = {line.split(':')[0]: (line.split(':')[1].strip()) for line in data[:] if line}
            #op_dict['AVE_LIB'] = float(line.split(':')[1].strip()) for line in data[-2:] if line
        with open(f"aigfuzz_large/simple_circuit_{i}_large.stats", "r") as f:
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
    # sort the columns as +,!,*,&,lev, ASTSize,ASTDepth, power, area , delay
    df = df.reindex(columns=['+', '!', '*', '&', 
                             'ASTSize',
                             'ASTDepth',
                             'SUM_LIB',
                             'SUM_NODE',
                             'AVE_LIB',
                             'lev', 
                             'power', 'area', 'delay'])
    
    
    df.to_csv("simple_circuit_analysis_large.csv", index=False)


def parse_data_project(file_count, start_idx=0, end_idx=None, output_file="simple_circuit_analysis_project_large.csv", append=False):
    """提取 EQN 特征和 stats 映射结果，合并保存为 CSV
    
    Args:
        file_count: 总电路数量（用于确定范围）
        start_idx: 起始索引（包含）
        end_idx: 结束索引（不包含），如果为 None 则使用 file_count
        output_file: 输出文件名
        append: 是否追加模式（True=追加，False=覆盖）
    """
    if end_idx is None:
        end_idx = file_count
    
    print(f"---------------------Parsing Data Project: EQN Features + Stats (Circuits {start_idx}-{end_idx-1})---------------------")
    
    # 导入特征提取器
    # from eqn_feature_extractor import EqnFeatureExtractor
    
    # extractor = EqnFeatureExtractor()

    from sexpr_feature_extractor import SExprFeatureExtractor
    extractor = SExprFeatureExtractor()
    
    def parse_single_circuit(i):
        """解析单个电路的特征和映射结果"""
        result = {}
        

        # 1. 从 S-expression 文件提取特征
        sexpr_file = f"aigfuzz_large/simple_circuit_{i}_large.sexpr"
        if os.path.exists(sexpr_file):
            try:
                sexpr_features = extractor.extract_all_features(sexpr_file)
                result.update(sexpr_features)
            except Exception as e:
                print(f"Warning: Failed to extract features from {sexpr_file}: {e}")
        else:
            print(f"Warning: {sexpr_file} not found")
        
        # # 1. 从 EQN 文件提取特征
        # eqn_file = f"aigfuzz_large/simple_circuit_{i}_large_processed.eqn"
        # if os.path.exists(eqn_file):
        #     try:
        #         eqn_features = extractor.extract_all_features(eqn_file)
        #         result.update(eqn_features)
        #     except Exception as e:
        #         print(f"Warning: Failed to extract features from {eqn_file}: {e}")
        # else:
        #     print(f"Warning: {eqn_file} not found")
        
        # 2. 从 stats 文件提取映射结果
        stats_file = f"aigfuzz_large/simple_circuit_{i}_large.stats"
        if os.path.exists(stats_file):
            try:
                with open(stats_file, "r") as f:
                    stats = f.read()
                
                # 提取 power
                power_match = re.search(r"power =\s+(\d+\.\d+)", stats)
                result['power'] = float(power_match[1]) if power_match else None
                
                # 提取 lev (logic level)
                lev_match = re.search(r"lev =\s+(\d+)", stats)
                result['lev'] = int(lev_match[1]) if lev_match else None
                
                # 提取 Area
                area_match = re.search(r"Area =\s+(\d+\.\d+)", stats)
                result['area'] = float(area_match[1]) if area_match else None
                
                # 提取 Delay
                delay_match = re.search(r"Delay =\s+(\d+\.\d+)", stats)
                result['delay'] = float(delay_match[1]) if delay_match else None
                
                # 提取 Gates
                gates_match = re.search(r"Gates =\s+(\d+)", stats)
                result['gates'] = int(gates_match[1]) if gates_match else None
                
                # 提取 Cap
                cap_match = re.search(r"Cap =\s+(\d+\.\d+)\s+ff", stats)
                result['cap'] = float(cap_match[1]) if cap_match else None
                
                # 提取 i/o 信息
                io_match = re.search(r"i/o =\s+(\d+)/(\d+)", stats)
                if io_match:
                    result['num_inputs_abc'] = int(io_match[1])
                    result['num_outputs_abc'] = int(io_match[2])
                
                # 提取 and 门数量
                and_match = re.search(r"and =\s+(\d+)", stats)
                result['and_gates'] = int(and_match[1]) if and_match else None
                
            except Exception as e:
                print(f"Warning: Failed to parse {stats_file}: {e}")
        else:
            print(f"Warning: {stats_file} not found")
        
        return result
    
    # 解析指定范围的电路
    data_list = []
    for i in tqdm(range(start_idx, end_idx), desc=f'Parsing circuits {start_idx}-{end_idx-1}'):
        data = parse_single_circuit(i)
        data_list.append(data)
    
    # 创建 DataFrame
    df = pd.DataFrame(data_list)
    
    # 填充缺失值为 0
    df = df.fillna(0)
    
    # 移除无效行（power, delay, lev, area 都为 0 的行）
    df = df[(df['power'] != 0) & (df['delay'] != 0) & (df['lev'] != 0) & (df['area'] != 0)]
    
    # 保存为 CSV
    if append and os.path.exists(output_file):
        # 追加模式：不包含表头
        df.to_csv(output_file, mode='a', header=False, index=False)
        print(f"\n数据已追加到: {output_file} (本批 {len(df)} 行)")
    else:
        # 覆盖模式：包含表头
        df.to_csv(output_file, index=False)
        print(f"\n数据已保存到: {output_file} (本批 {len(df)} 行)")
    
    print(f"本批有效行数: {len(df)}")
    print(f"总列数: {len(df.columns)}")
    
    return df

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
    parser.add_argument('--file_count', type=int, default=60000, help='Number of circuits to process')
    parser.add_argument('--max_workers', type=int, default=None, help='Maximum number of parallel workers (default: CPU count)')
    args = parser.parse_args()
    
    file_count = args.file_count
    max_workers = args.max_workers
    
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    print(f"Processing {file_count} circuits with {max_workers} workers")
    
    # 分批处理参数
    batch_size = 100
    output_file = "simple_circuit_analysis_project_large.csv"
    
    # 检查输出文件是否已存在
    file_exists = os.path.exists(output_file)
    if file_exists:
        # 读取现有文件，获取已有数据的最大索引
        try:
            existing_df = pd.read_csv(output_file)
            if len(existing_df) > 0:
                print(f"检测到已存在的输出文件: {output_file}")
                print(f"现有数据行数: {len(existing_df)}")
                # 如果文件存在，从文件末尾继续追加
                # 这里假设需要从 file_count 开始继续处理
                # 如果需要从现有数据的末尾继续，需要更复杂的逻辑
        except Exception as e:
            print(f"警告: 无法读取现有文件 {output_file}: {e}")
            file_exists = False
    
    # 分批处理
    total_batches = (file_count + batch_size - 1) // batch_size
    print(f"\n将分 {total_batches} 批处理，每批 {batch_size} 个电路\n")
    
    for batch_idx in range(total_batches):
        start_idx = batch_idx * batch_size
        end_idx = min((batch_idx + 1) * batch_size, file_count)
        
        print(f"\n{'='*80}")
        print(f"处理第 {batch_idx + 1}/{total_batches} 批: 电路 {start_idx} 到 {end_idx - 1}")
        print(f"{'='*80}\n")
        
        # 处理当前批次（使用绝对索引）
        batch_size_actual = end_idx - start_idx
        # run_aigfuzz(batch_size_actual, max_workers=max_workers, start_idx=start_idx)  # 如果需要生成新电路
        run_generate_eqn(batch_size_actual, max_workers=max_workers, start_idx=start_idx)
        # load_circuits(batch_size_actual, max_workers=max_workers, start_idx=start_idx)
        load_eqn(batch_size_actual, max_workers=max_workers, start_idx=start_idx)
        process_circuits(batch_size_actual, max_workers=max_workers, start_idx=start_idx)
        run_abc(batch_size_actual, max_workers=max_workers, start_idx=start_idx)
        
        # 解析并保存当前批次的数据到CSV
        # 如果文件已存在或是第一批，使用追加模式；否则覆盖写入
        parse_data_project(
            file_count=file_count,  # 总电路数量
            start_idx=start_idx,
            end_idx=end_idx,
            output_file=output_file,
            append=(file_exists or batch_idx > 0)  # 如果文件已存在或是第二批及以后，追加写入
        )
        
        print(f"\n第 {batch_idx + 1}/{total_batches} 批处理完成！\n")
    
    # 最终统计
    if os.path.exists(output_file):
        final_df = pd.read_csv(output_file)
        print(f"\n{'='*80}")
        print(f"所有批次处理完成！")
        print(f"最终文件: {output_file}")
        print(f"总行数: {len(final_df)}")
        print(f"总列数: {len(final_df.columns)}")
        print(f"{'='*80}")
# 