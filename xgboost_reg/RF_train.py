import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
import os
import argparse
import m2cgen as m2c

# 评估指标函数（与 train.py 保持一致）
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))

def r(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]

def main():
    parser = argparse.ArgumentParser(description='Train Random Forest model')
    parser.add_argument('--data', type=str, default='../sym_reg/feature1/10000.csv', help='Path to data file')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    args = parser.parse_args()
    
    # 读取数据
    data_path = args.data
    if not os.path.exists(data_path):
        alternative_paths = [
            '../sym_reg/mig_circuit_analysis.csv',
            '../sym_reg/simple_circuit_analysis_large.csv',
            'data.csv'
        ]
        for alt_path in alternative_paths:
            if os.path.exists(alt_path):
                data_path = alt_path
                print(f"Using alternative data path: {data_path}")
                break
        else:
            print(f"Error: Data file not found.")
            return
    
    df = pd.read_csv(data_path)
    print(f"Data shape: {df.shape}")
    print(f"Data columns: {df.columns.tolist()}")
    
    # 提取特征和目标
    # 明确排除目标变量和相关列，避免数据泄漏
    # 排除：lev, power, area, delay, gates, cap, and_gates
    exclude_cols = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
    # 只保留存在的列（避免某些列不存在时报错）
    exclude_cols = [col for col in exclude_cols if col in df.columns]
    feature_cols = [col for col in df.columns if col not in exclude_cols]
    
    print(f"\nExcluded columns: {exclude_cols}")
    print(f"Final feature count: {len(feature_cols)}")
    print(f"Feature columns: {feature_cols}")
    
    X = df[feature_cols].values
    # 保存特征名称用于后续绘图
    feature_names = feature_cols
    
    # 选择目标变量
    if args.target == 'area':
        y = df['area'].values
    else:
        y = df['delay'].values
    
    print(f"\nFeature shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    print(f"Target: {args.target}")
    print(f"Target statistics: mean={np.mean(y):.2f}, std={np.std(y):.2f}, min={np.min(y):.2f}, max={np.max(y):.2f}")
    
    # 限制数据量：最多使用 50000 条（40000 训练 + 10000 验证）
    # 注意：测试集（5000）应从原始数据集中单独划分，不在此处理
    max_total_samples = 50000
    max_train_samples = 40000
    max_val_samples = 10000
    
    if len(X) > max_total_samples:
        print(f"\n⚠️  Data has {len(X)} samples, limiting to {max_total_samples} samples")
        # 打乱数据
        indices = np.random.RandomState(seed=42).permutation(len(X))
        selected_indices = indices[:max_total_samples]
        X = X[selected_indices]
        y = y[selected_indices]
        print(f"   Using {len(X)} samples for training and validation")
    
    # 分割数据集
    # 确保训练集最多 40000，验证集 10000
    if len(X) >= max_total_samples:
        # 如果数据足够，使用固定数量
        train_size = max_train_samples
        X_train = X[:train_size]
        X_test = X[train_size:train_size+max_val_samples]
        y_train = y[:train_size]
        y_test = y[train_size:train_size+max_val_samples]
    else:
        # 如果数据不足，按比例分割
        val_ratio = max_val_samples / len(X) if len(X) > max_val_samples else 0.2
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=val_ratio, random_state=42
        )
        # 限制训练集大小
        if len(X_train) > max_train_samples:
            X_train = X_train[:max_train_samples]
            y_train = y_train[:max_train_samples]
    
    print(f"\nTrain set: {X_train.shape[0]} samples")
    print(f"Validation set: {X_test.shape[0]} samples")
    
    # 定义超参数网格（简化，与 XGBoost 风格一致）
    param_grid = {
        'n_estimators': [100, 160, 200],  # 与 XGBoost 一致
        'max_depth': [3, 5, 10],  # 与 XGBoost 一致
        'random_state': [42],
        'n_jobs': [-1]
    }
    
    # 创建模型
    model = RandomForestRegressor()
    
    # 使用 KFold 交叉验证进行网格搜索
    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    print("\nStarting GridSearchCV with Random Forest...")
    print(f"Total parameter combinations: {np.prod([len(v) for v in param_grid.values()])}")
    
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring='neg_mean_absolute_percentage_error',
        cv=kf,
        verbose=1,
        n_jobs=-1
    )
    
    # 在训练集上进行网格搜索（交叉验证会自动分割），避免数据泄漏
    grid_search.fit(X_train, y_train)
    
    # 获取最佳参数
    best_params = grid_search.best_params_
    print("\n" + "="*80)
    print("Best parameters found:")
    print("="*80)
    for param, value in best_params.items():
        print(f"  {param}: {value}")
    
    # 使用最佳参数在训练集上训练最终模型
    print("\nTraining final model with best parameters on training set...")
    best_model = RandomForestRegressor(**best_params)
    best_model.fit(X_train, y_train)
    
    # 在测试集上评估
    y_pred = best_model.predict(X_test)
    
    # 计算评估指标
    test_mape = mape(y_test, y_pred)
    test_rrse = rrse(y_test, y_pred)
    test_r = r(y_test, y_pred)
    test_r2 = r2_score(y_test, y_pred)
    test_mae = mean_absolute_error(y_test, y_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print("\n" + "="*80)
    print("Test Set Evaluation Metrics:")
    print("="*80)
    print(f"Mean Absolute Percentage Error (MAPE): {test_mape:.4f}%")
    print(f"Root Relative Square Error (RRSE): {test_rrse:.4f}")
    print(f"Correlation Coefficient (R): {test_r:.4f}")
    print(f"Coefficient of Determination (R²): {test_r2:.4f}")
    print(f"Mean Absolute Error (MAE): {test_mae:.4f}")
    print(f"RMSE (Root Mean Squared Error): {test_rmse:.4f}")
    print("="*80)
    
    # 特征重要性（基于 Gini 不纯度）
    print("\nFeature Importance (based on Gini impurity):")
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': best_model.feature_importances_
    }).sort_values('importance', ascending=False)
    print(feature_importance)
    
    # 创建输出文件夹
    output_dir = f'rf_data'
    os.makedirs(output_dir, exist_ok=True)
    
    # 绘制特征重要性
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance['feature'], feature_importance['importance'])
    plt.xlabel('Importance')
    plt.title('Random Forest Feature Importance')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'rf_feature_importance_{args.target}.png'), dpi=300, bbox_inches='tight')
    print("\nFeature importance plot saved to 'rf_feature_importance.png'")
    
    # Permutation Importance
    print("\nComputing permutation importance...")
    perm_result = permutation_importance(
        best_model, X_train, y_train, n_repeats=10, random_state=42, n_jobs=-1
    )
    
    # 排序重要性
    sorted_importances_idx = perm_result.importances_mean.argsort()
    df_columns_sorted = [feature_names[i] for i in sorted_importances_idx]
    
    # 创建 DataFrame 用于绘图
    importances = pd.DataFrame(
        perm_result.importances[sorted_importances_idx].T,
        columns=df_columns_sorted,
    )
    
    # 绘制 Permutation Importance
    fig, ax = plt.subplots(figsize=(10, 6))
    importances.plot.box(vert=False, whis=10, ax=ax)
    ax.set_title("Permutation Importances (train set)")
    ax.axvline(x=0, color="k", linestyle="--")
    ax.set_xlabel("Decrease in accuracy score")
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, f'rf_permutation_importance_{args.target}.png'), dpi=300, bbox_inches='tight')
    print("Permutation importance plot saved to 'rf_permutation_importance.png'")
    
    # 保存 Permutation Importance 为 CSV
    perm_importance_df = pd.DataFrame({
        'feature': df_columns_sorted,
        'importance_mean': perm_result.importances_mean[sorted_importances_idx],
        'importance_std': perm_result.importances_std[sorted_importances_idx]
    })
    perm_importance_df = perm_importance_df.sort_values('importance_mean', ascending=False)
    perm_csv_filename = os.path.join(output_dir, f'rf_permutation_importance_{args.target}.csv')
    perm_importance_df.to_csv(perm_csv_filename, index=False)
    print(f"Permutation importance CSV saved to '{perm_csv_filename}'")
    
    # 绘制预测 vs 真实值
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title(f'Random Forest Predictions vs True Values (R² = {test_r2:.4f})')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'rf_predictions_{args.target}.png'), dpi=300, bbox_inches='tight')
    print("Predictions plot saved to 'rf_predictions.png'")
    
    # 导出为 Rust 代码（用于 Rust 项目）
    try:
        print("\nExporting model to Rust code...")
        code = m2c.export_to_rust(best_model)
        
        # write code in rf_model.rs
        rust_filename = os.path.join(output_dir, f'rf_model_{args.target}.rs')
        with open(rust_filename, 'w') as f:
            f.write(code)
        print(f"Rust code exported to '{rust_filename}'")
    except Exception as e:
        print(f"Warning: Could not export to Rust code: {e}")
    
    # 导出为 Python 代码（用于 Python 加载）
    try:
        print("\nExporting model to Python code...")
        py_code = m2c.export_to_python(best_model)
        
        # write code in rf_model.py
        py_filename = os.path.join(output_dir, f'rf_model_{args.target}.py')
        with open(py_filename, 'w') as f:
            f.write(py_code)
        print(f"Python code exported to '{py_filename}'")
    except Exception as e:
        print(f"Warning: Could not export to Python code: {e}")
    
    print("\n" + "="*80)
    print("Training completed successfully!")
    print("="*80)

if __name__ == "__main__":
    main()

