import os
import sys
import pandas as pd
import re
from tqdm import tqdm

# MIG 数据收集脚本
# 流程：AIG -> (转换为 MIG) -> LUT -> 物理信息

# 设置工具路径
ABC_PATH = os.path.abspath("../abc/abc")
AIGFUZZ_PATH = None

# 查找 aigfuzz
aigfuzz_dir = os.path.abspath("aiger_tool_util")
aigfuzz_bin = os.path.join(aigfuzz_dir, "aigfuzz")

if os.path.exists(aigfuzz_bin):
    AIGFUZZ_PATH = aigfuzz_bin
elif os.path.exists("../sym_reg/aiger_tool_util/aigfuzz"):
    AIGFUZZ_PATH = os.path.abspath("../sym_reg/aiger_tool_util/aigfuzz")
else:
    # 尝试编译 aigfuzz
    aigfuzz_src = os.path.join(aigfuzz_dir, "aigfuzz.c")
    if os.path.exists(aigfuzz_src):
        print(f"Compiling aigfuzz from {aigfuzz_src}...")
        ret = os.system(f"cd {aigfuzz_dir} && gcc aigfuzz.c aiger.c aigfuzzlayers.c -o aigfuzz 2>&1")
        if ret == 0 and os.path.exists(aigfuzz_bin):
            AIGFUZZ_PATH = aigfuzz_bin
            print(f"Successfully compiled aigfuzz at {AIGFUZZ_PATH}")
        else:
            print(f"Warning: Failed to compile aigfuzz. Error code: {ret}")

# 检查工具是否存在
if not os.path.exists(ABC_PATH):
    print(f"Error: ABC not found at {ABC_PATH}")
    print(f"Please ensure ABC is compiled. Try: cd ../abc && make")
    sys.exit(1)

if AIGFUZZ_PATH is None or not os.path.exists(AIGFUZZ_PATH):
    print(f"Warning: aigfuzz not found at expected locations.")
    print(f"Trying to use system aigfuzz from PATH...")
    # 检查系统 PATH 中是否有 aigfuzz
    import shutil
    if shutil.which("aigfuzz"):
        AIGFUZZ_PATH = "aigfuzz"
        print(f"Found aigfuzz in system PATH")
    else:
        print(f"Error: aigfuzz not found. Please:")
        print(f"  1. Install aigfuzz system-wide, or")
        print(f"  2. Compile it manually:")
        print(f"     cd {os.path.abspath('../sym_reg/aiger_tool_util')}")
        print(f"     gcc aigfuzz.c aiger.c aigfuzzlayers.c -o aigfuzz")
        sys.exit(1)

def run_aigfuzz(file_count):
    """生成随机 AIG 电路"""
    if not os.path.exists("migfuzz"): 
        os.mkdir("migfuzz")
    for i in tqdm(range(file_count), desc='Run circuit generator'):
        # 使用完整路径或相对路径
        aigfuzz_cmd = AIGFUZZ_PATH if AIGFUZZ_PATH != "aigfuzz" else "aigfuzz"
        abc_cmd = ABC_PATH
        
        ret1 = os.system(f"{aigfuzz_cmd} -c -s > migfuzz/simple_circuit_{i}.aig 2>&1")
        if ret1 != 0:
            print(f"Warning: aigfuzz failed for circuit {i}")
            continue
            
        ret2 = os.system(
            f"{abc_cmd} -c \"read_aiger migfuzz/simple_circuit_{i}.aig; trim ; write_aiger migfuzz/simple_circuit_{i}.aig\" 2>&1")
        if ret2 != 0:
            print(f"Warning: abc failed for circuit {i}")


def convert_to_mig(file_count):
    """使用 ABC 将 AIG 转换为 MIG（如果支持）"""
    # ABC 的 if -g 命令可以将 AIG 转换为 MIG
    for i in tqdm(range(file_count), desc='Converting AIG to MIG'):
        if not os.path.exists(f"migfuzz/simple_circuit_{i}.aig"):
            continue
            
        # 使用 ABC 的 if -g 命令转换为 MIG
        # 注意：这会将 AIG 转换为 MIG 格式
        os.system(
            f"{ABC_PATH} -c \"read_aiger migfuzz/simple_circuit_{i}.aig; if -g; write_aiger migfuzz/simple_circuit_{i}_mig.aig\" 2>/dev/null")
        
        # 如果转换成功，使用 MIG 文件；否则继续使用原始 AIG
        if not os.path.exists(f"migfuzz/simple_circuit_{i}_mig.aig"):
            # 如果转换失败，复制原始文件
            import shutil
            if os.path.exists(f"migfuzz/simple_circuit_{i}.aig"):
                shutil.copy(f"migfuzz/simple_circuit_{i}.aig", f"migfuzz/simple_circuit_{i}_mig.aig")


