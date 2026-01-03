#!/usr/bin/env python3
"""
CSV文件分割工具
按照 10:1:2 的比例将CSV文件分成两份：
- 训练集+验证集（10+1=11份）
- 测试集（2份）
"""

import pandas as pd
import argparse
import os
from pathlib import Path


def split_csv(input_file, output_prefix=None, ratio=(10, 1, 2), shuffle=True, random_state=42):
    """
    将CSV文件按照指定比例分成两份：
    - 训练集+验证集（前两部分合并）
    - 测试集（第三部分）
    
    Args:
        input_file: 输入的CSV文件路径
        output_prefix: 输出文件前缀（如果不指定，使用输入文件名）
        ratio: 分割比例，默认为 (10, 1, 2)，表示训练:验证:测试
        shuffle: 是否在分割前打乱数据，默认为True
        random_state: 随机种子，默认为42
    """
    # 读取CSV文件
    print(f"正在读取文件: {input_file}")
    df = pd.read_csv(input_file)
    total_rows = len(df)
    print(f"总行数: {total_rows}")
    
    # 如果指定了打乱，则打乱数据
    if shuffle:
        print("正在打乱数据...")
        df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
    
    # 计算比例
    ratio_sum = sum(ratio)
    ratio_1 = ratio[0] / ratio_sum
    ratio_2 = ratio[1] / ratio_sum
    ratio_3 = ratio[2] / ratio_sum
    
    # 计算每份的数量
    n1 = int(total_rows * ratio_1)
    n2 = int(total_rows * ratio_2)
    n3 = total_rows - n1 - n2  # 剩余的全部给第三份，避免舍入误差
    
    print(f"\n分割比例: {ratio[0]}:{ratio[1]}:{ratio[2]}")
    print(f"第一份: {n1} 行 ({n1/total_rows*100:.2f}%)")
    print(f"第二份: {n2} 行 ({n2/total_rows*100:.2f}%)")
    print(f"第三份: {n3} 行 ({n3/total_rows*100:.2f}%)")
    
    # 分割数据
    df1 = df.iloc[:n1]              # 训练集（10份）
    df2 = df.iloc[n1:n1+n2]         # 验证集（1份）
    df3 = df.iloc[n1+n2:]           # 测试集（2份）
    
    # 合并训练集和验证集
    df_train_val = pd.concat([df1, df2], ignore_index=True)
    
    # 确定输出文件名
    if output_prefix is None:
        input_path = Path(input_file)
        output_prefix = input_path.stem
    
    output_dir = Path(input_file).parent
    output_file_train_val = output_dir / f"{output_prefix}_train_val.csv"  # 训练集+验证集（11份）
    output_file_test = output_dir / f"{output_prefix}_test.csv"            # 测试集（2份）
    
    # 保存文件
    print(f"\n正在保存文件...")
    df_train_val.to_csv(output_file_train_val, index=False)
    print(f"✓ 训练集+验证集已保存: {output_file_train_val} ({len(df_train_val)} 行)")
    
    df3.to_csv(output_file_test, index=False)
    print(f"✓ 测试集已保存: {output_file_test} ({len(df3)} 行)")
    
    print(f"\n分割完成！")
    print(f"训练集+验证集: {len(df_train_val)} 行 ({len(df_train_val)/total_rows*100:.2f}%)")
    print(f"测试集: {len(df3)} 行 ({len(df3)/total_rows*100:.2f}%)")
    return output_file_train_val, output_file_test


def main():
    parser = argparse.ArgumentParser(
        description='将CSV文件按照 10:1:2 的比例分成两份（训练集+验证集:测试集）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python split.py data.csv
  python split.py data.csv --output-prefix mydata
  python split.py data.csv --no-shuffle
  python split.py data.csv --ratio 8 1 1
        """
    )
    
    parser.add_argument('input_file', type=str, help='输入的CSV文件路径')
    parser.add_argument('--output-prefix', '-o', type=str, default=None,
                        help='输出文件前缀（默认使用输入文件名）')
    parser.add_argument('--ratio', '-r', type=int, nargs=3, default=[10, 1, 2],
                        metavar=('R1', 'R2', 'R3'),
                        help='分割比例，默认为 10:1:2')
    parser.add_argument('--no-shuffle', action='store_true',
                        help='不打乱数据（默认会打乱）')
    parser.add_argument('--random-state', type=int, default=42,
                        help='随机种子，默认为42')
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.exists(args.input_file):
        print(f"错误: 文件不存在: {args.input_file}")
        return 1
    
    # 执行分割
    try:
        split_csv(
            input_file=args.input_file,
            output_prefix=args.output_prefix,
            ratio=tuple(args.ratio),
            shuffle=not args.no_shuffle,
            random_state=args.random_state
        )
        return 0
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())

