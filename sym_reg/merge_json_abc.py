import json
import pandas as pd
import re
import concurrent.futures
from tqdm import tqdm
import os
from eqn_feature_extractor_eqn import EqnFeatureExtractorEqn

from generate_eqn_aigfuzz_small import AigfuzzSmallGenerator

from concurrent.futures import ProcessPoolExecutor, as_completed

ABC_PATH = "../abc/abc"
FILE_COUNT = 50000
FOLDER_NAME = f"large_{FILE_COUNT}_finc"

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)


def eqn_to_sexpr(eqn_file_path, output_file_path=None):
    """
    高效地将 EQN 文件展开并转换为 S-expression 格式
    
    Args:
        eqn_file_path: EQN 文件路径
        output_file_path: 输出 S-expression 文件路径（可选）
    
    Returns:
        S-expression 字符串
    """
    import re
    
    # 解析 EQN 文件
    inputs = []
    outputs = []
    nodes = {}  # node_name -> expression
    
    with open(eqn_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # 解析 INORDER
            if line.startswith('INORDER'):
                vars_str = line.split('=', 1)[1].rstrip(';').strip()
                inputs = vars_str.split()
                continue
            
            # 解析 OUTORDER
            if line.startswith('OUTORDER'):
                vars_str = line.split('=', 1)[1].rstrip(';').strip()
                outputs = vars_str.split()
                continue
            
            # 解析节点定义
            if '=' in line:
                parts = line.split('=', 1)
                if len(parts) == 2:
                    node_name = parts[0].strip()
                    expression = parts[1].rstrip(';').strip()
                    nodes[node_name] = expression
    
    # 构建输入变量集合
    input_set = set(inputs)
    
    # 递归展开表达式中的中间变量
    def expand_expression(expr, visited=None):
        """展开表达式，将所有中间变量替换为其定义"""
        if visited is None:
            visited = set()
        
        # 提取所有标识符（变量和节点名）
        tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expr)
        
        # 替换中间变量（不包括输入变量）
        for token in tokens:
            if token in nodes and token not in input_set and token not in visited:
                visited.add(token)
                # 递归展开该节点的表达式
                expanded = expand_expression(nodes[token], visited.copy())
                # 替换所有出现的 token（使用单词边界确保精确匹配）
                expr = re.sub(r'\b' + re.escape(token) + r'\b', f'({expanded})', expr)
                visited.remove(token)
        
        return expr
    
    # 将表达式转换为 S-expression 格式
    def expr_to_sexpr(expr):
        """将展开后的表达式转换为 S-expression"""
        expr = expr.strip()
        if not expr:
            return expr
        
        # 移除外层括号（如果是完整的括号表达式）
        while expr.startswith('(') and expr.endswith(')'):
            depth = 0
            is_complete = True
            for i, char in enumerate(expr):
                if char == '(':
                    depth += 1
                elif char == ')':
                    depth -= 1
                    if depth == 0 and i < len(expr) - 1:
                        is_complete = False
                        break
            if is_complete:
                expr = expr[1:-1].strip()
            else:
                break
        
        # 处理 NOT (!)，优先级最高
        if expr.startswith('!'):
            inner = expr[1:].strip()
            # 处理连续的 NOT
            not_count = 0
            while inner.startswith('!'):
                not_count += 1
                inner = inner[1:].strip()
            # 处理括号
            if inner.startswith('(') and inner.endswith(')'):
                inner = inner[1:-1].strip()
            result = expr_to_sexpr(inner)
            for _ in range(not_count + 1):
                result = f"(! {result})"
            return result
        
        # 按运算符优先级处理（从低到高：+ (OR), ^ (XOR), * (AND)）
        # 从右到左查找最外层的运算符
        
        # 处理 OR (+)，优先级最低
        depth = 0
        for i in range(len(expr) - 1, -1, -1):
            char = expr[i]
            if char == ')':
                depth += 1
            elif char == '(':
                depth -= 1
            elif char == '+' and depth == 0:
                left = expr[:i].strip()
                right = expr[i+1:].strip()
                return f"(+ {expr_to_sexpr(left)} {expr_to_sexpr(right)})"
        
        # 处理 XOR (^)
        depth = 0
        for i in range(len(expr) - 1, -1, -1):
            char = expr[i]
            if char == ')':
                depth += 1
            elif char == '(':
                depth -= 1
            elif char == '^' and depth == 0:
                left = expr[:i].strip()
                right = expr[i+1:].strip()
                return f"(^ {expr_to_sexpr(left)} {expr_to_sexpr(right)})"
        
        # 处理 AND (*)，优先级最高
        depth = 0
        for i in range(len(expr) - 1, -1, -1):
            char = expr[i]
            if char == ')':
                depth += 1
            elif char == '(':
                depth -= 1
            elif char == '*' and depth == 0:
                left = expr[:i].strip()
                right = expr[i+1:].strip()
                return f"(& {expr_to_sexpr(left)} {expr_to_sexpr(right)})"
        
        # 基础变量或数字
        return expr
    
    # 展开所有输出表达式并合并
    expanded_outputs = []
    for output in outputs:
        if output in nodes:
            # 展开该输出的表达式
            expanded = expand_expression(nodes[output])
            sexpr = expr_to_sexpr(expanded)
            expanded_outputs.append(sexpr)
        elif output in input_set:
            # 输出直接是输入变量
            expanded_outputs.append(output)
        else:
            # 未知的输出，保持原样
            expanded_outputs.append(output)
    
    # 如果有多个输出，使用 AND 连接所有输出
    if len(expanded_outputs) == 1:
        result = expanded_outputs[0]
    else:
        # 多个输出时，使用 AND 连接所有输出
        result = expanded_outputs[0]
        for out in expanded_outputs[1:]:
            result = f"(& {result} {out})"
    
    # 写入文件（如果指定了输出路径）
    if output_file_path:
        with open(output_file_path, 'w') as f:
            f.write(result)
    
    return result   

