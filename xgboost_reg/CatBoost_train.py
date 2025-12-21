import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
import m2cgen as m2c
import os
import argparse
import joblib

# 评估指标函数（与 train.py 保持一致）
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))

def r(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]

def main():
    parser = argparse.ArgumentParser(description='Train CatBoost model')
    parser.add_argument('--data', type=str, default='../sym_reg/feature1/10000.csv', help='Path to data file')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    args = parser.parse_args()
    
    # 读取数据
    data_path = args.data
    if not os.path.exists(data_path):
        alternative_paths = [
            '../sym_reg/new_50000.csv',
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
    
    # 使用 DataFrame 而不是 values，这样 CatBoost 可以使用特征名称，避免警告
    X_df = df[feature_cols]
    # 保存特征名称用于后续绘图
    feature_names = feature_cols
    
    # 选择目标变量
    if args.target == 'area':
        y = df['area'].values
    else:
        y = df['delay'].values
    
    print(f"\nFeature shape: {X_df.shape}")
    print(f"Target shape: {y.shape}")
    print(f"Target: {args.target}")
    print(f"Target statistics: mean={np.mean(y):.2f}, std={np.std(y):.2f}, min={np.min(y):.2f}, max={np.max(y):.2f}")
    
    # 分割数据集（使用 DataFrame）
    X_train, X_test, y_train, y_test = train_test_split(X_df, y, test_size=0.2, random_state=42)
    print(f"\nTrain set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    
    # 定义超参数网格（简化，与 XGBoost 一致）
    param_grid = {
        'iterations': [100, 160, 200],  # 对应 XGBoost 的 n_estimators
        'depth': [3, 5, 10],  # 对应 XGBoost 的 max_depth
        'learning_rate': [0.01, 0.1, 0.2],  # 与 XGBoost 一致
        'random_state': [42],
        'verbose': [False],  # 减少输出
        'thread_count': [-1]  # 使用所有 CPU 核心
    }
    
    # 创建模型，禁用文件写入以避免并行冲突
    model = CatBoostRegressor(allow_writing_files=False)
    
    # 使用 KFold 交叉验证进行网格搜索
    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    print("\nStarting GridSearchCV with CatBoost...")
    print(f"Total parameter combinations: {np.prod([len(v) for v in param_grid.values()])}")
    
    # 减少并行度以避免文件写入冲突
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring='neg_mean_absolute_percentage_error',
        cv=kf,
        verbose=1,
        n_jobs=4  # 减少并行度，避免文件冲突
    )
    
    # 在训练集上进行网格搜索（交叉验证会自动分割），避免数据泄漏
    grid_search.fit(X_train, y_train)
    
    # 获取最佳参数
    best_params = grid_search.best_params_
    # sklearn 的 neg_mean_absolute_percentage_error 返回负数的小数形式（0-1），需要转换为百分比
    best_cv_mape = -grid_search.best_score_ * 100
    print("\n" + "="*80)
    print("Best parameters found:")
    print("="*80)
    for param, value in best_params.items():
        print(f"  {param}: {value}")
    print(f"\nBest Cross-Validation MAPE: {best_cv_mape:.2f}%")
    
    # 使用最佳参数在训练集上训练最终模型
    print("\nTraining final model with best parameters on training set...")
    # 从 best_params 中移除 allow_writing_files（如果存在），然后单独设置
    final_params = {k: v for k, v in best_params.items() if k != 'allow_writing_files'}
    best_model = CatBoostRegressor(**final_params, allow_writing_files=True)  # 最终训练时可以写入文件
    best_model.fit(X_train, y_train, verbose=False)
    
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
    
    # Permutation Importance
    # 注意：permutation_importance 需要数组格式，所以转换为 values
    print("\nComputing permutation importance...")
    perm_result = permutation_importance(
        best_model, X_train.values, y_train, n_repeats=10, random_state=42, n_jobs=-1
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
    ax.set_title("CatBoost Permutation Importances (train set)")
    ax.axvline(x=0, color="k", linestyle="--")
    ax.set_xlabel("Decrease in accuracy score")
    fig.tight_layout()
    fig.savefig('catboost_permutation_importance.png', dpi=300, bbox_inches='tight')
    print("Permutation importance plot saved to 'catboost_permutation_importance.png'")
    
    # 绘制预测 vs 真实值
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title(f'CatBoost Predictions vs True Values (R² = {test_r2:.4f})')
    plt.tight_layout()
    plt.savefig('catboost_predictions.png', dpi=300, bbox_inches='tight')
    print("Predictions plot saved to 'catboost_predictions.png'")
    
    # 保存模型
    model_filename = 'catboost_best_model.pkl'
    joblib.dump({
        'model': best_model,
        'best_params': best_params,
        'feature_names': feature_names,
        'target': args.target,
        'input_dim': X_train.shape[1]
    }, model_filename)
    print(f"\nModel saved to '{model_filename}'")
    print("To load the model, use: joblib.load('catboost_best_model.pkl')")
    
    # 导出为 Rust 代码（用于 Rust 项目）
    try:
        print("\nExporting model to Rust code...")
        code = m2c.export_to_rust(best_model)
        
        # write code in catboost_model.rs
        with open('catboost_model.rs', 'w') as f:
            f.write(code)
        print("Rust code exported to 'catboost_model.rs'")
    except Exception as e:
        print(f"Warning: Could not export to Rust code: {e}")
    
    print("\n" + "="*80)
    print("Training completed successfully!")
    print("="*80)

if __name__ == "__main__":
    main()

