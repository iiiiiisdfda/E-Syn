"""
使用训练好的 PySR 模型进行预测

用法:
    python use_model.py --model-file outputs/20251219_171406_Bfkbrm/checkpoint.pkl --input mig_circuit_analysis.csv
    python use_model.py --model-file outputs/20251219_171406_Bfkbrm/checkpoint.pkl --features "11,173,172,584,25"
"""

from pysr import PySRRegressor
import pandas as pd
import numpy as np
import sympy
import argparse
from sklearn.preprocessing import StandardScaler

def load_model(model_file):
    """加载训练好的模型"""
    model = PySRRegressor.from_file(model_file)
    model.set_params(extra_sympy_mappings={"cos2": lambda x: sympy.cos(x)**2})
    model.refresh()
    return model

def predict_from_csv(model_file, csv_file):
    """从 CSV 文件读取数据并预测"""
    # 加载模型
    model = load_model(model_file)
    
    # 读取数据
    df = pd.read_csv(csv_file)
    
    # 提取特征（与训练时相同）
    X = df.iloc[:, [0, 1, 2, 4, 5]].to_numpy()  # +, !, *, ASTSize, ASTDepth
    
    # 标准化（需要与训练时使用相同的 scaler）
    # 注意：实际使用时应该保存训练时的 scaler，这里简化处理
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 预测
    predictions = model.predict(X_scaled)
    
    # 显示结果
    print(f"\n预测结果（共 {len(predictions)} 条）:")
    print("-" * 80)
    print(f"{'索引':<6} {'实际 delay':<15} {'预测 delay':<15} {'误差':<15} {'误差%':<15}")
    print("-" * 80)
    
    actual = df.iloc[:, -1].to_numpy()  # delay
    for i in range(len(predictions)):
        error = abs(actual[i] - predictions[i])
        error_pct = (error / actual[i]) * 100 if actual[i] != 0 else 0
        print(f"{i:<6} {actual[i]:<15.2f} {predictions[i]:<15.2f} {error:<15.2f} {error_pct:<15.2f}")
    
    # 统计信息
    mse = np.mean((actual - predictions)**2)
    mae = np.mean(np.abs(actual - predictions))
    mape = 100 * np.mean(np.abs((actual - predictions) / actual))
    rrse = np.sqrt(np.sum((actual - predictions)**2) / np.sum((actual - np.mean(actual))**2))
    
    print("-" * 80)
    print(f"\n评估指标:")
    print(f"  MSE:  {mse:.4f}")
    print(f"  MAE:  {mae:.4f}")
    print(f"  MAPE: {mape:.2f}%")
    print(f"  RRSE: {rrse:.4f}")
    
    return predictions

def predict_from_features(model_file, features_str):
    """从特征值字符串预测"""
    # 加载模型
    model = load_model(model_file)
    
    # 解析特征
    features = [float(x.strip()) for x in features_str.split(',')]
    if len(features) != 5:
        raise ValueError(f"需要 5 个特征值（+, !, *, ASTSize, ASTDepth），但提供了 {len(features)} 个")
    
    X = np.array([features])
    
    # 标准化（简化处理，实际应该使用训练时的 scaler）
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 预测
    prediction = model.predict(X_scaled)[0]
    
    print(f"\n输入特征:")
    print(f"  + (OR):        {features[0]}")
    print(f"  ! (NOT):       {features[1]}")
    print(f"  * (AND):       {features[2]}")
    print(f"  ASTSize:       {features[3]}")
    print(f"  ASTDepth:      {features[4]}")
    print(f"\n预测 delay: {prediction:.4f}")
    
    # 显示最佳方程
    print(f"\n使用的方程:")
    print(f"  LaTeX: {model.latex()}")
    print(f"  SymPy: {model.sympy()}")
    
    return prediction

def show_model_info(model_file):
    """显示模型信息"""
    model = load_model(model_file)
    
    print(f"\n模型信息:")
    print(f"  文件: {model_file}")
    print(f"  最佳方程 (LaTeX): {model.latex()}")
    print(f"  最佳方程 (SymPy): {model.sympy()}")
    print(f"\n所有发现的方程:")
    
    # 读取 hall_of_fame.csv（如果存在）
    import os
    model_dir = os.path.dirname(model_file)
    hall_of_fame = os.path.join(model_dir, "hall_of_fame.csv")
    if os.path.exists(hall_of_fame):
        df = pd.read_csv(hall_of_fame)
        print(f"\n{'复杂度':<10} {'损失':<15} {'方程'}")
        print("-" * 100)
        for idx, row in df.tail(10).iterrows():  # 显示最后 10 个（最复杂的）
            eq = row['Equation'][:80] + "..." if len(row['Equation']) > 80 else row['Equation']
            print(f"{row['Complexity']:<10} {row['Loss']:<15.4f} {eq}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="使用训练好的 PySR 模型进行预测")
    parser.add_argument('--model-file', type=str, required=True, help='模型文件路径 (checkpoint.pkl)')
    parser.add_argument('--input', type=str, default=None, help='输入 CSV 文件路径')
    parser.add_argument('--features', type=str, default=None, help='特征值（逗号分隔）：+,!,*,ASTSize,ASTDepth')
    parser.add_argument('--info', action='store_true', help='只显示模型信息')
    
    args = parser.parse_args()
    
    if args.info:
        show_model_info(args.model_file)
    elif args.input:
        predict_from_csv(args.model_file, args.input)
    elif args.features:
        predict_from_features(args.model_file, args.features)
    else:
        print("请指定 --input CSV文件 或 --features 特征值")
        print("\n示例:")
        print("  python use_model.py --model-file outputs/.../checkpoint.pkl --input mig_circuit_analysis.csv")
        print("  python use_model.py --model-file outputs/.../checkpoint.pkl --features '11,173,172,584,25'")
        print("  python use_model.py --model-file outputs/.../checkpoint.pkl --info")



