import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
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
    parser = argparse.ArgumentParser(description='Quick train and test Random Forest model')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    parser.add_argument('--train', action='store_true', help='Train model (if not set, only test)')
    args = parser.parse_args()
    
    # 读取数据
    data_path = '../sym_reg/1000.csv'
    
    df = pd.read_csv(data_path)
    print(f"Data shape: {df.shape}")
    
    # 提取特征和目标
    # 排除最后3列（power, area, delay），使用前面的列作为特征
    X = df.iloc[:, :-3].values
    feature_names = df.columns[:-3].tolist()
    
    # 选择目标变量
    if args.target == 'area':
        y = df['area'].values
    else:
        y = df['delay'].values
    
    print(f"Target: {args.target}")
    print(f"Feature shape: {X.shape}, Target shape: {y.shape}")
    
    model_path = 'rf_best_model.pkl'
    
    # 训练模式
    if args.train or not os.path.exists(model_path):
        print("\n" + "="*60)
        print("Training Random Forest Model (Quick Version)")
        print("="*60)
        
        # 分割数据集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
        print(f"Train set: {X_train.shape[0]} samples")
        print(f"Test set: {X_test.shape[0]} samples")
        
        # 轻量化的超参数网格（快速训练）
        param_grid = {
            'n_estimators': [100, 200],  # 只测试 2 个选项
            'max_depth': [20, None],  # 只测试 2 个选项
            'min_samples_split': [2, 5],  # 只测试 2 个选项
            'min_samples_leaf': [1, 2],  # 只测试 2 个选项
            'max_features': ['sqrt', None],  # 只测试 2 个选项
            'random_state': [42],
            'n_jobs': [-1]
        }
        # 总组合数：2 × 2 × 2 × 2 × 2 = 32 种组合
        
        # 使用较少的交叉验证折数以加快速度
        n_splits = 3  # 从 10 折减少到 3 折
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
        
        total_combinations = np.prod([len(v) for v in param_grid.values()])
        total_fits = total_combinations * n_splits
        
        print(f"\nGridSearchCV settings:")
        print(f"  Parameter combinations: {total_combinations}")
        print(f"  Cross-validation folds: {n_splits}")
        print(f"  Total fits: {total_fits}")
        print(f"  (This is much faster than full training)")
        
        model = RandomForestRegressor()
        grid_search = GridSearchCV(
            estimator=model,
            param_grid=param_grid,
            scoring='neg_mean_absolute_percentage_error',
            cv=kf,
            verbose=1,
            n_jobs=-1
        )
        
        print("\nStarting GridSearchCV...")
        grid_search.fit(X_train, y_train)
        
        # 获取最佳参数
        best_params = grid_search.best_params_
        print("\nBest parameters found:")
        for param, value in best_params.items():
            print(f"  {param}: {value}")
        
        # 使用最佳参数训练最终模型
        best_model = RandomForestRegressor(**best_params)
        best_model.fit(X_train, y_train)
        
        # 在测试集上评估
        y_pred_test = best_model.predict(X_test)
        test_mape = mape(y_test, y_pred_test)
        test_r2 = r2_score(y_test, y_pred_test)
        
        print(f"\nTest set performance (quick evaluation):")
        print(f"  MAPE: {test_mape:.4f}%")
        print(f"  R²:   {test_r2:.4f}")
        
        # 保存模型
        joblib.dump({
            'model': best_model,
            'best_params': best_params,
            'feature_names': feature_names,
            'target': args.target,
            'input_dim': X.shape[1]
        }, model_path)
        print(f"\n✓ Model saved to '{model_path}'")
    
    # 测试模式（使用全部数据）
    if os.path.exists(model_path):
        print("\n" + "="*60)
        print("Testing Random Forest Model")
        print("="*60)
        
        print(f"Loading model from {model_path}...")
        checkpoint = joblib.load(model_path)
        model = checkpoint['model']
        target = checkpoint.get('target', args.target)
        
        print(f"✓ Model loaded successfully")
        print(f"Target variable: {target}")
        
        # 使用全部数据作为测试集（轻量化快速测试）
        print(f"\nEvaluating on all data ({len(X)} samples)...")
        y_pred = model.predict(X)
        
        # 计算评估指标
        test_mape = mape(y, y_pred)
        test_rrse = rrse(y, y_pred)
        test_r = r(y, y_pred)
        test_r2 = r2_score(y, y_pred)
        test_mae = mean_absolute_error(y, y_pred)
        test_rmse = np.sqrt(mean_squared_error(y, y_pred))
        
        print("\n" + "="*60)
        print("Evaluation Metrics (All Data):")
        print("="*60)
        print(f"MAPE: {test_mape:.4f}%")
        print(f"RRSE: {test_rrse:.4f}")
        print(f"R:    {test_r:.4f}")
        print(f"R²:   {test_r2:.4f}")
        print(f"MAE:  {test_mae:.4f}")
        print(f"RMSE: {test_rmse:.4f}")
        print("="*60)
        
        # 显示特征重要性（Top 5）
        feature_importance = pd.DataFrame({
            'feature': feature_names,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\nTop 5 Most Important Features:")
        print(feature_importance.head(5).to_string(index=False))
    else:
        print(f"\nError: Model file not found at {model_path}")
        print("Run with --train flag to train a new model")

if __name__ == "__main__":
    main()
