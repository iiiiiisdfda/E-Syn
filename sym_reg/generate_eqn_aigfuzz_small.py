#!/usr/bin/env python3
"""
隨機生成 ABC EQN 格式的布林電路檔案，模擬 aigfuzz -s 的行為

基於 aigfuzz.c 和 aigfuzzlayers.c 的分析：
- depth: 2-10 (small mode)
- width: 10-20 (small mode)
- 使用分層結構生成電路
- 應用 closure 操作（and, or, merge, xor, cnf）
"""

import random
import argparse
from typing import List, Optional, Tuple


class AigfuzzSmallGenerator:
    """模擬 aigfuzz -s 的電路生成器"""
    
    def __init__(self, seed: Optional[int] = None):
        """
        初始化生成器
        
        Args:
            seed: 隨機種子（用於可重現性）
        """
        if seed is not None:
            random.seed(seed)
        self.rng = seed if seed is not None else random.randint(1, 2**31-1)
        random.seed(self.rng)
    
    def aigfuzz_pick(self, from_val: int, to_val: int) -> int:
        """
        模擬 aigfuzz_pick 函數的隨機數生成
        
        Args:
            from_val: 最小值
            to_val: 最大值
            
        Returns:
            隨機數
        """
        assert from_val <= to_val
        return random.randint(from_val, to_val)
    
    def aigfuzz_oneoutof(self, to: int) -> bool:
        """
        模擬 aigfuzz_oneoutof 函數
        
        Args:
            to: 分母
            
        Returns:
            是否為真（1/to 的機率）
        """
        assert to > 0
        return self.aigfuzz_pick(1, to) == 1
    
    def generate_layer_structure(self, small: bool = False, medium: bool = False, large: bool = False, extra_large: bool = False, combinational: bool = True) -> Tuple[List[dict], int, int]:
        """
        生成分層電路結構（模擬 aigfuzz_layers）
        
        Args:
            small: 是否為小電路模式 (-s)
            medium: 是否為中等電路模式 (-m)
            large: 是否為大電路模式 (-l)
            extra_large: 是否為超大電路模式 (-xl)
            combinational: 是否為組合邏輯（無 latch）
            
        Returns:
            (layers, total_inputs, total_outputs)
        """
        # 根據模式設定 depth 和 width
        if small:
            # -s: depth = 2-10, width = 10-20
            depth = self.aigfuzz_pick(2, 10)
            width = self.aigfuzz_pick(10, 20)
        elif medium:
            # -m: depth = 10-50, width = 20-50 (中等規模)
            depth = self.aigfuzz_pick(10, 20)
            width = self.aigfuzz_pick(20, 30)
            width = 35 - depth
        elif large:
            # -l: depth = 50-200, width = 50-200
            depth = self.aigfuzz_pick(50, 200)
            width = self.aigfuzz_pick(50, 200)
        elif extra_large:
            # -xl: depth = 200-500, width = 200-500
            depth = self.aigfuzz_pick(200, 300)
            width = self.aigfuzz_pick(200, 300)
        else:
            # 默認: depth = 2-200, width = 10-200
            depth = self.aigfuzz_pick(2, 200)
            width = self.aigfuzz_pick(10, 200)
        
        input_fraction = self.aigfuzz_pick(0, 20)  # 0-20%
        latch_fraction = 0 if combinational else self.aigfuzz_pick(0, 100)
        lower_fraction = 10 * self.aigfuzz_pick(0, 5)  # 0-50% in steps of 10
        monotonicity = self.aigfuzz_pick(0, 2) - 1  # -1, 0, or 1
        
        layers = []
        total_inputs = 0
        total_outputs = 0
        
        # 生成每一層
        for layer_idx in range(depth):
            # 決定該層的節點數 M
            if monotonicity < 0 and layer_idx == 1:
                M = self.aigfuzz_pick(layers[0]['M'], 2 * layers[0]['M'])
            else:
                M = self.aigfuzz_pick(10, 10 + width - 1)
                if monotonicity > 0 and layer_idx > 0 and M < layers[layer_idx-1]['M']:
                    M = layers[layer_idx-1]['M']
                elif monotonicity < 0 and layer_idx > 1 and M > layers[layer_idx-1]['M']:
                    M = layers[layer_idx-1]['M']
            
            # 決定輸入數 I
            if layer_idx == 0:
                I = M
            else:
                if input_fraction > 0:
                    I = self.aigfuzz_pick(0, (input_fraction * M) // 100)
                else:
                    I = 0
            
            # 決定 latch 數 L
            if latch_fraction > 0:
                L = self.aigfuzz_pick(0, (latch_fraction * I) // 100)
                I -= L
            else:
                L = 0
            
            # AND 門數 A
            A = M - I - L
            
            layer = {
                'M': M,
                'I': I,
                'L': L,
                'A': A,
                'O': M,  # 初始時所有節點都是輸出候選
                'nodes': [],  # 存儲節點信息
                'unused': list(range(M))  # 未使用的節點索引
            }
            
            layers.append(layer)
            total_inputs += I
        
        # 為每一層生成節點
        input_counter = 0
        node_counter = 0
        for layer_idx, layer in enumerate(layers):
            layer_nodes = []
            
            # 生成輸入節點（輸入編號從0開始連續）
            for i in range(layer['I']):
                layer_nodes.append({
                    'type': 'input',
                    'name': f'pi{input_counter:02d}',
                    'index': i
                })
                input_counter += 1
            
            # 生成 latch 節點（在組合邏輯中跳過）
            for i in range(layer['L']):
                node_counter += 1
                layer_nodes.append({
                    'type': 'latch',
                    'name': f'latch{node_counter-1}',
                    'index': layer['I'] + i
                })
            
            # 生成 AND 門節點
            for i in range(layer['A']):
                node_counter += 1
                layer_nodes.append({
                    'type': 'and',
                    'name': f'new_n{node_counter-1}_',
                    'index': layer['I'] + layer['L'] + i,
                    'inputs': []  # 將在後面填充
                })
            
            layer['nodes'] = layer_nodes
        
        # 為 AND 門生成連接（連接到前一層）
        for layer_idx in range(1, depth):
            layer = layers[layer_idx]
            prev_layer = layers[layer_idx - 1]
            
            for node in layer['nodes']:
                if node['type'] == 'and':
                    # 為 AND 門選擇兩個輸入
                    inputs = []
                    for k in range(2):
                        # 決定從哪一層選擇輸入
                        m_idx = layer_idx - 1
                        if k == 1:
                            # 有 lower_fraction 的機率選擇更早的層
                            while m_idx > 0 and self.aigfuzz_pick(1, 100) <= lower_fraction:
                                m_idx -= 1
                        
                        m = layers[m_idx]
                        
                        # 從未使用的節點中選擇，或從所有節點中選擇
                        if m['O'] > 0:
                            pos = self.aigfuzz_pick(0, m['O'] - 1)
                            node_idx = m['unused'][pos]
                            m['unused'][pos] = m['unused'][m['O'] - 1]
                            m['O'] -= 1
                        else:
                            node_idx = self.aigfuzz_pick(0, m['M'] - 1)
                        
                        # 50% 機率取反
                        negated = self.aigfuzz_oneoutof(2)
                        inputs.append((m_idx, node_idx, negated))
                    
                    node['inputs'] = inputs
        
        # 計算總輸出數（所有層的未使用節點）
        for layer in layers:
            total_outputs += layer['O']
        
        return layers, total_inputs, total_outputs
    
    def generate_closure(self, outputs: List[str], available_vars: List[str], node_definitions: dict) -> Tuple[List[str], dict]:
        """
        應用 closure 操作（模擬 aigfuzz 的 closure 函數）
        
        Args:
            outputs: 當前輸出列表（節點名稱）
            available_vars: 可用的變數列表
            node_definitions: 節點定義字典
            
        Returns:
            (新的輸出列表, 更新的節點定義字典)
        """
        if not outputs:
            return outputs, node_definitions
        
        closure_type = self.aigfuzz_pick(0, 99)
        next_node_id = len(available_vars)
        
        if closure_type < 10:
            # andclosure: 使用邏輯運算符連接輸出直到只剩 R 個
            R = self.aigfuzz_pick(1, len(outputs))
            while len(outputs) > R:
                # 隨機選擇兩個輸出
                idx1 = self.aigfuzz_pick(0, len(outputs) - 1)
                out1 = outputs.pop(idx1)
                idx2 = self.aigfuzz_pick(0, len(outputs) - 1)
                out2 = outputs.pop(idx2)
                
                # 50% 機率取反，但確保表達式格式正確
                expr1 = f"!{out1}" if self.aigfuzz_oneoutof(2) else out1
                expr2 = f"!{out2}" if self.aigfuzz_oneoutof(2) else out2
                
                # 隨機選擇運算符：主要使用 AND，但也可能使用 OR 或 XOR
                op_choice = self.aigfuzz_pick(0, 99)
                if op_choice < 70:
                    op = "*"
                elif op_choice < 90:
                    op = "+"
                else:
                    op = "^"
                
                new_node = f"new_n{next_node_id}_"
                next_node_id += 1
                available_vars.append(new_node)
                # 確保表達式格式正確：變數之間有運算符
                node_definitions[new_node] = f"{expr1} {op} {expr2}"
                outputs.append(new_node)
        
        elif closure_type < 20:
            # orclosure: 使用 OR (+) 連接輸出
            R = self.aigfuzz_pick(1, len(outputs))
            while len(outputs) > R:
                idx1 = self.aigfuzz_pick(0, len(outputs) - 1)
                out1 = outputs.pop(idx1)
                idx2 = self.aigfuzz_pick(0, len(outputs) - 1)
                out2 = outputs.pop(idx2)
                
                # 50% 機率取反
                expr1 = f"!{out1}" if self.aigfuzz_oneoutof(2) else out1
                expr2 = f"!{out2}" if self.aigfuzz_oneoutof(2) else out2
                
                # 主要使用 OR (+)，但也可能使用其他運算符
                op_choice = self.aigfuzz_pick(0, 99)
                if op_choice < 70:
                    op = "+"
                elif op_choice < 90:
                    op = "*"
                else:
                    op = "^"
                
                new_node = f"new_n{next_node_id}_"
                next_node_id += 1
                available_vars.append(new_node)
                node_definitions[new_node] = f"{expr1} {op} {expr2}"
                outputs.append(new_node)
        
        elif closure_type < 50:
            # mergeclosure: 使用各種邏輯運算符連接，允許取反
            R = self.aigfuzz_pick(1, len(outputs))
            while len(outputs) > R:
                idx1 = self.aigfuzz_pick(0, len(outputs) - 1)
                out1 = outputs.pop(idx1)
                idx2 = self.aigfuzz_pick(0, len(outputs) - 1)
                out2 = outputs.pop(idx2)
                
                expr1 = f"!{out1}" if self.aigfuzz_oneoutof(2) else out1
                expr2 = f"!{out2}" if self.aigfuzz_oneoutof(2) else out2
                
                # 隨機選擇運算符：AND, OR, XOR 各有一定機率
                op_choice = self.aigfuzz_pick(0, 99)
                if op_choice < 40:
                    op = "*"
                elif op_choice < 75:
                    op = "+"
                else:
                    op = "^"
                
                new_node = f"new_n{next_node_id}_"
                next_node_id += 1
                available_vars.append(new_node)
                node_definitions[new_node] = f"{expr1} {op} {expr2}"
                outputs.append(new_node)
        
        elif closure_type < 80:
            # xorclosure: 使用 XOR 連接
            R = self.aigfuzz_pick(1, len(outputs))
            while len(outputs) > R:
                idx1 = self.aigfuzz_pick(0, len(outputs) - 1)
                out1 = outputs.pop(idx1)
                idx2 = self.aigfuzz_pick(0, len(outputs) - 1)
                out2 = outputs.pop(idx2)
                
                expr1 = f"!{out1}" if self.aigfuzz_oneoutof(2) else out1
                expr2 = f"!{out2}" if self.aigfuzz_oneoutof(2) else out2
                
                # XOR: (expr1 ^ expr2) = (!expr1 * expr2) + (expr1 * !expr2)
                # 簡化為使用 ^ 運算符
                new_node = f"new_n{next_node_id}_"
                next_node_id += 1
                available_vars.append(new_node)
                node_definitions[new_node] = f"{expr1} ^ {expr2}"
                outputs.append(new_node)
        
        else:
            # cnfclosure: 生成 CNF 風格的結構
            ratio = self.aigfuzz_pick(400, 450)  # 400-450%
            C = (ratio * len(outputs)) // 100
            ternary_only = self.aigfuzz_oneoutof(2)
            
            new_outputs = []
            for i in range(C):
                clause_parts = []
                num_lits = 2 if ternary_only else (2 if self.aigfuzz_oneoutof(3) else 3)
                
                for j in range(num_lits):
                    if outputs:
                        idx = self.aigfuzz_pick(0, len(outputs) - 1)
                        lit = outputs[idx]
                        if self.aigfuzz_oneoutof(2):
                            lit = f"!{lit}" if not lit.startswith('!') else lit[1:]
                    else:
                        lit = available_vars[self.aigfuzz_pick(0, len(available_vars) - 1)]
                        if self.aigfuzz_oneoutof(2):
                            lit = f"!{lit}" if not lit.startswith('!') else lit[1:]
                    
                    clause_parts.append(lit)
                
                # CNF clause: !(lit1 + lit2 + ...) = !lit1 * !lit2 * ...
                # 但這裡我們生成的是 clause，然後取反
                clause_expr = " + ".join(clause_parts)
                if len(clause_parts) > 1:
                    clause_expr = f"({clause_expr})"
                
                new_node = f"new_n{next_node_id}_"
                next_node_id += 1
                available_vars.append(new_node)
                node_definitions[new_node] = f"!{clause_expr}"
                new_outputs.append(new_node)
            
            # 對新輸出應用 closure（使用各種運算符）
            outputs = new_outputs
            R = self.aigfuzz_pick(1, len(outputs))
            while len(outputs) > R:
                idx1 = self.aigfuzz_pick(0, len(outputs) - 1)
                out1 = outputs.pop(idx1)
                idx2 = self.aigfuzz_pick(0, len(outputs) - 1)
                out2 = outputs.pop(idx2)
                
                # 隨機選擇運算符
                op_choice = self.aigfuzz_pick(0, 99)
                if op_choice < 50:
                    op = "*"
                elif op_choice < 85:
                    op = "+"
                else:
                    op = "^"
                
                new_node = f"new_n{next_node_id}_"
                next_node_id += 1
                available_vars.append(new_node)
                node_definitions[new_node] = f"{out1} {op} {out2}"
                outputs.append(new_node)
        
        return outputs, node_definitions
    
    def get_node_name(self, layer_idx: int, node_idx: int, node_type: str, node_counter: int) -> str:
        """
        獲取節點名稱
        
        Args:
            layer_idx: 層索引
            node_idx: 節點在層中的索引
            node_type: 節點類型
            node_counter: 全局節點計數器
            
        Returns:
            節點名稱
        """
        if node_type == 'input':
            return f'pi{node_counter:02d}'
        elif node_type == 'latch':
            return f'latch{node_counter}'
        else:
            return f'new_n{node_counter}_'
    
    def generate_eqn_file(
        self,
        output_file: str,
        min_nodes: int = 20,
        max_nodes: int = 290,
        max_depth: int = 3,
        small: bool = False,
        medium: bool = False,
        large: bool = False,
        extra_large: bool = False
    ):
        """
        生成完整的 EQN 檔案
        
        Args:
            output_file: 輸出檔案路徑
            min_nodes: 最小節點數
            max_nodes: 最大節點數
            max_depth: 表達式最大深度（用於 closure 操作）
            small: 是否為小電路模式 (-s)
            medium: 是否為中等電路模式 (-m)
            large: 是否為大電路模式 (-l)
            extra_large: 是否為超大電路模式 (-xl)
        """
        # 生成分層結構
        layers, total_inputs, total_outputs = self.generate_layer_structure(small=small, medium=medium, large=large, extra_large=extra_large, combinational=True)
        
        # 收集所有輸入變數
        input_vars = []
        all_nodes = []  # 所有節點（輸入 + 內部節點）
        node_definitions = {}  # 節點定義字典
        
        # 處理每一層
        for layer_idx, layer in enumerate(layers):
            for node in layer['nodes']:
                if node['type'] == 'input':
                    input_vars.append(node['name'])
                    all_nodes.append(node['name'])
                elif node['type'] == 'and':
                    all_nodes.append(node['name'])
                    # 生成邏輯門的表達式（隨機選擇運算符類型）
                    inputs = node['inputs']
                    if len(inputs) == 2:
                        # 獲取輸入節點名稱
                        prev_layer1 = layers[inputs[0][0]]
                        node_idx1 = inputs[0][1]
                        input1_name = prev_layer1['nodes'][node_idx1]['name']
                        neg1 = inputs[0][2]
                        
                        prev_layer2 = layers[inputs[1][0]]
                        node_idx2 = inputs[1][1]
                        input2_name = prev_layer2['nodes'][node_idx2]['name']
                        neg2 = inputs[1][2]
                        
                        # 應用取反
                        if neg1:
                            input1_name = f"!{input1_name}" if not input1_name.startswith('!') else input1_name[1:]
                        if neg2:
                            input2_name = f"!{input2_name}" if not input2_name.startswith('!') else input2_name[1:]
                        
                        # 隨機選擇運算符類型：* (AND), + (OR), ^ (XOR)
                        op_type = self.aigfuzz_pick(0, 99)
                        if op_type < 50:
                            # 50% 機率使用 AND (*)
                            op = "*"
                        elif op_type < 85:
                            # 35% 機率使用 OR (+)
                            op = "+"
                        else:
                            # 15% 機率使用 XOR (^)
                            op = "^"
                        
                        expr = f"{input1_name} {op} {input2_name}"
                        node_definitions[node['name']] = expr
        
        # 收集輸出候選（未使用的節點）
        output_candidates = []
        for layer in layers:
            for unused_idx in layer['unused'][:layer['O']]:
                if unused_idx < len(layer['nodes']):
                    node = layer['nodes'][unused_idx]
                    output_candidates.append(node['name'])
        
        # 如果沒有輸出候選，從所有節點中選擇
        if not output_candidates:
            output_candidates = [n for n in all_nodes if n not in input_vars]
        
        # 應用 closure 操作
        final_outputs, node_definitions = self.generate_closure(output_candidates.copy(), all_nodes, node_definitions)
        
        # 將 closure 創建的新節點添加到 all_nodes
        for new_node in node_definitions:
            if new_node not in all_nodes and new_node not in input_vars:
                all_nodes.append(new_node)
        
        # 如果 closure 後沒有輸出，從候選中隨機選擇
        if not final_outputs:
            num_outputs = self.aigfuzz_pick(1, min(10, len(output_candidates)))
            final_outputs = random.sample(output_candidates, num_outputs)
        
        # 生成輸出變數名稱
        output_vars = [f"po{i:02d}" for i in range(len(final_outputs))]
        
        # 生成檔案內容
        lines = []
        
        # 生成 INORDER
        lines.append(f"INORDER = {' '.join(input_vars)};")
        
        # 生成 OUTORDER
        lines.append(f"OUTORDER = {' '.join(output_vars)};")
        lines.append("")
        
        # 生成內部節點定義（按順序）
        defined_nodes = set(input_vars)
        remaining_definitions = node_definitions.copy()
        
        # 拓撲排序：確保節點在被使用前已定義
        max_iterations = len(remaining_definitions) * 3  # 增加迭代次數
        iteration = 0
        while remaining_definitions and iteration < max_iterations:
            iteration += 1
            progress = False
            for node_name, expr in list(remaining_definitions.items()):
                # 檢查表達式中使用的所有變數是否已定義
                import re
                # 提取所有變數名（處理否定符）
                # 匹配模式：piXX, new_nXX_, latchXX，可能前面有 !
                used_vars = re.findall(r'!?(pi\d+|new_n\d+_|latch\d+)', expr)
                # 移除否定符來檢查基礎變數
                base_vars = [v.lstrip('!') for v in used_vars]
                can_define = all(var in defined_nodes for var in base_vars)
                
                if can_define:
                    # 確保表達式格式正確
                    # 移除多餘空格，確保運算符周圍有空格
                    expr = re.sub(r'\s+', ' ', expr).strip()
                    expr = re.sub(r'\s*\*\s*', ' * ', expr)
                    expr = re.sub(r'\s+\+\s+', ' + ', expr)
                    expr = re.sub(r'\s+\^\s+', ' ^ ', expr)
                    expr = re.sub(r'!\s+', '!', expr)  # 否定符緊貼變數
                    lines.append(f"{node_name} = {expr};")
                    defined_nodes.add(node_name)
                    del remaining_definitions[node_name]
                    progress = True
            
            if not progress:
                # 如果無法進展，強制定義剩餘節點（使用簡單表達式）
                # 但優先使用已定義的節點
                for node_name, expr in list(remaining_definitions.items()):
                    # 嘗試使用表達式中已定義的變數
                    import re
                    used_vars = re.findall(r'!?(pi\d+|new_n\d+_|latch\d+)', expr)
                    base_vars = [v.lstrip('!') for v in used_vars]
                    defined_base_vars = [v for v in base_vars if v in defined_nodes]
                    
                    if defined_base_vars:
                        # 使用第一個已定義的變數
                        backup_expr = defined_base_vars[0]
                    else:
                        # 使用第一個輸入作為備用
                        backup_expr = input_vars[0] if input_vars else "0"
                    lines.append(f"{node_name} = {backup_expr};")
                    defined_nodes.add(node_name)
                    del remaining_definitions[node_name]
                break
        
        # 生成輸出節點
        # 重要：輸出節點必須直接引用已定義的節點，不能使用複雜表達式
        for i, output_var in enumerate(output_vars):
            if i < len(final_outputs):
                output_expr = final_outputs[i]
                # 確保輸出表達式中的變數都已定義
                import re
                # 提取基礎變數名（移除否定符）
                used_vars = re.findall(r'!?(pi\d+|new_n\d+_|latch\d+)', output_expr)
                base_vars = [v.lstrip('!') for v in used_vars]
                
                # 檢查所有變數是否已定義
                if all(var in defined_nodes for var in base_vars):
                    # 如果表達式只是一個簡單的變數引用，直接使用
                    # 否則簡化為只使用第一個變數
                    if len(base_vars) == 1 and output_expr == base_vars[0]:
                        lines.append(f"{output_var} = {output_expr};")
                    elif len(base_vars) == 1 and output_expr.startswith('!'):
                        lines.append(f"{output_var} = {output_expr};")
                    else:
                        # 複雜表達式，簡化為第一個變數
                        lines.append(f"{output_var} = {base_vars[0]};")
                else:
                    # 使用已定義的節點
                    available = [v for v in defined_nodes if v not in input_vars]
                    if available:
                        lines.append(f"{output_var} = {random.choice(available)};")
                    else:
                        lines.append(f"{output_var} = {input_vars[0] if input_vars else '0'};")
            else:
                # 如果輸出數不足，使用已定義的節點
                available = [v for v in defined_nodes if v not in input_vars]
                if available:
                    lines.append(f"{output_var} = {random.choice(available)};")
                else:
                    lines.append(f"{output_var} = {input_vars[0] if input_vars else '0'};")
        
        # 寫入檔案
        with open(output_file, 'w') as f:
            f.write('\n'.join(lines))
        
        # print(f"Generated EQN file: {output_file}")
        # print(f"  Inputs: {len(input_vars)}")
        # print(f"  Outputs: {len(output_vars)}")
        # print(f"  Internal nodes: {len(all_nodes) - len(input_vars)}")
        # print(f"  Layers: {len(layers)}")


def main():
    parser = argparse.ArgumentParser(
        description='隨機生成 ABC EQN 格式的布林電路檔案（模擬 aigfuzz -s/-m/-l）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  # 生成小規模電路 (aigfuzz -s)
  python generate_eqn_aigfuzz_small.py -o circuit.eqn -s
  
  # 生成中等規模電路 (-m)
  python generate_eqn_aigfuzz_small.py -o circuit.eqn -m
  
  # 生成大規模電路 (aigfuzz -l)
  python generate_eqn_aigfuzz_small.py -o circuit.eqn -l
  
  # 生成默認規模電路
  python generate_eqn_aigfuzz_small.py -o circuit.eqn
  
  # 指定節點範圍
  python generate_eqn_aigfuzz_small.py -o circuit.eqn --min-nodes 20 --max-nodes 290
        """
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help='輸出 EQN 檔案路徑'
    )
    
    parser.add_argument(
        '-s', '--small',
        action='store_true',
        help='生成小規模電路 (aigfuzz -s: depth 2-10, width 10-20)'
    )
    
    parser.add_argument(
        '-m', '--medium',
        action='store_true',
        help='生成中等規模電路 (-m: depth 10-50, width 20-50)'
    )
    
    parser.add_argument(
        '-l', '--large',
        action='store_true',
        help='生成大規模電路 (aigfuzz -l: depth 50-200, width 50-200)'
    )
    
    parser.add_argument(
        '-xl', '--extra-large',
        action='store_true',
        help='生成超大規模電路 (aigfuzz -xl: depth 200-300, width 200-300)'
    )
    
    parser.add_argument(
        '--min-nodes',
        type=int,
        default=20,
        help='最小節點數 (預設: 20)'
    )
    
    parser.add_argument(
        '--max-nodes',
        type=int,
        default=290,
        help='最大節點數 (預設: 290)'
    )
    
    parser.add_argument(
        '--max-depth',
        type=int,
        default=3,
        help='表達式最大深度 (預設: 3)'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        default=None,
        help='隨機種子（用於可重現性）'
    )
    
    args = parser.parse_args()
    
    # 檢查參數衝突
    size_flags = sum([args.small, args.medium, args.large, args.extra_large])
    if size_flags > 1:
        parser.error("不能同時指定多個規模參數 (-s, -m, -l, -xl)")
    
    # 創建生成器
    generator = AigfuzzSmallGenerator(seed=args.seed)
    
    # 生成檔案
    generator.generate_eqn_file(
        output_file=args.output,
        min_nodes=args.min_nodes,
        max_nodes=args.max_nodes,
        max_depth=args.max_depth,
        small=args.small,
        medium=args.medium,
        large=args.large,
        extra_large=args.extra_large
    )


if __name__ == '__main__':
    main()