def process_mig_circuits(file_count):
    """处理 MIG 电路，提取特征（操作符统计）"""
    sys.path.append("..")
    for i in tqdm(range(file_count), desc='Processing MIG circuits for analyzer'):
        print(f"processing No.{i} circuit")
        
        # 将 AIG/MIG 转换为 eqn 格式
        eqn_file = f"migfuzz/simple_circuit_{i}.eqn"
        processed_eqn = f"migfuzz/simple_circuit_{i}_processed.eqn"
        
        # 优先使用 MIG 文件
        input_aig = f"migfuzz/simple_circuit_{i}_mig.aig"
        if not os.path.exists(input_aig):
            input_aig = f"migfuzz/simple_circuit_{i}.aig"
        
        if not os.path.exists(eqn_file):
            if os.path.exists(input_aig):
                os.system(
                    f"{ABC_PATH} -c \"read_aiger {input_aig}; write_eqn {eqn_file}\" 2>&1")
            else:
                print(f"Warning: {input_aig} not found, skipping circuit {i}")
                continue
        
        # 处理 eqn（如果需要）
        if not os.path.exists(processed_eqn):
            try:
                from CircuitParser import CircuitParser
                parser = CircuitParser(eqn_file, processed_eqn)
                parser.process()
            except Exception as e:
                print(f"Warning: CircuitParser failed, copying file: {e}")
                import shutil
                shutil.copy(eqn_file, processed_eqn)
        
        # 转换为 s-expression
        sexpr_file = f"migfuzz/simple_circuit_{i}.sexpr"
        if not os.path.exists(sexpr_file):
            try:
                import run
                with open(processed_eqn, "r") as myfile:
                    data = myfile.readlines()
                _ = run.conver_to_sexpr(
                    data, multiple_output=True, output_file_path=sexpr_file)
            except Exception as e:
                print(f"Warning: Failed to convert to sexpr for circuit {i}: {e}")
                continue
        
        # 使用 analyzer 提取特征
        data_file = f"migfuzz/simple_circuit_{i}.data"
        if os.path.exists(sexpr_file):
            analyzer_path = "../analyzer/target/release/analyzer"
            if not os.path.exists(analyzer_path):
                analyzer_path = "analyzer/target/release/analyzer"
            
            if os.path.exists(analyzer_path):
                # analyzer 需要两个参数：输入文件和 dot 名称
                dot_name = f"simple_circuit_{i}"
                ret = os.system(
                    f"{analyzer_path} {sexpr_file} {dot_name} > {data_file} 2>&1")
                # 检查 analyzer 是否成功（返回码 0）
                if ret != 0:
                    print(f"Warning: analyzer failed for circuit {i} (exit code {ret})")
            else:
                print(f"Warning: analyzer not found at {analyzer_path}")


def convert_mig_to_lut_and_get_stats(file_count):
    """使用 ABC 将电路转换为 LUT 并获取物理信息"""
    for i in tqdm(range(file_count), desc='Converting to LUT and getting stats'):
        # 检查是否有编译好的 mig_to_lut 工具
        mig_to_lut_tool = "./mig_to_lut"
        input_aig = f"migfuzz/simple_circuit_{i}_mig.aig"
        if not os.path.exists(input_aig):
            input_aig = f"migfuzz/simple_circuit_{i}.aig"
        
        if os.path.exists(mig_to_lut_tool) and os.path.exists(input_aig):
            # 使用 mockturtle 工具
            output_file = f"migfuzz/simple_circuit_{i}.lut_stats"
            os.system(f"{mig_to_lut_tool} {input_aig} {output_file}")
        else:
            # 使用 ABC 的 LUT mapping（fallback）
            eqn_file = f"migfuzz/simple_circuit_{i}_processed.eqn"
            if not os.path.exists(eqn_file):
                # 从 AIG 转换为 eqn
                if os.path.exists(input_aig):
                    os.system(
                        f"{ABC_PATH} -c \"read_aiger {input_aig}; write_eqn {eqn_file}\" 2>&1")
                else:
                    continue
            
            # 使用 ABC 进行 LUT mapping 并获取统计信息
            stats_file = f"migfuzz/simple_circuit_{i}.lut_stats"
            
            if not os.path.exists(eqn_file):
                continue
                
            # 使用正确的 ABC 命令获取 area 和 delay（参考 data_collect.py）
            # 需要加载库、map、然后 stime 才能获取延迟
            lib_path = "../asap7_clean.lib"
            if not os.path.exists(lib_path):
                lib_path = "../../asap7_clean.lib"  # 尝试其他路径
            
            if os.path.exists(lib_path):
                # 使用完整的命令序列获取 area 和 delay
                os.system(
                    f"{ABC_PATH} -c \"read_eqn {eqn_file}; strash; dch -f; print_stats -p; read_lib {lib_path} ; map ; topo; upsize; dnsize; stime; \" > {stats_file} 2>&1")
            else:
                # 如果没有库文件，至少尝试获取基本统计
                os.system(
                    f"{ABC_PATH} -c \"read_eqn {eqn_file}; strash; print_stats; \" > {stats_file} 2>&1")


