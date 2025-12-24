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

def run_generate_eqn_parallel(i):
    """并行处理单个电路的 EQN 生成"""
    import random
    import traceback
    try:
        # 复杂电路参数（推荐设置）
        in_num = random.randint(40, 100)      # 输入：20-100（增加输入复杂度）
        out_num = random.randint(40, 100)    # 输出：50-200（增加输出数量）
        node_num = random.randint(40, 100)  # 内部节点：100-500（增加电路规模）
        max_depth = random.randint(5, 10) 
            
        ret = os.system(
            f"python ./generate_eqn.py -o aigfuzz/simple_circuit_{i}.eqn -i {in_num} --outputs {out_num} -n {node_num} --max-depth {max_depth} 2>&1")
        
        if ret != 0:
            print(f"Warning: generate_eqn returned non-zero exit code {ret} for circuit {i}")
            return False
        
        # 检查文件是否成功创建
        if not os.path.exists(f"aigfuzz/simple_circuit_{i}.eqn"):
            print(f"Warning: EQN file not created for circuit {i}")
            return False
        
        return True
    except Exception as e:
        print(f"Error generating EQN for circuit {i}: {e}")
        traceback.print_exc()
        return False

def run_generate_eqn(file_count, max_workers=None):
    if not os.path.exists("aigfuzz"): os.mkdir("aigfuzz")
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    # 使用 submit 而不是 map，以便更好地处理异常
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(run_generate_eqn_parallel, i): i for i in range(file_count)}
        
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=file_count, desc='Running generate eqn'):
            i = futures[future]
            try:
                result = future.result(timeout=600)  # 10分钟超时
                results.append((i, result))
            except concurrent.futures.TimeoutError:
                print(f"Circuit {i} EQN generation timed out after 10 minutes")
                results.append((i, False))
            except Exception as e:
                print(f"Circuit {i} EQN generation raised an exception: {e}")
                results.append((i, False))
        
        success_count = sum(1 for _, result in results if result)
        print(f"\nEQN generation complete: {success_count}/{file_count} circuits generated successfully")

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

def load_eqn_parallel(i):
    """并行处理单个电路的 EQN 加载和转换"""
    import traceback
    try:
        eqn_file = f"aigfuzz/simple_circuit_{i}.eqn"
        if not os.path.exists(eqn_file):
            print(f"Warning: {eqn_file} not found for circuit {i}, skipping")
            return False
        
        ret = os.system(
            f"{ABC_PATH} -c \"read_eqn {eqn_file}; strash; write_aiger aigfuzz/simple_circuit_{i}.aig\" 2>&1")
        
        if ret != 0:
            print(f"Warning: ABC load_eqn returned non-zero exit code {ret} for circuit {i}")
            return False
        
        return True
    except Exception as e:
        print(f"Error loading EQN for circuit {i}: {e}")
        traceback.print_exc()
        return False

def load_eqn(file_count, max_workers=None):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    # 使用 submit 而不是 map，以便更好地处理异常
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(load_eqn_parallel, i): i for i in range(file_count)}
        
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=file_count, desc='Loading eqn in abc and convert to aig'):
            i = futures[future]
            try:
                result = future.result(timeout=600)  # 10分钟超时
                results.append((i, result))
            except concurrent.futures.TimeoutError:
                print(f"Circuit {i} load_eqn timed out after 10 minutes")
                results.append((i, False))
            except Exception as e:
                print(f"Circuit {i} load_eqn raised an exception: {e}")
                results.append((i, False))
        
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
        eqn_file = f"aigfuzz/simple_circuit_{i}.eqn"
        if not os.path.exists(eqn_file):
            print(f"Warning: {eqn_file} not found for circuit {i}")
            return False
        
        # 1. CircuitParser 处理
        try:
            parser = CircuitParser(
                eqn_file, f"aigfuzz/simple_circuit_{i}_processed.eqn")
            parser.process()
        except Exception as e:
            print(f"Error in CircuitParser for circuit {i}: {e}")
            traceback.print_exc()
            return False
        
        # 检查处理后的文件是否存在
        processed_eqn_file = f"aigfuzz/simple_circuit_{i}_processed.eqn"
        if not os.path.exists(processed_eqn_file):
            print(f"Warning: {processed_eqn_file} not created for circuit {i}")
            return False
        
        # 2. 转换为 S-expression
        try:
            with open(processed_eqn_file, "r") as myfile:
                data = myfile.readlines()
            _ = run.conver_to_sexpr(
                data, multiple_output=True, output_file_path=f"aigfuzz/simple_circuit_{i}.sexpr")
        except Exception as e:
            print(f"Error converting to S-expression for circuit {i}: {e}")
            traceback.print_exc()
            return False
        
        # 检查 S-expression 文件是否存在
        sexpr_file = f"aigfuzz/simple_circuit_{i}.sexpr"
        if not os.path.exists(sexpr_file):
            print(f"Warning: {sexpr_file} not created for circuit {i}")
            return False
        
        # 3. 运行 analyzer
        try:
            ret = os.system(
                f"analyzer/target/release/analyzer aigfuzz/simple_circuit_{i}.sexpr {i} > aigfuzz/simple_circuit_{i}.data 2>&1")
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

def process_circuits(file_count, max_workers=None):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    # 使用 submit 而不是 map，以便更好地处理异常
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_circuits_parallel, i): i for i in range(file_count)}
        
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=file_count, desc='Processing circuits for analyzer'):
            i = futures[future]
            try:
                result = future.result(timeout=600)  # 10分钟超时
                results.append((i, result))
            except concurrent.futures.TimeoutError:
                print(f"Circuit {i} timed out after 10 minutes")
                results.append((i, False))
            except Exception as e:
                print(f"Circuit {i} raised an exception: {e}")
                results.append((i, False))
        
        # 统计成功和失败的数量
        success_count = sum(1 for _, result in results if result)
        print(f"\nProcessing complete: {success_count}/{file_count} circuits processed successfully")

