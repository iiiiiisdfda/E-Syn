import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
import joblib
import os
import argparse

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
    # 排除最后3列（power, area, delay），使用前面的列作为特征
    X = df.iloc[:, :-3].values
    # 保存特征名称用于后续绘图
    feature_names = df.columns[:-3].tolist()
    
    # 选择目标变量
    if args.target == 'area':
        y = df['area'].values
    else:
        y = df['delay'].values
    
    print(f"\nFeature shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    print(f"Target: {args.target}")
    print(f"Target statistics: mean={np.mean(y):.2f}, std={np.std(y):.2f}, min={np.min(y):.2f}, max={np.max(y):.2f}")
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    print(f"\nTrain set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    
    # 定义超参数网格
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [10, 20, 30, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 'log2', None],
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
    
    # 在全部数据上进行网格搜索（交叉验证会自动分割）
    grid_search.fit(X, y)
    
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
    
    # 绘制特征重要性
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance['feature'], feature_importance['importance'])
    plt.xlabel('Importance')
    plt.title('Random Forest Feature Importance')
    plt.tight_layout()
    plt.savefig('rf_feature_importance.png', dpi=300, bbox_inches='tight')
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
    fig.savefig('rf_permutation_importance.png', dpi=300, bbox_inches='tight')
    print("Permutation importance plot saved to 'rf_permutation_importance.png'")
    
    # 绘制预测 vs 真实值
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title(f'Random Forest Predictions vs True Values (R² = {test_r2:.4f})')
    plt.tight_layout()
    plt.savefig('rf_predictions.png', dpi=300, bbox_inches='tight')
    print("Predictions plot saved to 'rf_predictions.png'")
    
    # 保存模型
    model_filename = 'rf_best_model.pkl'
    joblib.dump({
        'model': best_model,
        'best_params': best_params,
        'feature_names': feature_names,
        'target': args.target,
        'input_dim': X.shape[1]
    }, model_filename)
    print(f"\nModel saved to '{model_filename}'")
    print("To load the model, use: joblib.load('rf_best_model.pkl')")
    
    print("\n" + "="*80)
    print("Training completed successfully!")
    print("="*80)

if __name__ == "__main__":
    main()

