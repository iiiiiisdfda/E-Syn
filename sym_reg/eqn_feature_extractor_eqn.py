#!/usr/bin/env python3
"""
EQN 格式電路特徵提取器（針對 aigfuzz_10000_large 格式）

從 EQN 檔案中提取適合用於機器學習訓練的特徵
與 sexpr_feature_extractor.py 提取相同的特徵集

EQN 檔案格式：
- INORDER = pi00 pi01 ... （輸入變數）
- OUTORDER = po00 po01 ... （輸出變數）
- node_name = expression; （節點定義，使用 *, +, ^, ! 運算符）

Usage (stored as csv) : python eqn_feature_extractor_aigfuzz.py <eqn_file> -o <output_file> --format csv
"""

import re
from typing import Dict, List
from collections import defaultdict
import argparse


class EqnFeatureExtractorEqn:
    """EQN 檔案特徵提取器（針對 aigfuzz_10000_large 格式）"""
    
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
        # 移除運算符和括號，提取所有標識符
        tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expression)
        return list(set(tokens))
    
    def _calculate_fanout(self) -> Dict[str, int]:
        """計算每個節點的使用次數（fanout），用於模擬展開後的特徵"""
        fanout = defaultdict(int)
        
        # 統計每個節點被其他節點引用的次數
        for node_name, deps in self.dependencies.items():
            for dep in deps:
                if dep in self.nodes:  # 只統計中間節點，不包括輸入變數
                    fanout[dep] += 1
        
        # 輸出節點至少被使用 1 次（作為輸出）
        for output in self.outputs:
            if output in self.nodes:
                fanout[output] = max(fanout[output], 1)
        
        return fanout
    
    def extract_structural_features(self) -> Dict[str, float]:
        """提取結構特徵（模擬展開後，考慮節點重用次數）"""
        features = {}
        
        # 計算每個節點的使用次數（fanout）
        fanout = self._calculate_fanout()
        
        # 計算內部節點數（模擬展開後：每個節點定義 × 使用次數）
        # 例如：new_n7_ 定義1次，使用7次 → 展開後算7個節點
        # 注意：在展開後的視圖中，所有節點（包括輸出節點）都算內部節點
        total_expanded_nodes = 0
        for node_name in self.nodes:
            usage_count = max(fanout.get(node_name, 0), 1)
            total_expanded_nodes += usage_count
        
        # 在展開後的視圖中，所有節點都是內部節點（因為已經展開）
        features['num_internal_nodes'] = total_expanded_nodes
        
        # 使用動態規劃一次性計算所有節點的深度（避免重複計算和遞歸開銷）
        depth_cache = {}
        
        def get_node_depth(node: str) -> int:
            """計算節點的邏輯深度（使用動態規劃）"""
            # 檢查緩存
            if node in depth_cache:
                return depth_cache[node]
            
            # 輸入節點深度為 0
            if node in self.inputs:
                depth_cache[node] = 0
                return 0
            
            # 不存在的節點深度為 0
            if node not in self.nodes:
                depth_cache[node] = 0
                return 0
            
            # 獲取依賴節點
            deps = self.dependencies[node]
            if not deps:
                depth_cache[node] = 1
                return 1
            
            # 計算所有依賴節點的最大深度
            max_dep_depth = 0
            for dep in deps:
                dep_depth = get_node_depth(dep)
                max_dep_depth = max(max_dep_depth, dep_depth)
            
            # 當前節點深度 = 1 + 最大依賴深度
            depth = 1 + max_dep_depth
            depth_cache[node] = depth
            return depth
        
        # 計算所有輸出節點的深度
        max_depth = 0
        depth_sum = 0
        for output in self.outputs:
            depth = get_node_depth(output)
            max_depth = max(max_depth, depth)
            depth_sum += depth
        features['max_logic_depth'] = max_depth
        features['avg_logic_depth'] = depth_sum / len(self.outputs) if self.outputs else 0
        
        # 計算扇入扇出（模擬展開後：考慮重用次數）
        fanin_counts = []
        fanout_counts = []
        
        for node_name, expr in self.nodes.items():
            deps = self.dependencies[node_name]
            fanin = len(deps)
            usage_count = max(fanout.get(node_name, 0), 1)
            
            # 扇入：每個使用都算一次
            for _ in range(usage_count):
                fanin_counts.append(fanin)
            
            # 扇出：已經在 fanout 中計算了
            if node_name in fanout:
                fanout_counts.append(fanout[node_name])
        
        features['avg_fanin'] = sum(fanin_counts) / len(fanin_counts) if fanin_counts else 0
        features['max_fanin'] = max(fanin_counts) if fanin_counts else 0
        features['avg_fanout'] = sum(fanout_counts) / len(fanout_counts) if fanout_counts else 0
        features['max_fanout'] = max(fanout_counts) if fanout_counts else 0
        
        return features
        
        
        
    
    def extract_syntactic_features(self) -> Dict[str, float]:
        """提取語法特徵（模擬展開後，考慮節點重用次數）
        
        如果中間變數 c = a^b，且 c 被使用了 n 次，
        那麼這個 ^ 會被計算為出現 n 次。
        """
        features = {}
        
        # 計算每個節點的使用次數（fanout）- 使用統一的方法
        fanout = self._calculate_fanout()
        
        # 統計運算符（考慮重用次數）
        # 在 EQN 格式中：* 表示 AND，+ 表示 OR，^ 表示 XOR，! 表示 NOT
        count_and = 0
        count_or = 0
        count_xor = 0
        count_not = 0
        
        for node_name, expression in self.nodes.items():
            # 節點的使用次數：如果沒有被其他節點使用，至少為 1（因為它被定義了）
            # 如果是輸出節點，至少為 1
            usage_count = max(fanout.get(node_name, 0), 1)
            
            # 統計該表達式中的運算符，並乘以使用次數
            # 例如：c = a^b，如果 c 被使用 3 次，則 ^ 被計算為 3 次
            count_and += expression.count('*') * usage_count
            count_or += expression.count('+') * usage_count
            count_xor += expression.count('^') * usage_count
            count_not += expression.count('!') * usage_count
        
        features['count_and'] = count_and
        features['count_or'] = count_or
        features['count_xor'] = count_xor
        features['count_not'] = count_not
        features['total_operators'] = count_and + count_or + count_xor + count_not
        
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
        
        # 括號特徵（也考慮重用次數）
        # 與 Rust 版本一致：每個節點對應一對括號
        # 但這裡需要考慮重用次數，因為 EQN 是壓縮表示
        num_parentheses = 0
        max_nesting = 0
        # 使用緩存避免重複計算嵌套深度
        nesting_cache = {}
        for node_name, expression in self.nodes.items():
            usage_count = max(fanout.get(node_name, 0), 1)
            # 每個運算符節點對應一對括號，但 EQN 中可能沒有顯式括號
            # 為了與 Rust 版本一致，我們計算實際的運算符節點數
            operator_count = expression.count('*') + expression.count('+') + expression.count('^') + expression.count('!')
            # 每個運算符節點在 S-expression 中對應一對括號
            num_parentheses += operator_count * 2 * usage_count
            # 計算展開後的嵌套深度（考慮中間變數展開時增加的嵌套，使用緩存）
            expanded_nesting = self._calculate_expanded_nesting_depth(node_name, cache=nesting_cache)
            max_nesting = max(max_nesting, expanded_nesting)
        
        features['num_parentheses'] = num_parentheses
        features['max_nesting_depth'] = max_nesting
        
        return features
    
    def _calculate_max_nesting(self, expression: str) -> int:
        """計算最大括號嵌套深度（僅統計表達式本身的括號）"""
        max_depth = 0
        current_depth = 0
        
        for char in expression:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        return max_depth
    
    def _calculate_expanded_nesting_depth(self, node: str, visited: set = None, cache: Dict[str, int] = None) -> int:
        """計算節點展開後的最大嵌套深度（帶緩存優化）
        
        考慮中間變數展開的情況：
        - c = a^b (nesting_depth = 0)
        - d = c^e (nesting_depth = 0)
        - 展開後：d = (a^b)^e (nesting_depth = 1，因為 c 被展開為 (a^b))
        
        當中間變數被展開時，會增加一層嵌套深度。
        
        使用緩存避免重複計算，提升性能。
        """
        # 檢查緩存
        if cache is not None and node in cache:
            return cache[node]
        
        if visited is None:
            visited = set()
        
        if node in visited:
            return 0  # 避免循環依賴
        
        if node in self.inputs:
            return 0  # 輸入節點沒有嵌套
        
        if node not in self.nodes:
            return 0
        
        visited.add(node)
        expression = self.nodes[node]
        
        # 1. 計算表達式本身的括號嵌套深度
        base_nesting = self._calculate_max_nesting(expression)
        
        # 2. 提取所有依賴的中間節點（使用已計算的依賴關係，避免重複正則表達式）
        deps = self.dependencies.get(node, [])
        max_dep_nesting = 0
        
        for token in deps:
            # 如果是中間節點（不是輸入變數），需要展開
            if token in self.nodes and token not in self.inputs:
                # 遞歸計算依賴節點的展開後嵌套深度（傳遞緩存）
                dep_nesting = self._calculate_expanded_nesting_depth(token, visited.copy(), cache)
                # 當依賴節點被展開時，會增加一層嵌套（因為會被包在括號中）
                max_dep_nesting = max(max_dep_nesting, dep_nesting + 1)
        
        visited.remove(node)
        
        # 展開後的嵌套深度 = max(表達式本身的嵌套, 依賴節點展開後的嵌套 + 1)
        result = max(base_nesting, max_dep_nesting)
        
        # 存入緩存
        if cache is not None:
            cache[node] = result
        
        return result
    
    def _count_nodes_in_expression(self, expression: str) -> int:
        """計算表達式中的節點數量（與 Rust 版本一致）
        
        節點數 = 運算符數量 + 操作數數量
        例如：pi01 ^ pi00 = 1 (運算符) + 2 (操作數) = 3
        
        注意：與 Rust 版本一致，操作數不去重（每個出現都算一次）
        例如：pi01 ^ pi01 = 1 (運算符) + 2 (操作數，pi01 出現兩次) = 3
        """
        # 統計運算符
        operators = expression.count('*') + expression.count('+') + expression.count('^') + expression.count('!')
        
        # 統計操作數（變數和節點名）
        # 移除運算符和括號，提取所有標識符
        tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expression)
        operands = len(tokens)  # 不去重，與 Rust 版本一致
        
        # 節點數 = 運算符數 + 操作數
        return operators + operands
    
    def _calculate_expanded_expr_length(self, node: str, visited: set = None, cache: Dict[str, int] = None) -> int:
        """計算節點展開後的表達式長度（與 Rust 版本一致：樹中節點總數）
        
        Rust 版本的邏輯：
        - 葉節點（輸入變數）：返回 1
        - 內部節點：返回 1 + 所有子節點的長度之和
        
        這表示以該節點為根的樹中的節點總數。
        
        例如：
        - n1 = a^b: 1 (當前節點) + 1 (a) + 1 (b) = 3
        - n2 = n1^c: 1 (當前節點) + n1的長度(3) + 1 (c) = 5
        
        注意：為了避免數值溢出，設置最大限制
        """
        # 檢查緩存
        if cache is not None and node in cache:
            return cache[node]
        
        if visited is None:
            visited = set()
        
        if node in visited:
            return 0  # 避免循環依賴
        
        if node in self.inputs:
            return 1  # 葉節點（輸入變數）返回 1
        
        if node not in self.nodes:
            return 0
        
        visited.add(node)
        expression = self.nodes[node]
        
        # 當前節點算 1
        expanded_length = 1
        
        # 統計每個依賴的出現次數（不去重，因為同一個節點可能被使用多次）
        tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expression)
        from collections import Counter
        dep_counts = Counter(tokens)
        
        # 設置最大限制，避免數值溢出（對於非常大的電路）
        MAX_EXPR_LENGTH = 10**15  # 約 1 千萬億
        
        for dep, count in dep_counts.items():
            if expanded_length > MAX_EXPR_LENGTH:
                break  # 如果已經超過限制，停止計算
            
            if dep in self.inputs:
                # 輸入變數（葉節點）：每個出現算 1
                expanded_length += count
            elif dep in self.nodes:
                # 中間變數：遞歸計算展開後的長度
                dep_length = self._calculate_expanded_expr_length(dep, visited.copy(), cache)
                
                # 檢查是否會導致溢出
                if dep_length > MAX_EXPR_LENGTH or count * dep_length > MAX_EXPR_LENGTH:
                    expanded_length = MAX_EXPR_LENGTH
                    break
                
                # 每個出現都算一次完整的長度
                expanded_length += count * dep_length
        
        visited.remove(node)
        
        # 限制最大值
        expanded_length = min(expanded_length, MAX_EXPR_LENGTH)
        
        # 存入緩存
        if cache is not None:
            cache[node] = expanded_length
        
        return expanded_length
    
    def extract_expression_complexity_features(self) -> Dict[str, float]:
        """提取表達式複雜度特徵（計算所有節點的 expr_length，與 Rust 版本一致）"""
        features = {}
        
        # expr_length 計算已註釋掉
        # # 使用緩存避免重複計算
        # expr_length_cache = {}
        # 
        # # 計算所有節點的表達式長度（展開後，與 Rust 版本一致）
        # expr_lengths = []
        # for node_name, expression in self.nodes.items():
        #     # 計算展開後的表達式長度（遞歸展開所有中間變數，使用緩存）
        #     expr_length = self._calculate_expanded_expr_length(node_name, cache=expr_length_cache)
        #     expr_lengths.append(expr_length)
        # 
        # if expr_lengths:
        #     features['avg_expr_length'] = sum(expr_lengths) / len(expr_lengths)
        #     features['max_expr_length'] = max(expr_lengths)
        #     features['min_expr_length'] = min(expr_lengths)
        #     
        #     # 標準差
        #     mean = features['avg_expr_length']
        #     variance = sum((x - mean) ** 2 for x in expr_lengths) / len(expr_lengths)
        #     features['std_expr_length'] = variance ** 0.5
        # else:
        #     features['avg_expr_length'] = 0
        #     features['max_expr_length'] = 0
        #     features['min_expr_length'] = 0
        #     features['std_expr_length'] = 0
        
        # 設置默認值
        # features['avg_expr_length'] = 0
        # features['max_expr_length'] = 0
        # features['min_expr_length'] = 0
        # features['std_expr_length'] = 0
        
        # 括號嵌套深度特徵（邏輯複雜度，模擬展開後：每個定義 × 使用次數）
        # 注意：需要考慮中間變數展開時增加的嵌套深度
        # 例如：c = a^b, d = c^e → 展開後 d = (a^b)^e，嵌套深度增加 1
        weighted_nesting_depths = []
        # 計算每個節點的使用次數（fanout）
        fanout = self._calculate_fanout()
        # 使用緩存避免重複計算嵌套深度（與 extract_syntactic_features 共享緩存）
        nesting_cache = {}
        for node_name, expression in self.nodes.items():
            # 計算展開後的嵌套深度（考慮中間變數展開，使用緩存）
            nesting_depth = self._calculate_expanded_nesting_depth(node_name, cache=nesting_cache)
            usage_count = max(fanout.get(node_name, 0), 1)
            # 展開後：每個使用都算一次
            for _ in range(usage_count):
                weighted_nesting_depths.append(nesting_depth)
        
        if weighted_nesting_depths:
            features['avg_nesting_depth'] = sum(weighted_nesting_depths) / len(weighted_nesting_depths)
            features['max_nesting_depth'] = max(weighted_nesting_depths)
            features['min_nesting_depth'] = min(weighted_nesting_depths)
            
            # 標準差
            mean_nesting = features['avg_nesting_depth']
            variance_nesting = sum((x - mean_nesting) ** 2 for x in weighted_nesting_depths) / len(weighted_nesting_depths)
            features['std_nesting_depth'] = variance_nesting ** 0.5
        else:
            features['avg_nesting_depth'] = 0
            features['max_nesting_depth'] = 0
            features['min_nesting_depth'] = 0
            features['std_nesting_depth'] = 0
        
        return features
    
    def extract_graph_features(self) -> Dict[str, float]:
        """提取圖形特徵
        
        注意：圖特徵在 EQN 和 S-expression 格式中本質不同
        - EQN：基於壓縮表示的圖（中間變數定義一次，可重用）
        - S-expression：基於完全展開的圖（每次使用都是獨立節點）
        因此這些特徵已被移除，以保持兩個版本的一致性
        """
        features = {}
        # 圖特徵已移除，因為 EQN 和 S-expression 的圖結構本質不同
        return features
    
    def extract_all_features(self, filepath: str) -> Dict[str, float]:
        """提取所有特徵"""
        self.parse_eqn_file(filepath)
        
        features = {}
        features.update(self.extract_structural_features())
        features.update(self.extract_syntactic_features())
        features.update(self.extract_expression_complexity_features())
        # 注意：extract_graph_features 已移除圖特徵，因為 EQN 和 S-expression 的圖結構本質不同
        # features.update(self.extract_graph_features())
        
        return features


def main():
    parser = argparse.ArgumentParser(
        description='從 EQN 檔案中提取特徵（針對 aigfuzz_10000_large 格式）',
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
    
    extractor = EqnFeatureExtractorEqn()
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

