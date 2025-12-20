#!/usr/bin/env python3
"""
EQN 格式電路特徵提取器

從 EQN 檔案中提取適合用於機器學習訓練的特徵

Usage (stored as csv) : python eqn_feature_extractor.py <eqn_file> -o <output_file> --format csv
"""

import re
from typing import Dict, List
from collections import defaultdict
import argparse


class EqnFeatureExtractor:
    """EQN 檔案特徵提取器"""
    
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.nodes = {}  # node_name -> expression
        self.dependencies = defaultdict(list)  # node -> [dependencies]
    
    def parse_eqn_file(self, filepath: str) -> None:
        """解析 EQN 檔案"""
        with open(filepath, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # 解析 INORDER
            if line.startswith('INORDER'):
                vars_str = line.split('=', 1)[1].rstrip(';').strip()
                self.inputs = vars_str.split()
                continue
            
            # 解析 OUTORDER
            if line.startswith('OUTORDER'):
                vars_str = line.split('=', 1)[1].rstrip(';').strip()
                self.outputs = vars_str.split()
                continue
            
            # 解析節點定義
            if '=' in line:
                parts = line.split('=', 1)
                if len(parts) == 2:
                    node_name = parts[0].strip()
                    expression = parts[1].rstrip(';').strip()
                    self.nodes[node_name] = expression
                    
                    # 提取依賴關係
                    deps = self._extract_dependencies(expression)
                    self.dependencies[node_name] = deps
    
    def _extract_dependencies(self, expression: str) -> List[str]:
        """從表達式中提取依賴的變數和節點"""
        # 移除運算符和括號
        tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expression)
        return list(set(tokens))
    
    def extract_structural_features(self) -> Dict[str, float]:
        """提取結構特徵"""
        features = {}
        
        features['num_inputs'] = len(self.inputs)
        features['num_outputs'] = len(self.outputs)
        # 計算內部節點數：總節點數減去輸出節點數
        # 注意：在 EQN 格式中，輸出節點通常也在 nodes 字典中
        outputs_in_nodes = sum(1 for out in self.outputs if out in self.nodes)
        features['num_internal_nodes'] = max(0, len(self.nodes) - outputs_in_nodes)
        features['total_nodes'] = len(self.inputs) + len(self.nodes)
        features['num_equations'] = len(self.nodes)
        
        # 計算邏輯深度
        max_depth = 0
        depth_sum = 0
        for output in self.outputs:
            depth = self._calculate_depth(output, set())
            max_depth = max(max_depth, depth)
            depth_sum += depth
        
        features['max_logic_depth'] = max_depth
        features['avg_logic_depth'] = depth_sum / len(self.outputs) if self.outputs else 0
        
        # 計算扇入扇出
        fanin_counts = []
        fanout = defaultdict(int)
        
        for node_name, expr in self.nodes.items():
            deps = self.dependencies[node_name]
            fanin_counts.append(len(deps))
            for dep in deps:
                fanout[dep] += 1
        
        features['avg_fanin'] = sum(fanin_counts) / len(fanin_counts) if fanin_counts else 0
        features['max_fanin'] = max(fanin_counts) if fanin_counts else 0
        features['avg_fanout'] = sum(fanout.values()) / len(fanout) if fanout else 0
        features['max_fanout'] = max(fanout.values()) if fanout else 0
        
        return features
    
    def _calculate_depth(self, node: str, visited: set) -> int:
        """計算節點的邏輯深度"""
        # 如果是輸入節點，深度為 0
        if node in self.inputs:
            return 0
        
        # 如果節點不在 nodes 中（可能是未定義的節點），返回 0
        if node not in self.nodes:
            return 0
        
        # 檢測循環依賴：如果節點已在訪問路徑中，返回 1（避免無限遞歸）
        if node in visited:
            return 1
        
        visited.add(node)
        deps = self.dependencies[node]
        if not deps:
            visited.remove(node)  # 回溯
            return 1
        
        max_dep_depth = 0
        for dep in deps:
            if dep in self.inputs:
                continue
            # 使用同一個 visited 集合以正確檢測循環
            dep_depth = self._calculate_depth(dep, visited)
            max_dep_depth = max(max_dep_depth, dep_depth)
        
        visited.remove(node)  # 回溯
        return max_dep_depth + 1
    
    def extract_syntactic_features(self) -> Dict[str, float]:
        """提取語法特徵"""
        features = {}
        
        all_expressions = ' '.join(self.nodes.values())
        
        # 運算符計數
        features['count_and'] = all_expressions.count('*')
        features['count_or'] = all_expressions.count('+')
        features['count_xor'] = all_expressions.count('^')
        features['count_not'] = all_expressions.count('!')
        features['total_operators'] = (
            features['count_and'] + 
            features['count_or'] + 
            features['count_xor'] + 
            features['count_not']
        )
        
        # 運算符比例
        if features['total_operators'] > 0:
            features['ratio_and'] = features['count_and'] / features['total_operators']
            features['ratio_or'] = features['count_or'] / features['total_operators']
            features['ratio_xor'] = features['count_xor'] / features['total_operators']
            features['ratio_not'] = features['count_not'] / features['total_operators']
        else:
            features['ratio_and'] = 0
            features['ratio_or'] = 0
            features['ratio_xor'] = 0
            features['ratio_not'] = 0
        
        # 括號特徵
        features['num_parentheses'] = all_expressions.count('(')
        features['max_nesting_depth'] = self._calculate_max_nesting(all_expressions)
        
        # 常數特徵（使用正則表達式更準確地匹配常數）
        # 匹配獨立的 0 和 1（不在變數名稱中）
        const0_pattern = r'\b0\b'
        const1_pattern = r'\b1\b'
        features['count_const0'] = len(re.findall(const0_pattern, all_expressions))
        features['count_const1'] = len(re.findall(const1_pattern, all_expressions))
        features['has_constants'] = 1.0 if (features['count_const0'] > 0 or features['count_const1'] > 0) else 0.0
        
        return features
    
    def _calculate_max_nesting(self, expression: str) -> int:
        """計算最大括號嵌套深度"""
        max_depth = 0
        current_depth = 0
        
        for char in expression:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        return max_depth
    
    def extract_expression_complexity_features(self) -> Dict[str, float]:
        """提取表達式複雜度特徵"""
        features = {}
        
        expr_lengths = [len(expr) for expr in self.nodes.values()]
        
        if expr_lengths:
            features['avg_expr_length'] = sum(expr_lengths) / len(expr_lengths)
            features['max_expr_length'] = max(expr_lengths)
            features['min_expr_length'] = min(expr_lengths)
            
            # 標準差
            mean = features['avg_expr_length']
            variance = sum((x - mean) ** 2 for x in expr_lengths) / len(expr_lengths)
            features['std_expr_length'] = variance ** 0.5
        else:
            features['avg_expr_length'] = 0
            features['max_expr_length'] = 0
            features['min_expr_length'] = 0
            features['std_expr_length'] = 0
        
        # 變數使用特徵
        all_vars = set(self.inputs)
        used_vars = set()
        for deps in self.dependencies.values():
            used_vars.update([d for d in deps if d in self.inputs])
        
        features['input_usage_rate'] = len(used_vars) / len(all_vars) if all_vars else 0
        
        # 變數重用率
        var_usage_count = defaultdict(int)
        for deps in self.dependencies.values():
            for dep in deps:
                if dep in self.inputs:
                    var_usage_count[dep] += 1
        
        reused_vars = sum(1 for count in var_usage_count.values() if count > 1)
        features['variable_reuse_rate'] = reused_vars / len(used_vars) if used_vars else 0
        
        return features
    
    def extract_graph_features(self) -> Dict[str, float]:
        """提取圖形特徵（簡化版）"""
        features = {}
        
        # 構建節點集合
        all_nodes = set(self.inputs) | set(self.nodes.keys())
        
        # 計算邊數
        edge_count = 0
        for node_name, deps in self.dependencies.items():
            edge_count += len([d for d in deps if d in all_nodes])
        
        features['graph_nodes'] = len(all_nodes)
        features['graph_edges'] = edge_count
        
        # 圖密度（對於有向圖）
        n = features['graph_nodes']
        if n > 1:
            max_edges = n * (n - 1)  # 有向圖最大邊數
            features['graph_density'] = edge_count / max_edges if max_edges > 0 else 0
        else:
            features['graph_density'] = 0
        
        # 平均度數（對於有向圖，每個節點的度數 = 入度 + 出度）
        # 但這裡我們計算的是平均出度（因為 edge_count 是從節點出發的邊數）
        # 如果要計算平均總度數，需要同時考慮入度和出度
        # 當前實現：edge_count 是總邊數，對於有向圖，平均度數 = edge_count / n
        if n > 0:
            features['avg_degree'] = edge_count / n  # 有向圖平均度數
        else:
            features['avg_degree'] = 0
        
        return features
    
    def extract_all_features(self, filepath: str) -> Dict[str, float]:
        """提取所有特徵"""
        self.parse_eqn_file(filepath)
        
        features = {}
        features.update(self.extract_structural_features())
        features.update(self.extract_syntactic_features())
        features.update(self.extract_expression_complexity_features())
        features.update(self.extract_graph_features())
        
        return features


def main():
    parser = argparse.ArgumentParser(
        description='從 EQN 檔案中提取特徵',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'eqn_file',
        type=str,
        help='輸入的 EQN 檔案路徑'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=None,
        help='輸出 CSV 檔案路徑（可選）'
    )
    
    parser.add_argument(
        '--format',
        choices=['dict', 'csv', 'json'],
        default='dict',
        help='輸出格式（預設: dict）'
    )
    
    args = parser.parse_args()
    
    extractor = EqnFeatureExtractor()
    features = extractor.extract_all_features(args.eqn_file)
    
    if args.format == 'dict':
        print("\n提取的特徵:")
        print("=" * 60)
        for key, value in sorted(features.items()):
            print(f"{key:30s}: {value:15.4f}")
    
    elif args.format == 'csv':
        import csv
        output_file = args.output or 'features.csv'
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=sorted(features.keys()))
            writer.writeheader()
            writer.writerow(features)
        print(f"特徵已保存到: {output_file}")
    
    elif args.format == 'json':
        import json
        output_file = args.output or 'features.json'
        with open(output_file, 'w') as f:
            json.dump(features, f, indent=2)
        print(f"特徵已保存到: {output_file}")
    
    return features


if __name__ == '__main__':
    main()