def run_abc_parallel(i):
    """并行处理单个电路的 ABC 统计提取"""
    os.system(
        f"{ABC_PATH} -c \"read_eqn {FOLDER_NAME}/simple_circuit_{i}.eqn; strash; dch -f; print_stats -p; read_lib ../asap7_clean.lib ; map ; topo; upsize; dnsize; stime; \" > {FOLDER_NAME}/simple_circuit_{i}.stats 2>&1")

def run_abc(file_count, max_workers=None, parallel=True):
    
    
    
    if max_workers is None:
        max_workers = min(64, os.cpu_count() or 1)
    
    if parallel and max_workers > 1:
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            list(tqdm(
                executor.map(run_abc_parallel, range(file_count)),
                total=file_count,
                desc='Running abc to extract stats'
            ))
    else:
        # 串行執行
        for i in tqdm(range(file_count), desc='Running abc to extract stats'):
            run_abc_parallel(i)

features_list = []
eqn_feature_extractor = EqnFeatureExtractorEqn()

# for i in tqdm(range(50000)):
#     file_name = f"{FOLDER_NAME}/simple_circuit_{i}.eqn"
#     features = eqn_feature_extractor.extract_all_features(file_name)
#     features_list.append(features)
    
def parse_single_circuit(i):
        """解析单个电路的特征和映射结果"""
        result = {}
        
        
        # 1. 从 eqn 文件提取特征
        file_name = f"{FOLDER_NAME}/simple_circuit_{i}.eqn"
        features = eqn_feature_extractor.extract_all_features(file_name)
        result.update(features)
        
        # 2. 从 stats 文件提取映射结果
        stats_file = f"{FOLDER_NAME}/simple_circuit_{i}.stats"
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

