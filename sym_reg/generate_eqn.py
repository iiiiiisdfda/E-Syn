#!/usr/bin/env python3
"""
隨機生成 ABC EQN 格式的布林電路檔案

根據 ABC 的 read_eqn 解析規則（參考 src/base/io/ioReadEqn.c 和 src/misc/parse/parseEqn.c）：

支援的運算符：
- ! : 否定 (NOT) - 優先順序 10（最高）
- * : 邏輯 AND - 優先順序 9
- ^ : 邏輯 XOR - 優先順序 8
- + : 邏輯 OR - 優先順序 7（最低）
- 0, 1 : 邏輯常數（可選）

ABC 解析規則：
1. 變數名不能包含運算符符號：! * + ^ ( )
2. 兩個變數之間必須有運算符（不能直接連接）
3. 變數後跟括號時，必須有運算符（不能 var(...)）
4. 括號必須平衡（開括號和閉括號數量相等）
5. 空格、換行符、制表符會被忽略（但為可讀性可保留）
6. 否定運算符 ! 必須緊貼變數（!var，不能 ! var）
7. 如果否定符後跟變數，會隱式添加 AND（!var1 var2 會被解析為 !var1 * var2）
"""

import random
import argparse
from typing import List, Optional


class EqnGenerator:
    """EQN 檔案生成器"""
    
    def __init__(self, use_constants: bool = False, seed: Optional[int] = None):
        """
        初始化生成器
        
        Args:
            use_constants: 是否在表達式中使用邏輯常數 0 和 1
            seed: 隨機種子（用於可重現性）
        """
        self.use_constants = use_constants
        if seed is not None:
            random.seed(seed)
    
    def _get_operator_precedence(self, operator: str) -> int:
        """
        獲取運算符優先順序
        
        Args:
            operator: 運算符符號
            
        Returns:
            優先順序數值（越大優先順序越高）
        """
        precedence_map = {
            '*': 9,  # AND
            '^': 8,  # XOR
            '+': 7,  # OR
        }
        return precedence_map.get(operator, 0)
    
    def _needs_parentheses(self, expr: str, parent_operator: str) -> bool:
        """
        判斷表達式是否需要括號
        
        Args:
            expr: 子表達式
            parent_operator: 父運算符
            
        Returns:
            是否需要括號
        """
        # 如果是終端節點（不包含運算符），不需要括號
        if not any(op in expr for op in ['*', '+', '^']):
            return False
        
        # 如果表達式已經有括號包裹，不需要再加
        if expr.startswith('(') and expr.endswith(')'):
            # 檢查括號是否平衡且完整包裹
            paren_count = 0
            fully_wrapped = True
            for i, char in enumerate(expr):
                if char == '(':
                    paren_count += 1
                elif char == ')':
                    paren_count -= 1
                    if paren_count == 0 and i < len(expr) - 1:
                        # 括號在表達式中間結束，不是完整包裹
                        fully_wrapped = False
                        break
            if fully_wrapped and paren_count == 0:
                # 已經有完整括號包裹，不需要再加
                return False
        
        # 提取表達式的主要運算符（最外層的運算符）
        # 簡單檢查：如果表達式包含多個運算符，需要根據優先順序判斷
        has_and = '*' in expr
        has_xor = '^' in expr
        has_or = '+' in expr
        
        # 如果子表達式包含多個不同類型的運算符，為了安全起見，需要括號
        operator_count = sum([has_and, has_xor, has_or])
        if operator_count > 1:
            # 多個運算符混合，需要括號確保正確解析
            return True
        
        if parent_operator == '+':
            # OR 優先順序最低，如果子表達式包含 AND 或 XOR，需要括號
            if has_and or has_xor:
                return True
        elif parent_operator == '^':
            # XOR 優先順序中等，如果子表達式包含 AND，需要括號
            if has_and:
                return True
        # AND 優先順序最高，子表達式通常不需要括號（除非是 OR 或 XOR）
        elif parent_operator == '*':
            if has_or or has_xor:
                return True
        
        return False
    
    def _check_balanced_parentheses(self, expr: str) -> bool:
        """
        檢查表達式的括號是否平衡
        
        Args:
            expr: 表達式
            
        Returns:
            括號是否平衡
        """
        count = 0
        for char in expr:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
    
    def _format_expression_in_parentheses(self, expr: str) -> str:
        """
        格式化括號內的表達式，確保運算符和變數名稱之間有空格
        
        Args:
            expr: 表達式
            
        Returns:
            格式化後的表達式
        """
        import re
        
        # 如果表達式已經有括號包裹，先移除外層括號
        if expr.startswith('(') and expr.endswith(')'):
            # 檢查是否完整包裹
            paren_count = 0
            fully_wrapped = True
            for i, char in enumerate(expr):
                if char == '(':
                    paren_count += 1
                elif char == ')':
                    paren_count -= 1
                    if paren_count == 0 and i < len(expr) - 1:
                        fully_wrapped = False
                        break
            if fully_wrapped and paren_count == 0:
                expr = expr[1:-1]  # 移除外層括號
        
        # 使用更簡單的方法：逐字符處理
        result = []
        i = 0
        while i < len(expr):
            char = expr[i]
            
            if char in ['*', '+', '^']:
                # 運算符：確保前後有空格
                # 檢查前面
                if result and result[-1] != ' ':
                    result.append(' ')
                result.append(char)
                # 檢查後面（跳過否定運算符）
                if i + 1 < len(expr):
                    next_char = expr[i + 1]
                    if next_char != ' ' and next_char != '!':
                        result.append(' ')
            elif char == '!':
                # 否定運算符：緊貼變數，不需要空格
                result.append(char)
            elif char == ' ':
                # 跳過現有空格，我們會統一添加
                pass
            else:
                # 其他字符（變數名、括號等）
                result.append(char)
            
            i += 1
        
        formatted = ''.join(result)
        
        # 標準化運算符周圍的空格
        formatted = re.sub(r'\s*\*\s*', ' * ', formatted)
        formatted = re.sub(r'\s*\^\s*', ' ^ ', formatted)
        formatted = re.sub(r'\s+\+\s+', ' + ', formatted)
        
        # 確保否定運算符緊貼變數
        formatted = re.sub(r'!\s+', '!', formatted)
        
        # 清理多餘的空格
        formatted = re.sub(r'\s+', ' ', formatted).strip()
        
        return formatted
    
    def _wrap_in_parentheses(self, expr: str) -> str:
        """
        用括號包裹表達式（如果尚未包裹），並格式化括號內的表達式
        
        Args:
            expr: 表達式
            
        Returns:
            包裹後的表達式
        """
        # 如果已經是終端節點，不需要括號
        if not any(op in expr for op in ['*', '+', '^']):
            return expr
        
        # 檢查是否已經有平衡的括號包裹
        if expr.startswith('(') and expr.endswith(')'):
            # 檢查括號是否完整包裹整個表達式
            paren_count = 0
            fully_wrapped = True
            for i, char in enumerate(expr):
                if char == '(':
                    paren_count += 1
                elif char == ')':
                    paren_count -= 1
                    if paren_count == 0 and i < len(expr) - 1:
                        # 括號在表達式中間結束，不是完整包裹
                        fully_wrapped = False
                        break
            if fully_wrapped and paren_count == 0:
                # 已經有完整括號包裹，且括號平衡
                # 確保括號內的表達式已格式化
                inner_expr = expr[1:-1]
                formatted_inner = self._format_expression_in_parentheses(inner_expr)
                return f"({formatted_inner})"
        
        # 確保括號平衡後再包裹
        if not self._check_balanced_parentheses(expr):
            # 如果括號不平衡，這是一個錯誤，但我們嘗試修復
            # 簡單處理：直接包裹（這可能不是最佳方案，但至少能生成有效表達式）
            pass
        
        # 格式化表達式後再包裹
        formatted_expr = self._format_expression_in_parentheses(expr)
        return f"({formatted_expr})"
    
    def generate_terminal(self, available_vars: List[str]) -> str:
        """
        生成終端節點（變數或常數）
        
        Args:
            available_vars: 可用的變數列表
            
        Returns:
            終端節點字串
        """
        if self.use_constants and random.random() < 0.15:  # 15% 機率使用常數
            return random.choice(['0', '1'])
        else:
            if not available_vars:
                return random.choice(['0', '1']) if self.use_constants else '0'
            var = random.choice(available_vars)
            # 50% 機率加上否定
            if random.random() < 0.5:
                return f"!{var}"
            return var
    
    def generate_expression(self, available_vars: List[str], depth: int = 0, max_depth: int = 3) -> str:
        """
        遞迴生成隨機布林表達式（確保符合 ABC 解析規則）
        
        ABC 解析規則：
        1. 變數名不能包含 !*+() 等運算符
        2. 兩個變數之間必須有運算符
        3. 變數後跟括號時，必須有運算符
        4. 括號必須平衡
        5. 空格會被忽略，但為可讀性可保留
        
        Args:
            available_vars: 可用的變數列表
            depth: 當前遞迴深度
            max_depth: 最大遞迴深度
            
        Returns:
            布林表達式字串
        """
        if not available_vars:
            return random.choice(['0', '1']) if self.use_constants else '0'
        
        # 如果深度達到最大值或隨機決定，返回終端節點
        if depth >= max_depth or (depth > 0 and random.random() < 0.4):
            return self.generate_terminal(available_vars)
        
        # 選擇運算符
        operator = random.choice(['*', '+', '^'])
        
        # 決定操作數數量（2個，偶爾3個）
        num_operands = 2 if random.random() < 0.8 else 3
        
        # 生成操作數
        operands = []
        for _ in range(num_operands):
            # 遞迴生成子表達式
            expr = self.generate_expression(available_vars, depth + 1, max_depth)
            
            # 根據運算符優先順序決定是否需要括號
            # 重要：如果子表達式是變數且父運算符優先順序較低，不需要括號
            # 但如果子表達式包含運算符，需要根據優先順序判斷
            if self._needs_parentheses(expr, operator):
                expr = self._wrap_in_parentheses(expr)
            
            operands.append(expr)
        
        # 組合表達式，確保所有運算符前後都有空格
        # 統一使用空格分隔運算符，然後清理多餘空格
        result = f" {operator} ".join(operands)
        # 清理多餘的空格（但保留運算符周圍的單個空格）
        import re
        result = re.sub(r'\s+', ' ', result).strip()
        
        # 確保運算符和括號、變數之間有空格
        # 處理運算符後緊跟括號的情況：`+(` -> `+ (`, `*(` -> `* (`
        result = re.sub(r'([*+\^])\s*\(', r'\1 (', result)
        # 處理括號後緊跟運算符的情況：`)*` -> `) *`, `)+` -> `) +`
        result = re.sub(r'\)\s*([*+\^])', r') \1', result)
        # 處理變數/否定運算符後緊跟運算符的情況：`var*` -> `var *`, `!var*` -> `!var *`
        # 注意：否定運算符 ! 必須緊貼變數，所以這裡只處理變數名本身
        result = re.sub(r'([a-zA-Z0-9_])\s*([*+\^])', r'\1 \2', result)
        # 處理運算符後緊跟變數/否定運算符的情況：`*var` -> `* var`, `*!var` -> `* !var`
        result = re.sub(r'([*+\^])\s*([a-zA-Z0-9_!])', r'\1 \2', result)
        
        # 再次清理多餘空格
        result = re.sub(r'\s+', ' ', result).strip()
        
        return result
    
    def _validate_variable_name(self, name: str) -> bool:
        """
        驗證變數名是否符合 ABC 規則
        
        ABC 規則：變數名不能包含 !*+() 等運算符
        
        Args:
            name: 變數名
            
        Returns:
            是否符合規則
        """
        forbidden_chars = ['!', '*', '+', '(', ')', '^']
        return not any(char in name for char in forbidden_chars)
    
    def generate_node_name(self, index: int, prefix: str = "new_n") -> str:
        """
        生成節點名稱（確保符合 ABC 規則）
        
        Args:
            index: 節點索引
            prefix: 名稱前綴
            
        Returns:
            節點名稱
        """
        name = f"{prefix}{index}_"
        # 確保變數名符合規則（不包含運算符）
        if not self._validate_variable_name(name):
            # 如果不符合，使用更安全的名稱格式
            name = f"{prefix}{index}_"
        return name
    
    def generate_eqn_file(
        self,
        output_file: str,
        num_inputs: int = 10,
        num_outputs: int = 5,
        num_internal_nodes: int = 20,
        input_prefix: str = "pi",
        output_prefix: str = "po",
        max_depth: int = 3
    ):
        """
        生成完整的 EQN 檔案
        
        Args:
            output_file: 輸出檔案路徑
            num_inputs: 輸入變數數量
            num_outputs: 輸出變數數量
            num_internal_nodes: 內部節點數量
            input_prefix: 輸入變數前綴
            output_prefix: 輸出變數前綴
            max_depth: 表達式最大深度
        """
        # 生成輸入變數
        input_vars = [f"{input_prefix}{i:02d}" for i in range(num_inputs)]
        
        # 生成輸出變數
        output_vars = [f"{output_prefix}{i:02d}" for i in range(num_outputs)]
        
        # 生成內部節點名稱
        internal_nodes = [self.generate_node_name(i) for i in range(num_internal_nodes)]
        
        # 所有可用的變數（輸入 + 已定義的內部節點）
        all_available_vars = input_vars + internal_nodes
        
        # 生成檔案內容
        lines = []
        
        # 添加註解
        lines.append(f"# Randomly generated EQN file")
        if self.use_constants:
            lines.append(f"# Includes logical constants 0 and 1")
        lines.append("")
        
        # 生成 INORDER
        lines.append(f"INORDER = {' '.join(input_vars)};")
        
        # 生成 OUTORDER
        lines.append(f"OUTORDER = {' '.join(output_vars)};")
        lines.append("")
        
        # 生成內部節點
        for i, node_name in enumerate(internal_nodes):
            # 可用的變數：輸入變數 + 之前定義的內部節點
            available = input_vars + internal_nodes[:i]
            
            # 生成表達式，確保括號平衡
            max_attempts = 10
            expr = None
            for attempt in range(max_attempts):
                expr = self.generate_expression(available, max_depth=max_depth)
                if self._check_balanced_parentheses(expr):
                    break
                # 如果括號不平衡，重試
                if attempt == max_attempts - 1:
                    # 最後一次嘗試，強制修復（簡單處理：如果括號不平衡，重新生成簡單表達式）
                    expr = self.generate_terminal(available)
            
            lines.append(f"{node_name} = {expr};")
        
        lines.append("")
        
        # 生成輸出節點
        for output_var in output_vars:
            # 輸出可以依賴所有輸入和內部節點
            available = all_available_vars
            
            # 生成表達式（輸出節點通常較簡單），確保括號平衡
            max_attempts = 10
            expr = None
            for attempt in range(max_attempts):
                expr = self.generate_expression(available, max_depth=min(max_depth, 2))
                if self._check_balanced_parentheses(expr):
                    break
                # 如果括號不平衡，重試
                if attempt == max_attempts - 1:
                    # 最後一次嘗試，強制修復
                    expr = self.generate_terminal(available)
            
            lines.append(f"{output_var} = {expr};")
        
        # 寫入檔案
        with open(output_file, 'w') as f:
            f.write('\n'.join(lines))
        
        print(f"Generated EQN file: {output_file}")
        print(f"  Inputs: {num_inputs}")
        print(f"  Outputs: {num_outputs}")
        print(f"  Internal nodes: {num_internal_nodes}")
        print(f"  Use constants: {self.use_constants}")


