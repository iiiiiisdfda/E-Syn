#!/usr/bin/env python3
"""
测试 CircuitParser_simple.py
验证运算符处理是否正确
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from CircuitParser_simple import CircuitParser

def test_operators():
    """测试运算符处理"""
    
    # 创建测试文件
    test_input = """# Test circuit
INORDER = pi00 pi01 pi02;
OUTORDER = po00;

new_n1_ = pi00 * pi01;
new_n2_ = pi01 + pi02;
new_n3_ = pi00 ^ pi01;
new_n4_ = pi00 & pi01;
new_n5_ = !pi00 * pi01;

po00 = new_n1_ * new_n2_ + new_n3_ ^ new_n4_ & !new_n5_;
"""
    
    with open("test_simple_input.eqn", "w") as f:
        f.write(test_input)
    
    # 处理文件
    parser = CircuitParser("test_simple_input.eqn", "test_simple_output.eqn")
    parser.process()
    
    # 读取结果
    with open("test_simple_output.eqn", "r") as f:
        result = f.read()
    
    print("=" * 80)
    print("测试结果")
    print("=" * 80)
    print("\n输入文件:")
    print(test_input)
    print("\n输出文件:")
    print(result)
    
    # 检查运算符格式
    print("\n运算符格式检查:")
    checks = [
        ("!", "! " in result, "! 运算符应该有空格"),
        (" * ", " * " in result, "* 运算符前后应该有空格"),
        (" + ", " + " in result, "+ 运算符前后应该有空格"),
        (" ^ ", " ^ " in result, "^ 运算符前后应该有空格"),
        (" & ", " & " in result, "& 运算符前后应该有空格"),
    ]
    
    all_passed = True
    for op, check, desc in checks:
        status = "✓" if check else "✗"
        print(f"  {status} {desc}")
        if not check:
            all_passed = False
    
    # 清理
    if os.path.exists("test_simple_input.eqn"):
        os.remove("test_simple_input.eqn")
    if os.path.exists("test_simple_output.eqn"):
        os.remove("test_simple_output.eqn")
    
    if all_passed:
        print("\n✓ 所有测试通过！")
    else:
        print("\n✗ 部分测试失败")
    
    return all_passed

if __name__ == "__main__":
    test_operators()




