import re

class CircuitParser:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.new_n_dict = {}

    def parse_circuit(self):
        with open(self.input_file_path, 'r') as f:
            lines = f.readlines()
        
        comments = lines[0].rstrip()
        lines = lines[1:]

        output = []
        in_order = ""
        out_order = ""
        current_line = ""
        for line in lines:
            line = line.strip()
            current_line += " " + line
            if line.endswith(";"):
                # Use strip() to handle cases where current_line has multiple leading spaces
                current_line_stripped = current_line.strip()
                if current_line_stripped.startswith("INORDER"):
                    in_order += current_line
                elif current_line_stripped.startswith("OUTORDER"):
                    out_order += current_line
                elif current_line_stripped.startswith("new_n"):
                    # Use split with maxsplit=1 to handle cases where expression might contain " = "
                    parts = current_line.split(" = ", 1)
                    if len(parts) == 2:
                        new_n_name = parts[0].strip()
                        new_n_expr = parts[1].strip().rstrip(";")
                        self.new_n_dict[new_n_name] = new_n_expr
                    else:
                        # If parsing fails, skip this line (shouldn't happen in valid eqn files)
                        print(f"Warning: Failed to parse new_n definition: {current_line_stripped}")
                else:
                    # 先保存输出节点，稍后处理
                    output.append(current_line)
                current_line = ""

        # Add INORDER and OUTORDER lines
        output.insert(0, in_order.strip())
        output.insert(1, out_order.strip())

        # 先展开中间节点定义（使用迭代方法，直到没有更多变化）
        max_expand_iterations = 20
        for expand_iter in range(max_expand_iterations):
            changed = False
            for key in list(self.new_n_dict.keys()):
                old_value = self.new_n_dict[key]
                # 只替换其他中间节点的引用，不替换自己
                new_value = self._replace_other_nodes(old_value, key)
                if new_value != old_value:
                    self.new_n_dict[key] = new_value
                    changed = True
            if not changed:
                break
        
        # 最后替换输出表达式中的中间节点
        output = [self.replace_new_n(line).lstrip() for line in output ]
        
        # Use split with maxsplit=1 to handle cases where expression might contain '='
        output[2:] = [self._format_output_line(expr) for expr in output[2:]]
        
        # for `!` replace to `! `
        output[2:] = [expr.replace("!", "! ") for expr in output[2:]]
        
        # 統一處理運算符 `*`, `+`, `^`，確保前後都有空格（與 generate_eqn.py 保持一致）
        # 標準化運算符周圍的空格：a*b -> a * b, a+b -> a + b, a^b -> a ^ b
        # 使用相同的正則表達式模式處理所有二元運算符
        output[2:] = [re.sub(r'\s*\*\s*', ' * ', expr) for expr in output[2:]]
        output[2:] = [re.sub(r'\s*\^\s*', ' ^ ', expr) for expr in output[2:]]
        output[2:] = [re.sub(r'\s*\+\s*', ' + ', expr) for expr in output[2:]]
        
        # 清理多餘的空格（但保留運算符周圍的單個空格）
        output[2:] = [re.sub(r'\s+', ' ', expr).strip() for expr in output[2:]]
        
        # insert comments in the beginning
        output.insert(0, comments)

        return "\n".join(output)

    def _replace_other_nodes(self, expr, exclude_key):
        """替换表达式中的其他中间节点引用（排除指定的键）"""
        # Sort keys by length (longest first) to avoid partial matches
        # e.g., replace "new_n10_" before "new_n1_" to avoid matching part of "new_n10_"
        sorted_keys = sorted([k for k in self.new_n_dict.keys() if k != exclude_key], 
                              key=len, reverse=True)
        
        for key in sorted_keys:
            if key in expr:
                # Use a pattern that matches the node name as a whole word
                # Since node names may end with '_', we need to match word boundaries correctly
                # Pattern: word boundary or start of string, then escaped key, then word boundary or end of string or non-word char
                pattern = r'(?<!\w)' + re.escape(key) + r'(?!\w)'
                expr = re.sub(pattern, "(" + self.new_n_dict[key] + ")", expr)
        return expr
    
    def replace_new_n(self, expr):
        """替换表达式中的所有中间节点引用"""
        max_iterations = 20  # 防止无限循环
        iteration = 0
        changed = True
        
        # Sort keys by length (longest first) to avoid partial matches
        # e.g., replace "new_n10_" before "new_n1_" to avoid matching part of "new_n10_"
        sorted_keys = sorted(self.new_n_dict.keys(), key=len, reverse=True)
        
        while changed and iteration < max_iterations:
            changed = False
            iteration += 1
            for key in sorted_keys:
                if key in expr:
                    # Use a pattern that matches the node name as a whole word
                    # Since node names may end with '_', we need to match word boundaries correctly
                    # Pattern: negative lookbehind for word char, then escaped key, then negative lookahead for word char
                    pattern = r'(?<!\w)' + re.escape(key) + r'(?!\w)'
                    new_expr = re.sub(pattern, "(" + self.new_n_dict[key] + ")", expr)
                    if new_expr != expr:
                        expr = new_expr
                        changed = True
        
        if iteration >= max_iterations:
            # 如果达到最大迭代次数，警告但继续处理
            print(f"Warning: Maximum iterations ({max_iterations}) reached in replace_new_n. Some nodes may not be fully expanded.")
        
        return expr
    
    def _format_output_line(self, expr):
        """格式化输出行，处理可能包含多个'='的情况"""
        # Use split with maxsplit=1 to handle cases where expression might contain '='
        parts = expr.split('=', 1)
        if len(parts) == 2:
            expr_name = parts[0].strip()
            expr_value = parts[1].strip().rstrip(';')
            return f"{expr_name} = ({expr_value});"
        else:
            # If no '=' found, return as is (shouldn't happen in valid eqn files)
            return expr

    def write_to_file(self, content):
        with open(self.output_file_path, 'w') as f:
            f.write(content)

    def process(self):
        parsed_content = self.parse_circuit()
        self.write_to_file(parsed_content)


# input_file_path = "/data/guangyuh/coding_env/E-Brush/test_data/raw_circuit.txt"
# output_file_path = "/data/guangyuh/coding_env/E-Brush/test_data/original_circuit.txt"

# parser = CircuitParser(input_file_path, output_file_path)
# parser.process()