if __name__ == "__main__":
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
    # generate eqn file
    
    def generate_eqn_parallel(i):
        AigfuzzSmallGenerator().generate_eqn_file(f"{FOLDER_NAME}/simple_circuit_{i}.eqn", large=True)
    
    with ProcessPoolExecutor(max_workers=16) as executor:
        list(tqdm(executor.map(generate_eqn_parallel, range(FILE_COUNT)), total=FILE_COUNT, desc='Generate EQN'))
        
    # run abc to get stats file
    def run_abc_parallel(i):
        os.system(
            f"{ABC_PATH} -c \"read_eqn {FOLDER_NAME}/simple_circuit_{i}.eqn; strash; dch -f; print_stats -p; read_lib ../asap7_clean.lib ; map ; topo; upsize; dnsize; stime; \" > {FOLDER_NAME}/simple_circuit_{i}.stats 2>&1")
    
    with ProcessPoolExecutor(max_workers=16) as executor:
        list(tqdm(executor.map(run_abc_parallel, range(FILE_COUNT)), total=FILE_COUNT, desc='Run ABC'))
        
    # get csv file
    def get_csv_file_parallel(i):
        file_name = f"{FOLDER_NAME}/simple_circuit_{i}.eqn"
        features = eqn_feature_extractor.extract_all_features(file_name)
        return features
    
    data_list = []
    completed_count = 0
    with ProcessPoolExecutor(max_workers=16) as executor:
        futures = {executor.submit(get_csv_file_parallel, i): i for i in range(FILE_COUNT)}
        for f in tqdm(as_completed(futures), total=FILE_COUNT, desc='Get CSV File'):
            data = f.result()
            completed_count += 1
            data_list.append(data)
            if completed_count % 2500 == 0 and completed_count > 10000:
                df = pd.DataFrame(data_list)
                df.to_csv(f'{FOLDER_NAME}_c{completed_count}.csv', index=False)
    df = pd.DataFrame(data_list)
    df.to_csv(f'{FOLDER_NAME}.csv', index=False)
    print(f'save the training data to {FOLDER_NAME}.csv')
    # filter csv file
    def filter_csv_file(i):
        df = pd.read_csv(f'{FOLDER_NAME}_c{i}.csv')
        df = df[~(
            (df['area'] == 0) | 
            (df['area'].isna()) | 
            (df['delay'] == 0) | 
            (df['delay'].isna())
        )]
        df.to_csv(f'{FOLDER_NAME}_c{i}_filtered.csv', index=False)
        print(f'filter the training data and save to {FOLDER_NAME}_c{i}_filtered.csv')
        return df
    
    if FILE_COUNT >= 12500:
        filter_csv_file(12500)
    if FILE_COUNT >= 15000:
        filter_csv_file(15000)
    if FILE_COUNT >= 17500:
        filter_csv_file(17500)
    if FILE_COUNT >= 20000:
        filter_csv_file(20000)
    if FILE_COUNT >= 22500:
        filter_csv_file(22500)
    if FILE_COUNT >= 25000:
        filter_csv_file(25000)
    if FILE_COUNT >= 27500:
        filter_csv_file(27500)
    if FILE_COUNT >= 30000:
        filter_csv_file(30000)
    if FILE_COUNT >= 32500:
        filter_csv_file(32500)
    if FILE_COUNT >= 35000:
        filter_csv_file(35000)
    if FILE_COUNT >= 37500:
        filter_csv_file(37500)
    if FILE_COUNT >= 40000:
        filter_csv_file(40000)
    if FILE_COUNT >= 42500:
        filter_csv_file(42500)
    if FILE_COUNT >= 45000:
        filter_csv_file(45000)
    if FILE_COUNT >= 47500:
        filter_csv_file(47500)
    if FILE_COUNT >= 50000:
        filter_csv_file(50000)
    
    