def run_abc_parallel(i):
    """并行处理单个电路的 ABC 统计提取"""
    import traceback
    try:
        processed_eqn_file = f"aigfuzz/simple_circuit_{i}_processed.eqn"
        if not os.path.exists(processed_eqn_file):
            print(f"Warning: {processed_eqn_file} not found for circuit {i}, skipping ABC")
            return False
        
        ret = os.system(
            f"{ABC_PATH} -c \"read_eqn {processed_eqn_file}; strash; dch -f; print_stats -p; read_lib ../asap7_clean.lib ; map ; topo; upsize; dnsize; stime; \" > aigfuzz/simple_circuit_{i}.stats 2>&1")
        
        if ret != 0:
            print(f"Warning: ABC returned non-zero exit code {ret} for circuit {i}")
            return False
        
        return True
    except Exception as e:
        print(f"Error running ABC for circuit {i}: {e}")
        traceback.print_exc()
        return False

def run_abc(file_count, max_workers=None):
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    # 使用 submit 而不是 map，以便更好地处理异常
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(run_abc_parallel, i): i for i in range(file_count)}
        
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=file_count, desc='Running abc to extract stats'):
            i = futures[future]
            try:
                result = future.result(timeout=1200)  # 20分钟超时（ABC 可能需要更长时间）
                results.append((i, result))
            except concurrent.futures.TimeoutError:
                print(f"Circuit {i} ABC timed out after 20 minutes")
                results.append((i, False))
            except Exception as e:
                print(f"Circuit {i} ABC raised an exception: {e}")
                results.append((i, False))
        
        # 统计成功和失败的数量
        success_count = sum(1 for _, result in results if result)
        print(f"\nABC processing complete: {success_count}/{file_count} circuits processed successfully")


def parse_data(file_count):
    print("---------------------Final Step: Parsing Data---------------------")
    def parser(i):
        with open(f"aigfuzz/simple_circuit_{i}.data", "r") as f:
            data = f.read().split('\n')
            #print(data)
            op_dict = {line.split(':')[0]: (line.split(':')[1].strip()) for line in data[:] if line}
            #op_dict['AVE_LIB'] = float(line.split(':')[1].strip()) for line in data[-2:] if line
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


def parse_data_project(file_count):
    """提取 EQN 特征和 stats 映射结果，合并保存为 CSV"""
    print("---------------------Parsing Data Project: EQN Features + Stats---------------------")
    
    # 导入特征提取器
    # from eqn_feature_extractor import EqnFeatureExtractor
    
    # extractor = EqnFeatureExtractor()

    from sexpr_feature_extractor import SExprFeatureExtractor
    extractor = SExprFeatureExtractor()
    
    def parse_single_circuit(i):
        """解析单个电路的特征和映射结果"""
        result = {}
        

        # 1. 从 S-expression 文件提取特征
        sexpr_file = f"aigfuzz/simple_circuit_{i}.sexpr"
        if os.path.exists(sexpr_file):
            try:
                sexpr_features = extractor.extract_all_features(sexpr_file)
                result.update(sexpr_features)
            except Exception as e:
                print(f"Warning: Failed to extract features from {sexpr_file}: {e}")
        else:
            print(f"Warning: {sexpr_file} not found")
        
        # # 1. 从 EQN 文件提取特征
        # eqn_file = f"aigfuzz/simple_circuit_{i}_processed.eqn"
        # if os.path.exists(eqn_file):
        #     try:
        #         eqn_features = extractor.extract_all_features(eqn_file)
        #         result.update(eqn_features)
        #     except Exception as e:
        #         print(f"Warning: Failed to extract features from {eqn_file}: {e}")
        # else:
        #     print(f"Warning: {eqn_file} not found")
        
        # 2. 从 stats 文件提取映射结果
        stats_file = f"aigfuzz/simple_circuit_{i}.stats"
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
    
    # 解析所有电路
    data_list = []
    for i in tqdm(range(file_count), desc='Parsing circuits'):
        data = parse_single_circuit(i)
        data_list.append(data)
    
    # 创建 DataFrame
    df = pd.DataFrame(data_list)
    
    # 填充缺失值为 0
    df = df.fillna(0)
    
    # 移除无效行（power, delay, lev, area 都为 0 的行）
    df = df[(df['power'] != 0) & (df['delay'] != 0) & (df['lev'] != 0) & (df['area'] != 0)]
    
    # 保存为 CSV
    output_file = "simple_circuit_analysis_project.csv"
    df.to_csv(output_file, index=False)
    
    print(f"\n数据已保存到: {output_file}")
    print(f"总行数: {len(df)}")
    print(f"总列数: {len(df.columns)}")
    print(f"\n列名: {', '.join(df.columns.tolist())}")
    
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
    parser.add_argument('--file_count', type=int, default=1000, help='Number of circuits to process')
    parser.add_argument('--max_workers', type=int, default=None, help='Maximum number of parallel workers (default: CPU count)')
    args = parser.parse_args()
    
    file_count = args.file_count
    max_workers = args.max_workers
    
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    print(f"Processing {file_count} circuits with {max_workers} workers")
    
    # run_aigfuzz(file_count, max_workers=max_workers)
    run_generate_eqn(file_count, max_workers=max_workers)
    # load_circuits(file_count, max_workers=max_workers)
    load_eqn(file_count, max_workers=max_workers)
    process_circuits(file_count, max_workers=max_workers)
    run_abc(file_count, max_workers=max_workers)
    # parse_data(file_count)
    parse_data_project(file_count)
# 