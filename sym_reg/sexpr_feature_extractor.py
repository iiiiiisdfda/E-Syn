#!/usr/bin/env python3
"""
S-expression 格式電路特徵提取器

從 S-expression 檔案中提取適合用於機器學習訓練的特徵
與 eqn_feature_extractor.py 提取相同的特徵集

Usage (stored as csv) : python sexpr_feature_extractor.py <sexpr_file> -o <output_file> --format csv
"""

import re
from typing import Dict, List, Union, Set
from collections import defaultdict
import argparse


class SExprNode:
    """S-expression 節點表示"""
    def __init__(self, operator: str = None, children: List = None, value: str = None):
        self.operator = operator  # &, +, *, !, ^
        self.children = children or []
        self.value = value  # 變數名稱（如 pi00, pi01）
        self.is_leaf = value is not None
    
    def __repr__(self):
        if self.is_leaf:
            return f"Leaf({self.value})"
        return f"Node({self.operator}, {len(self.children)} children)"


class SExprFeatureExtractor:
    """S-expression 檔案特徵提取器"""
    
    def __init__(self):
        self.root = None
        self.all_nodes = []  # 所有節點（用於統計）
        self.variables = set()  # 所有變數
        self.node_dependencies = defaultdict(set)  # 節點依賴關係
        self.fanout = defaultdict(int)  # 變數/節點的扇出
    
    def parse_sexpr_file(self, filepath: str) -> None:
        """解析 S-expression 檔案"""
        with open(filepath, 'r') as f:
            content = f.read().strip()
        
        # 解析 s-expression
        self.root = self._parse_sexpr(content)
        
        # 構建依賴關係和統計信息
        self._build_dependencies()
    
    def _parse_sexpr(self, sexpr_str: str) -> SExprNode:
        """遞歸解析 S-expression 字符串（使用位置指針）"""
        sexpr_str = sexpr_str.strip()
        pos = [0]  # 使用列表以便在遞歸中修改
        
        def parse_atom():
            """解析原子（變數）"""
            start = pos[0]
            while pos[0] < len(sexpr_str) and not sexpr_str[pos[0]].isspace() and sexpr_str[pos[0]] not in '()':
                pos[0] += 1
            return sexpr_str[start:pos[0]]
        
        def skip_whitespace():
            """跳過空白字符"""
            while pos[0] < len(sexpr_str) and sexpr_str[pos[0]].isspace():
                pos[0] += 1
        
        def parse_expr():
            """解析表達式"""
            skip_whitespace()
            
            if pos[0] >= len(sexpr_str):
                return None
            
            # 如果是葉節點（變數）
            if sexpr_str[pos[0]] != '(':
                var_name = parse_atom()
                if var_name:
                    self.variables.add(var_name)
                    return SExprNode(value=var_name)
                return None
            
            # 移除外層左括號
            pos[0] += 1
            skip_whitespace()
            
            # 解析運算符（第一個 token）
            operator = parse_atom()
            if not operator:
                # 如果沒有運算符，可能是空列表或其他格式
                pos[0] -= 1  # 回退
                return None
            
            skip_whitespace()
            
            # 解析子表達式
            children = []
            while pos[0] < len(sexpr_str) and sexpr_str[pos[0]] != ')':
                child = parse_expr()
                if child:
                    children.append(child)
                skip_whitespace()
            
            # 跳過右括號
            if pos[0] < len(sexpr_str) and sexpr_str[pos[0]] == ')':
                pos[0] += 1
            
            return SExprNode(operator=operator, children=children)
        
        return parse_expr()
    
    def _build_dependencies(self) -> None:
        """構建節點依賴關係和統計信息"""
        node_counter = [0]  # 使用列表以便在遞歸中修改
        
        def traverse(node: SExprNode, parent_id: str = None):
            if node.is_leaf:
                # 葉節點是變數
                if parent_id:
                    self.node_dependencies[parent_id].add(node.value)
                    self.fanout[node.value] += 1
                return
            
            # 為內部節點生成唯一 ID
            node_id = f"node_{node_counter[0]}"
            node_counter[0] += 1
            self.all_nodes.append(node)
            
            # 記錄依賴關係
            for child in node.children:
                if child.is_leaf:
                    self.node_dependencies[node_id].add(child.value)
                    self.fanout[child.value] += 1
                else:
                    # 為子節點生成 ID 並記錄依賴
                    child_id = f"node_{node_counter[0]}"
                    self.node_dependencies[node_id].add(child_id)
                    traverse(child, child_id)
            
            # 遞歸處理子節點（已經在上面處理了，這裡不需要重複）
        
        if self.root:
            traverse(self.root)
    
    def _collect_all_nodes(self, node: SExprNode) -> List[SExprNode]:
        """收集所有節點"""
        nodes = []
        if not node.is_leaf:
            nodes.append(node)
            for child in node.children:
                nodes.extend(self._collect_all_nodes(child))
        return nodes
    
    def extract_structural_features(self) -> Dict[str, float]:
        """提取結構特徵"""
        features = {}
        
        # 計算內部節點數（非葉節點）
        all_nodes_list = self._collect_all_nodes(self.root) if self.root else []
        features['num_internal_nodes'] = len(all_nodes_list)
        
        # 計算扇入扇出
        fanin_counts = []
        for node_id, deps in self.node_dependencies.items():
            fanin_counts.append(len(deps))
        
        features['avg_fanin'] = sum(fanin_counts) / len(fanin_counts) if fanin_counts else 0
        features['max_fanin'] = max(fanin_counts) if fanin_counts else 0
        features['avg_fanout'] = sum(self.fanout.values()) / len(self.fanout) if self.fanout else 0
        features['max_fanout'] = max(self.fanout.values()) if self.fanout else 0
        
        return features
    
    def _count_operators(self, node: SExprNode) -> Dict[str, int]:
        """遞歸計算運算符數量"""
        counts = {'&': 0, '+': 0, '*': 0, '!': 0, '^': 0}
        
        def traverse(n: SExprNode):
            if not n.is_leaf and n.operator:
                if n.operator in counts:
                    counts[n.operator] += 1
                for child in n.children:
                    traverse(child)
        
        if node:
            traverse(node)
        return counts
    
    def _calculate_max_nesting(self, node: SExprNode, current_depth: int = 0) -> int:
        """計算最大嵌套深度"""
        if node.is_leaf:
            return current_depth
        
        max_depth = current_depth
        for child in node.children:
            child_depth = self._calculate_max_nesting(child, current_depth + 1)
            max_depth = max(max_depth, child_depth)
        
        return max_depth
    
    def extract_syntactic_features(self) -> Dict[str, float]:
        """提取語法特徵"""
        features = {}
        
        # 運算符計數
        op_counts = self._count_operators(self.root)
        features['count_and'] = op_counts['&'] + op_counts['*']  # & 和 * 都表示 AND
        features['count_or'] = op_counts['+']
        features['count_xor'] = op_counts['^']
        features['count_not'] = op_counts['!']
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
        
        # 括號特徵（在 s-expression 中，每個非葉節點都有一對括號）
        all_nodes_list = self._collect_all_nodes(self.root) if self.root else []
        features['num_parentheses'] = len(all_nodes_list) * 2  # 每個節點一對括號
        
        # 最大嵌套深度（從根節點開始計算，但會被 expression_complexity 中的覆蓋）
        # 為了與 EQN 提取器保持一致，這裡先計算一個值
        max_nesting = self._calculate_max_nesting(self.root) if self.root else 0
        features['max_nesting_depth'] = max_nesting
        
        return features
    
    def _get_expression_length(self, node: SExprNode) -> int:
        """計算表達式長度（節點數）"""
        if node.is_leaf:
            return 1
        return 1 + sum(self._get_expression_length(child) for child in node.children)
    
    def extract_expression_complexity_features(self) -> Dict[str, float]:
        """提取表達式複雜度特徵"""
        features = {}
        
        all_nodes_list = self._collect_all_nodes(self.root) if self.root else []
        
        # 計算每個子樹的大小（節點數）
        if self.root:
            # 對於 s-expression，我們可以計算每個子表達式的大小
            expr_sizes = []
            def collect_sizes(n: SExprNode):
                if not n.is_leaf:
                    size = self._get_expression_length(n)
                    expr_sizes.append(size)
                    for child in n.children:
                        collect_sizes(child)
            
            collect_sizes(self.root)
            
            if expr_sizes:
                features['avg_expr_length'] = sum(expr_sizes) / len(expr_sizes)
                features['max_expr_length'] = max(expr_sizes)
                features['min_expr_length'] = min(expr_sizes)
                
                # 標準差
                mean = features['avg_expr_length']
                variance = sum((x - mean) ** 2 for x in expr_sizes) / len(expr_sizes)
                features['std_expr_length'] = variance ** 0.5
            else:
                features['avg_expr_length'] = 0
                features['max_expr_length'] = 0
                features['min_expr_length'] = 0
                features['std_expr_length'] = 0
        else:
            features['avg_expr_length'] = 0
            features['max_expr_length'] = 0
            features['min_expr_length'] = 0
            features['std_expr_length'] = 0
        
        # 嵌套深度特徵
        nesting_depths = []
        def collect_nesting(n: SExprNode, depth: int = 0):
            if not n.is_leaf:
                nesting_depths.append(depth)
                for child in n.children:
                    collect_nesting(child, depth + 1)
        
        if self.root:
            collect_nesting(self.root)
        
        if nesting_depths:
            features['avg_nesting_depth'] = sum(nesting_depths) / len(nesting_depths)
            features['max_nesting_depth'] = max(nesting_depths)
            features['min_nesting_depth'] = min(nesting_depths)
            
            # 標準差
            mean_nesting = features['avg_nesting_depth']
            variance_nesting = sum((x - mean_nesting) ** 2 for x in nesting_depths) / len(nesting_depths)
            features['std_nesting_depth'] = variance_nesting ** 0.5
        else:
            features['avg_nesting_depth'] = 0
            features['max_nesting_depth'] = 0
            features['min_nesting_depth'] = 0
            features['std_nesting_depth'] = 0
        
        return features
    
    def extract_graph_features(self) -> Dict[str, float]:
        """提取圖形特徵"""
        features = {}
        
        # 構建節點集合（變數 + 內部節點）
        all_nodes_list = self._collect_all_nodes(self.root) if self.root else []
        graph_nodes = len(self.variables) + len(all_nodes_list)
        
        # 計算邊數（依賴關係）
        edge_count = sum(len(deps) for deps in self.node_dependencies.values())
        
        features['graph_nodes'] = graph_nodes
        features['graph_edges'] = edge_count
        
        # 圖密度
        n = features['graph_nodes']
        if n > 1:
            max_edges = n * (n - 1)  # 有向圖最大邊數
            features['graph_density'] = edge_count / max_edges if max_edges > 0 else 0
        else:
            features['graph_density'] = 0
        
        # 平均度數
        if n > 0:
            features['avg_degree'] = edge_count / n
        else:
            features['avg_degree'] = 0
        
        return features
    
    def extract_analyzer_features(self) -> Dict[str, float]:
        """提取 analyzer 相關特徵（與 data_collect.py 中的特徵對應）"""
        features = {}
        
        # 1. 運算符計數（+, !, *, &）
        op_counts = self._count_operators(self.root)
        # 映射到 analyzer 的格式：+ 對應 OR, ! 對應 NOT, * 對應 AND, & 對應 CONCAT
        features['+'] = float(op_counts.get('+', 0))
        features['!'] = float(op_counts.get('!', 0))
        features['*'] = float(op_counts.get('*', 0))
        features['&'] = float(op_counts.get('&', 0))
        
        # 2. ASTSize: AST 中所有節點的總數（包括葉節點和內部節點）
        def count_all_nodes(node: SExprNode) -> int:
            """遞歸計算所有節點數（包括葉節點）"""
            if node.is_leaf:
                return 1
            return 1 + sum(count_all_nodes(child) for child in node.children)
        
        if self.root:
            features['ASTSize'] = float(count_all_nodes(self.root))
        else:
            features['ASTSize'] = 0.0
        
        # 3. ASTDepth: AST 的最大深度（從根節點到最深葉節點的路徑長度）
        def calculate_depth(node: SExprNode, current_depth: int = 0) -> int:
            """計算節點深度"""
            if node.is_leaf:
                return current_depth
            if not node.children:
                return current_depth
            return max(calculate_depth(child, current_depth + 1) for child in node.children)
        
        if self.root:
            features['ASTDepth'] = float(calculate_depth(self.root))
        else:
            features['ASTDepth'] = 0.0
        
        # 4. SUM_LIB: 所有運算符的 Liberty 成本總和
        # Liberty 成本：! = 9, + = 26, * = 22, & = 22 (CONCAT 通常與 AND 類似), ^ = 24
        liberty_costs = {
            '!': 9,
            '+': 26,
            '*': 22,
            '&': 22,  # CONCAT 使用與 AND 相同的成本
            '^': 24
        }
        sum_lib = sum(liberty_costs.get(op, 0) * count for op, count in op_counts.items())
        features['SUM_LIB'] = float(sum_lib)
        
        # 5. SUM_NODE: 所有運算符節點的總數（不包括葉節點）
        sum_node = sum(op_counts.values())
        features['SUM_NODE'] = float(sum_node)
        
        # 6. AVE_LIB: 平均 Liberty 成本
        if sum_node > 0:
            features['AVE_LIB'] = float(sum_lib) / float(sum_node)
        else:
            features['AVE_LIB'] = 0.0
        
        return features
    
    def extract_all_features(self, filepath: str) -> Dict[str, float]:
        """提取所有特徵"""
        self.parse_sexpr_file(filepath)
        
        features = {}
        features.update(self.extract_structural_features())
        features.update(self.extract_syntactic_features())
        features.update(self.extract_expression_complexity_features())
        features.update(self.extract_graph_features())
        features.update(self.extract_analyzer_features())  # 添加 analyzer 相關特徵
        
        return features


def main():
    parser = argparse.ArgumentParser(
        description='從 S-expression 檔案中提取特徵',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'sexpr_file',
        type=str,
        help='輸入的 S-expression 檔案路徑'
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
    
    extractor = SExprFeatureExtractor()
    features = extractor.extract_all_features(args.sexpr_file)
    
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