# def run_abc_debug(i):
#     stats_file = f"{FOLDER_NAME}/simple_circuit_{i}.stats"
#     eqn_file = f"{FOLDER_NAME}/simple_circuit_{i}.eqn"
#     if not os.path.isfile(eqn_file):
#         print(f"{eqn_file} not found, rebuilding")
#         AigfuzzSmallGenerator().generate_eqn_file(f"{FOLDER_NAME}/simple_circuit_{i}.eqn", medium=True)
#         run_abc_parallel(i)
#     if os.path.isfile(stats_file):
#         try:
#             with open(stats_file, "r") as f:
#                 content = f.read()
#             if "Segmentation fault (core dumped)" in content:
#                 print(f"Rebuilding {stats_file} because it contains 'Segmentation fault (core dumped)'")
#                 os.remove(stats_file)
#                 AigfuzzSmallGenerator().generate_eqn_file(f"{FOLDER_NAME}/simple_circuit_{i}.eqn", medium=True)
#                 run_abc_parallel(i)
#             if not content.startswith("ABC command line:"):
#                 print(f"Rebuilding {stats_file} because it is empty")
#                 os.remove(stats_file)
#                 AigfuzzSmallGenerator().generate_eqn_file(f"{FOLDER_NAME}/simple_circuit_{i}.eqn", medium=True)
#                 run_abc_parallel(i)
#         except Exception as e:
#             print(f"Error processing {stats_file}: {e}")
#     else:
#         print(f"{stats_file} not found, rebuilding")
#         AigfuzzSmallGenerator().generate_eqn_file(f"{FOLDER_NAME}/simple_circuit_{i}.eqn", medium=True)
#         run_abc_parallel(i)

# def eqn_to_sexpr_parallel(i):
#     file_name = f"{FOLDER_NAME}/simple_circuit_{i}.eqn"
#     eqn_to_sexpr(file_name, f"{FOLDER_NAME}/simple_circuit_{i}.sexpr")


# with ProcessPoolExecutor(max_workers=16) as executor:
#     list(tqdm(executor.map(run_abc_debug, range(10000)), total=10000, desc='Run ABC Debug'))


# data_list = []
# completed_count = 0

# with ProcessPoolExecutor(max_workers=16) as executor:
#     futures = {executor.submit(parse_single_circuit, i): i for i in range(10000)}
#     for f in tqdm(as_completed(futures), total=10000, desc='取得特徵'):
#         data = f.result()
#         completed_count += 1
#         data_list.append(data)
#         if completed_count % 2500 == 0 and completed_count > 10000:
#             df = pd.DataFrame(data_list)
#             df.to_csv(f'{FOLDER_NAME}_c{completed_count}.csv', index=False)
            
    
# df = pd.DataFrame(data_list)
# df.to_csv(f'{FOLDER_NAME}.csv', index=False)



# csv_file1 = pd.read_csv('/home/str367/lsv_final/E-Syn_local/sym_reg/aigfuzz_10000_large_abc.csv')

# csv_file2 = pd.read_csv(f'/home/str367/lsv_final/E-Syn_local/sym_reg/large_50000_c15000.csv')

# # 檢查 'area' 與 'delay' column，分別印出為0與為NaN的行數

# # 檢查 'area' 欄位
# num_area_zero = (csv_file2['area'] == 0).sum()
# num_area_nan = csv_file2['area'].isna().sum()
# print(f"'area' 為 0 的行數: {num_area_zero}")
# print(f"'area' 為 NaN 的行數: {num_area_nan}")

# # 檢查 'delay' 欄位
# num_delay_zero = (csv_file2['delay'] == 0).sum()
# num_delay_nan = csv_file2['delay'].isna().sum()
# print(f"'delay' 為 0 的行數: {num_delay_zero}")
# print(f"'delay' 為 NaN 的行數: {num_delay_nan}")

# # 刪除 'area' 或 'delay' 欄位為0或NaN的行，並存成新的CSV
# filtered_csv = csv_file2[~(
#     (csv_file2['area'] == 0) | 
#     (csv_file2['area'].isna()) | 
#     (csv_file2['delay'] == 0) | 
#     (csv_file2['delay'].isna())
# )]
# # 刪除 num_inputs_abc 和 num_outputs_abc 欄位（如果存在）
# if 'num_inputs_abc' in filtered_csv.columns:
#     filtered_csv = filtered_csv.drop(columns=['num_inputs_abc'])
# if 'num_outputs_abc' in filtered_csv.columns:
#     filtered_csv = filtered_csv.drop(columns=['num_outputs_abc'])

