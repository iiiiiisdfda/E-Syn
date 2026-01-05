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
                if current_line.startswith(" INORDER"):
                    in_order += current_line
                elif current_line.startswith(" OUTORDER"):
                    out_order += current_line
                elif current_line.startswith(" new_n"):
                    new_n_name, new_n_expr = current_line.split(" = ")
                    self.new_n_dict[new_n_name.strip()] = new_n_expr.strip(";")
                else:
                    output.append(self.replace_new_n(current_line))
                current_line = ""

        # Add INORDER and OUTORDER lines
        output.insert(0, in_order.strip())
        output.insert(1, out_order.strip())

        for key in self.new_n_dict:
            self.new_n_dict[key] = self.replace_new_n(self.new_n_dict[key])

        output = [self.replace_new_n(line).lstrip() for line in output ]
        
        output[2:] = [f"{expr.split('=')[0]} = ({expr.split('=')[1].replace(';', '')});" for expr in output[2:]]
        
        # 处理运算符：模仿原始版本的方式，使用简单字符串替换
        # 与原始版本相同，只使用 replace() 方法，不使用正则表达式
        
        # 1. 处理 `!` 替换为 `! `（与原始版本完全相同）
        output[2:] = [expr.replace("!", "! ") for expr in output[2:]]
        
        # 2. 处理 `*` 运算符：确保前后有空格
        # 替换模式：`*` -> ` * `（简单替换，与原始版本风格一致）
        output[2:] = [expr.replace("*", " * ") for expr in output[2:]]
        
        # 3. 处理 `+` 运算符：确保前后有空格
        output[2:] = [expr.replace("+", " + ") for expr in output[2:]]
        
        # 4. 处理 `^` 运算符：确保前后有空格
        output[2:] = [expr.replace("^", " ^ ") for expr in output[2:]]
        
        # 5. 处理 `&` 运算符：确保前后有空格
        output[2:] = [expr.replace("&", " & ") for expr in output[2:]]
        
        # 6. 清理多余空格：将多个连续空格替换为单个空格（模仿原始版本的简单方式）
        # 多次替换以确保清理所有多余空格
        for _ in range(5):  # 最多5次应该足够
            output[2:] = [expr.replace("  ", " ") for expr in output[2:]]
        
        # 7. 最终清理：移除行首行尾空格
        output[2:] = [expr.strip() for expr in output[2:]]
        
        # insert comments in the beginning
        output.insert(0, comments)

        return "\n".join(output)

    def replace_new_n(self, expr):
        for key in self.new_n_dict:
            expr = expr.replace(key, "("+self.new_n_dict[key]+")")
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

