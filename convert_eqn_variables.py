#!/usr/bin/env python3
"""
转换 EQN 文件中的变量名：
- INORDER 中的变量转换为 pi00, pi01, pi02, ...
- OUTORDER 中的变量转换为 po0, po1, po2, ...
"""

import re
import sys
import os

def convert_eqn_file(input_file, output_file=None):
    """
    转换 EQN 文件中的变量名
    
    Args:
        input_file: 输入的 EQN 文件路径
        output_file: 输出的 EQN 文件路径（如果为 None，则覆盖原文件）
    """
    if output_file is None:
        output_file = input_file
    
    # 读取文件
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # 解析 INORDER 和 OUTORDER（支持多行）
    inorder_vars = []
    outorder_vars = []
    inorder_line_indices = []  # 记录所有相关行的索引
    outorder_line_indices = []
    
    i = 0
    while i < len(lines):
        line_stripped = lines[i].strip()
        if line_stripped.startswith('INORDER'):
            # 解析 INORDER = var1 var2 var3 ...;（可能跨多行）
            inorder_line_indices.append(i)
            # 提取第一行的变量
            match = re.match(r'INORDER\s*=\s*(.+?)(;|$)', line_stripped)
            if match:
                var_part = match.group(1).strip()
                if var_part:
                    inorder_vars.extend(var_part.split())
            
            # 如果第一行没有分号，继续读取后续行
            if ';' not in line_stripped:
                i += 1
                while i < len(lines) and ';' not in lines[i]:
                    line_stripped = lines[i].strip()
                    if line_stripped:
                        inorder_line_indices.append(i)
                        inorder_vars.extend(line_stripped.split())
                    i += 1
                # 处理包含分号的最后一行
                if i < len(lines):
                    line_stripped = lines[i].strip()
                    inorder_line_indices.append(i)
                    # 提取分号前的变量
                    var_part = line_stripped.rstrip(';').strip()
                    if var_part:
                        inorder_vars.extend(var_part.split())
        elif line_stripped.startswith('OUTORDER'):
            # 解析 OUTORDER = var1 var2 var3 ...;（可能跨多行）
            outorder_line_indices.append(i)
            # 提取第一行的变量
            match = re.match(r'OUTORDER\s*=\s*(.+?)(;|$)', line_stripped)
            if match:
                var_part = match.group(1).strip()
                if var_part:
                    outorder_vars.extend(var_part.split())
            
            # 如果第一行没有分号，继续读取后续行
            if ';' not in line_stripped:
                i += 1
                while i < len(lines) and ';' not in lines[i]:
                    line_stripped = lines[i].strip()
                    if line_stripped:
                        outorder_line_indices.append(i)
                        outorder_vars.extend(line_stripped.split())
                    i += 1
                # 处理包含分号的最后一行
                if i < len(lines):
                    line_stripped = lines[i].strip()
                    outorder_line_indices.append(i)
                    # 提取分号前的变量
                    var_part = line_stripped.rstrip(';').strip()
                    if var_part:
                        outorder_vars.extend(var_part.split())
        i += 1
    
    if not inorder_vars:
        print("Warning: INORDER not found in file")
    if not outorder_vars:
        print("Warning: OUTORDER not found in file")
    
    # 创建变量映射
    var_mapping = {}
    
    # INORDER -> pi00, pi01, pi02, ...
    for idx, var in enumerate(inorder_vars):
        new_name = f"pi{idx:02d}"
        var_mapping[var] = new_name
    
    # OUTORDER -> po0, po1, po2, ...
    for idx, var in enumerate(outorder_vars):
        new_name = f"po{idx}"
        var_mapping[var] = new_name
    
    print(f"Found {len(inorder_vars)} input variables")
    print(f"Found {len(outorder_vars)} output variables")
    print(f"Total variables to convert: {len(var_mapping)}")
    
    # 预编译正则表达式以提高性能
    compiled_patterns = []
    sorted_vars = sorted(var_mapping.items(), key=lambda x: len(x[0]), reverse=True)
    for old_var, new_var in sorted_vars:
        if '[' in old_var:
            # 带索引的变量名
            pattern = re.compile(re.escape(old_var) + r'(?=\s|;|\)|\(|\*|\+|\&|\^|!|=|$)')
        else:
            # 简单变量名
            pattern = re.compile(r'\b' + re.escape(old_var) + r'(?=\s|\[|;|\)|\(|\*|\+|\&|\^|!|=|$)')
        compiled_patterns.append((pattern, new_var))
    
    # 转换文件内容
    new_lines = []
    for i, line in enumerate(lines):
        if i in inorder_line_indices:
            # 更新 INORDER 行（第一行），所有变量放在一行
            if i == inorder_line_indices[0]:
                new_vars = [var_mapping.get(var, var) for var in inorder_vars]
                var_str = ' '.join(new_vars)
                new_lines.append(f"INORDER = {var_str};\n")
            else:
                # 跳过其他 INORDER 相关行（已经在第一行处理了）
                continue
        elif i in outorder_line_indices:
            # 更新 OUTORDER 行（第一行），所有变量放在一行
            if i == outorder_line_indices[0]:
                new_vars = [var_mapping.get(var, var) for var in outorder_vars]
                var_str = ' '.join(new_vars)
                new_lines.append(f"OUTORDER = {var_str};\n")
            else:
                # 跳过其他 OUTORDER 相关行（已经在第一行处理了）
                continue
        else:
            # 转换其他行中的变量名
            new_line = line
            # 使用预编译的正则表达式进行替换
            for pattern, new_var in compiled_patterns:
                new_line = pattern.sub(new_var, new_line)
            new_lines.append(new_line)
    
    # 写入输出文件
    with open(output_file, 'w') as f:
        f.writelines(new_lines)
    
    print(f"Conversion complete! Output written to: {output_file}")
    
    # 显示一些转换示例
    if var_mapping:
        print("\nVariable mapping examples:")
        for old_var, new_var in list(var_mapping.items())[:10]:
            print(f"  {old_var} -> {new_var}")
        if len(var_mapping) > 10:
            print(f"  ... and {len(var_mapping) - 10} more")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_eqn_variables.py <input_file> [output_file]")
        print("  If output_file is not specified, input_file will be overwritten")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)
    
    convert_eqn_file(input_file, output_file)

if __name__ == "__main__":
    main()

