import pandas as pd
import os

def remove_and_column(csv_file):
    """删除 CSV 文件中的 & 列"""
    if not os.path.exists(csv_file):
        print(f"Error: File {csv_file} not found")
        return False
    
    print(f"Processing {csv_file}...")
    
    # 读取 CSV 文件
    df = pd.read_csv(csv_file)
    
    # 检查 & 列是否存在
    if '&' not in df.columns:
        print(f"  Warning: '&' column not found in {csv_file}")
        return False
    
    # 删除 & 列
    df = df.drop(columns=['&'])
    
    # 保存文件（覆盖原文件）
    df.to_csv(csv_file, index=False)
    
    print(f"  ✓ Removed '&' column from {csv_file}")
    print(f"  New columns: {', '.join(df.columns.tolist())}")
    print(f"  Shape: {df.shape}")
    
    return True

def main():
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 要处理的文件列表
    csv_files = [
        '1000.csv',
        '10000.csv'
    ]
    
    print("="*60)
    print("Removing '&' column from CSV files")
    print("="*60)
    
    success_count = 0
    for csv_file in csv_files:
        file_path = os.path.join(script_dir, csv_file)
        if remove_and_column(file_path):
            success_count += 1
        print()
    
    print("="*60)
    print(f"Completed: {success_count}/{len(csv_files)} files processed")
    print("="*60)

if __name__ == "__main__":
    main()