def main():
    parser = argparse.ArgumentParser(
        description='隨機生成 ABC EQN 格式的布林電路檔案',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  # 生成基本電路（不含常數）
  python generate_eqn.py -o circuit.eqn -i 10 -o 5 -n 20
  
  # 生成包含邏輯常數的電路
  python generate_eqn.py -o circuit.eqn -i 10 -o 5 -n 20 --use-constants
  
  # 使用隨機種子以確保可重現性
  python generate_eqn.py -o circuit.eqn -i 10 -o 5 -n 20 --seed 42
        """
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help='輸出 EQN 檔案路徑'
    )
    
    parser.add_argument(
        '-i', '--inputs',
        type=int,
        default=10,
        help='輸入變數數量 (預設: 10)'
    )
    
    parser.add_argument(
        '--outputs',
        type=int,
        default=5,
        help='輸出變數數量 (預設: 5)'
    )
    
    parser.add_argument(
        '-n', '--nodes',
        type=int,
        default=20,
        help='內部節點數量 (預設: 20)'
    )
    
    parser.add_argument(
        '--input-prefix',
        type=str,
        default='pi',
        help='輸入變數前綴 (預設: pi)'
    )
    
    parser.add_argument(
        '--output-prefix',
        type=str,
        default='po',
        help='輸出變數前綴 (預設: po)'
    )
    
    parser.add_argument(
        '--max-depth',
        type=int,
        default=3,
        help='表達式最大遞迴深度 (預設: 3)'
    )
    
    parser.add_argument(
        '--use-constants',
        action='store_true',
        help='在表達式中使用邏輯常數 0 和 1'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        default=None,
        help='隨機種子（用於可重現性）'
    )
    
    args = parser.parse_args()
    
    # 創建生成器
    generator = EqnGenerator(
        use_constants=args.use_constants,
        seed=args.seed
    )
    
    # 生成檔案
    generator.generate_eqn_file(
        output_file=args.output,
        num_inputs=args.inputs,
        num_outputs=args.outputs,
        num_internal_nodes=args.nodes,
        input_prefix=args.input_prefix,
        output_prefix=args.output_prefix,
        max_depth=args.max_depth
    )


if __name__ == '__main__':
    main()