# filtered_csv.to_csv(f"/home/str367/lsv_final/E-Syn_local/sym_reg/large_15000_filtered.csv", index=False)
# print(f"已儲存過濾後的csv到 large_15000_filtered.csv，共 {filtered_csv.shape[0]} 行")




# # 檢查這兩個檔案csv檔案是否有完全一致的column name

# columns1 = set(csv_file1.columns)
# columns2 = set(csv_file2.columns)

# if columns1 == columns2:
#     print("兩個CSV檔案有完全一致的column name")
# else:
#     print("兩個CSV檔案的column name不完全一致")
#     print("只在csv_file1中的columns:", columns1 - columns2)
#     print("只在csv_file2中的columns:", columns2 - columns1)
#     print("共同columns:", columns1 & columns2)

# def parse_stats(i):
#     """解析单个电路的统计信息，返回结果字典"""
#     file_name = f"{FOLDER_NAME}/simple_circuit_{i}.eqn"
#     stats_file = f"tmp{i}.stats"
    
#     os.system(
#         f"{ABC_PATH} -c \"read_eqn {file_name}; print_stats \" > {stats_file}")
    
#     result = {
#         'valid': False,
#         'num_inputs': 0,
#         'num_outputs': 0,
#         'lat': 0,
#         'nd': 0,
#         'edge': 0,
#         'aig': 0,
#         'lev': 0
#     }
    
#     try:
#         with open(stats_file, "r") as f:
#             content = f.read()
#         # 解析範例: large_50000/simple_circuit_0  : i/o =  234/  215  lat =    0  nd =  6727  edge =  13113  aig  =  8308  lev = 179
#         match = re.search(
#             r"i/o\s*=\s*(\d+)\s*/\s*(\d+)\s*lat\s*=\s*(\d+)\s*nd\s*=\s*(\d+)\s*edge\s*=\s*(\d+)\s*aig\s*=\s*(\d+)\s*lev\s*=\s*(\d+)",
#             content)
#         if match:
#             result['valid'] = True
#             result['num_inputs'] = int(match.group(1))
#             result['num_outputs'] = int(match.group(2))
#             result['lat'] = int(match.group(3))
#             result['nd'] = int(match.group(4))
#             result['edge'] = int(match.group(5))
#             result['aig'] = int(match.group(6))
#             result['lev'] = int(match.group(7))
#     except Exception as e:
#         print(f"Error parsing stats for circuit {i}: {e}")
#     finally:
#         if os.path.exists(stats_file):
#             os.remove(stats_file)
    
#     return result


# # 使用 ProcessPoolExecutor 并行处理
# with ProcessPoolExecutor(max_workers=16) as executor:
#     results = list(tqdm(executor.map(parse_stats, range(50000)), total=50000, desc='Parse Stats'))

# # 在主进程中汇总结果
# avg_input = 0
# avg_output = 0
# avg_node = 0
# avg_lev = 0
# aig_num = 0
# file_count = 0

# for result in results:
#     if result['valid']:
#         file_count += 1
#         avg_input += result['num_inputs']
#         avg_output += result['num_outputs']
#         avg_node += result['nd']
#         avg_lev += result['lev']
#         aig_num += result['aig']

# if file_count > 0:
#     print(f"avg_input: {avg_input / file_count}")
#     print(f"avg_output: {avg_output / file_count}")
#     print(f"avg_node: {avg_node / file_count}")
#     print(f"avg_lev: {avg_lev / file_count}")
#     print(f"aig_num: {aig_num / file_count}")
#     print(f"file_count: {file_count}")
# else:
#     print("Warning: No valid stats found!")