def parse_data(file_count):
    """解析数据并生成 CSV"""
    print("---------------------Final Step: Parsing Data---------------------")
    def parser(i):
        # 读取操作符统计
        data_file = f"migfuzz/simple_circuit_{i}.data"
        op_dict = {}
        if os.path.exists(data_file):
            with open(data_file, "r") as f:
                data = f.read().split('\n')
                for line in data:
                    if ':' in line:
                        parts = line.split(':')
                        if len(parts) == 2:
                            key = parts[0].strip()
                            try:
                                value = int(parts[1].strip())
                                op_dict[key] = value
                            except ValueError:
                                pass
        else:
            # 如果文件不存在，使用默认值
            op_dict = {'+': 0, '!': 0, '*': 0, '&': 0, 'ASTSize': 0, 'ASTDepth': 0}
        
        # 从 LUT mapping 结果中提取物理信息
        stats_file = f"migfuzz/simple_circuit_{i}.lut_stats"
        area = None
        delay = None
        depth = None
        power = 0.0
        
        if os.path.exists(stats_file):
            with open(stats_file, "r") as f:
                stats = f.read()
                
                # 解析 ABC 输出格式（参考 data_collect.py）
                # ABC 输出格式示例：
                # "area = 123.45"
                # "delay = 67.89"
                # "lev = 5"
                # "power = 12.34"
                
                # 解析 area（从 map 后的输出）
                area_match = re.search(r"Area\s*=\s*(\d+\.?\d*)", stats, re.I)
                if not area_match:
                    area_match = re.search(r"area\s*=\s*(\d+\.?\d*)", stats, re.I)
                if area_match:
                    area = float(area_match.group(1))
                
                # 解析 delay（从 stime 后的输出）
                delay_match = re.search(r"Delay\s*=\s*(\d+\.?\d*)", stats, re.I)
                if not delay_match:
                    delay_match = re.search(r"delay\s*=\s*(\d+\.?\d*)", stats, re.I)
                if delay_match:
                    delay = float(delay_match.group(1))
                
                # 解析 lev/depth
                depth_match = re.search(r"lev\s*=\s*(\d+)", stats, re.I)
                if depth_match:
                    depth = int(depth_match.group(1))
                
                # 解析 power
                power_match = re.search(r"power\s*=\s*(\d+\.?\d*)", stats, re.I)
                if power_match:
                    power = float(power_match.group(1))
        else:
            print(f"Warning: {stats_file} not found for circuit {i}")
        
        return {
            "power": power,
            "lev": depth if depth is not None else 0,
            "area": area if area is not None else 0,
            "delay": delay if delay is not None else 0,
            **op_dict
        }

    df = pd.DataFrame([parser(i) for i in range(file_count)])
    df = df.fillna(0)
    
    # 定义必需的列
    required_columns = ['+', '!', '*', '&', 'ASTSize', 'ASTDepth', 'lev', 'power', 'area', 'delay']
    
    # 确保所有必需的列都存在（如果不存在则设为 0）
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0
    
    # 移除无效数据（所有特征都是 0，且 area, delay, lev 都为 0 的行）
    # 至少需要有一些有效数据
    feature_sum = df['+'] + df['!'] + df['*'] + df['&'] + df['ASTSize']
    df = df[
        (feature_sum > 0) | 
        (df.area != 0) | 
        (df.delay != 0) | 
        (df.lev != 0)
    ]
    
    # MIG 的特征列可能不同，需要根据实际情况调整
    # 如果有 majority 门，可能需要添加 'M' 列
    columns = ['+', '!', '*', '&', 'ASTSize', 'ASTDepth', 'lev', 'power', 'area', 'delay']
    
    # 如果有多数门统计，添加 'M' 列
    if 'M' in df.columns:
        columns.insert(4, 'M')
    
    # 确保所有必需的列都存在
    for col in columns:
        if col not in df.columns:
            df[col] = 0
    
    df = df.reindex(columns=columns)
    df.to_csv("mig_circuit_analysis.csv", index=False)
    print(f"Saved {len(df)} rows to mig_circuit_analysis.csv")
    print(f"Columns: {df.columns.tolist()}")
    if len(df) > 0:
        print(f"Sample data:\n{df.head()}")
    else:
        print("Warning: No valid data rows found!")
    print(f"Sample data:\n{df.head()}")


if __name__ == "__main__":
    sys.path.append("..")
    file_count = 100  # 初始测试用较小数量，可以修改
    print(f"Starting MIG data collection for {file_count} circuits...")
    
    run_aigfuzz(file_count)
    convert_to_mig(file_count)
    process_mig_circuits(file_count)
    convert_mig_to_lut_and_get_stats(file_count)
    parse_data(file_count)
    
    print("MIG data collection completed!")
