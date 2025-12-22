import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import cross_val_score, KFold, GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import lightgbm as lgb
import os
import argparse
import warnings
warnings.filterwarnings('ignore')

# 评估指标函数
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))

# MLP 模型定义
class MLPRegressor(nn.Module):
    def __init__(self, input_dim, hidden_dims=[128, 64, 32], dropout_rate=0.2):
        super(MLPRegressor, self).__init__()
        layers = []
        prev_dim = input_dim
        
        for hidden_dim in hidden_dims:
            layers.append(nn.Linear(prev_dim, hidden_dim))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout_rate))
            prev_dim = hidden_dim
        
        layers.append(nn.Linear(prev_dim, 1))
        self.model = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.model(x).squeeze()

# MLP 包装类，用于预测
class MLPWrapper:
    def __init__(self, model, scaler, device='cuda'):
        self.model = model
        self.scaler = scaler
        self.device = torch.device(device if torch.cuda.is_available() else 'cpu')
    
    def predict(self, X):
        self.model.eval()
        X_scaled = self.scaler.transform(X)
        X_tensor = torch.FloatTensor(X_scaled).to(self.device)
        
        with torch.no_grad():
            pred = self.model(X_tensor).cpu().numpy()
        
        return pred

# 交叉验证评估函数（用于XGBoost和Random Forest）
def cross_val_evaluate_sklearn(model, X, y, model_name="Model", n_folds=10):
    """使用交叉验证评估sklearn兼容的模型（XGBoost, Random Forest）"""
    print(f"Cross-validating {model_name} ({n_folds}-fold)...")
    
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)
    
    # 计算各个指标
    mae_scores = -cross_val_score(model, X, y, cv=kf, scoring='neg_mean_absolute_error')
    mape_scores = -cross_val_score(model, X, y, cv=kf, scoring='neg_mean_absolute_percentage_error')
    mse_scores = -cross_val_score(model, X, y, cv=kf, scoring='neg_mean_squared_error')
    r2_scores = cross_val_score(model, X, y, cv=kf, scoring='r2')
    
    # 计算RMSE和RRSE
    rmse_scores = np.sqrt(mse_scores)
    rrse_scores = rmse_scores / np.std(y)
    
    # sklearn 的 MAPE 返回小数形式（0-1），需要乘以 100 转换为百分比形式
    # 以与自定义的 mape 函数保持一致（返回百分比 0-100）
    mape_scores_percent = mape_scores * 100
    
    return {
        'MAE': np.mean(mae_scores),
        'MAE_std': np.std(mae_scores),
        'MAPE': np.mean(mape_scores_percent),
        'MAPE_std': np.std(mape_scores_percent),
        'RRSE': np.mean(rrse_scores),
        'RRSE_std': np.std(rrse_scores),
        'R²': np.mean(r2_scores),
        'R²_std': np.std(r2_scores),
        'RMSE': np.mean(rmse_scores),
        'RMSE_std': np.std(rmse_scores),
    }

# 交叉验证评估函数（用于MLP）
def cross_val_evaluate_mlp(mlp_wrapper, X, y, model_name="MLP", n_folds=10):
    """使用交叉验证评估MLP模型"""
    print(f"Cross-validating {model_name} ({n_folds}-fold)...")
    
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)
    
    mae_scores = []
    mape_scores = []
    rmse_scores = []
    r2_scores = []
    rrse_scores = []
    
    for fold, (train_idx, val_idx) in enumerate(kf.split(X)):
        X_train_fold, X_val_fold = X[train_idx], X[val_idx]
        y_train_fold, y_val_fold = y[train_idx], y[val_idx]
        
        # 使用MLP包装器进行预测
        y_pred = mlp_wrapper.predict(X_val_fold)
        
        # 计算指标
        mae_scores.append(mean_absolute_error(y_val_fold, y_pred))
        mape_scores.append(mape(y_val_fold, y_pred))
        rmse_scores.append(np.sqrt(mean_squared_error(y_val_fold, y_pred)))
        r2_scores.append(r2_score(y_val_fold, y_pred))
        rrse_scores.append(rrse(y_val_fold, y_pred))
        
        if (fold + 1) % 2 == 0:
            print(f"  Completed {fold + 1}/{n_folds} folds...", end='\r', flush=True)
    
    print(f"  Completed {n_folds}/{n_folds} folds")
    
    return {
        'MAE': np.mean(mae_scores),
        'MAE_std': np.std(mae_scores),
        'MAPE': np.mean(mape_scores),
        'MAPE_std': np.std(mape_scores),
        'RRSE': np.mean(rrse_scores),
        'RRSE_std': np.std(rrse_scores),
        'R²': np.mean(r2_scores),
        'R²_std': np.std(r2_scores),
        'RMSE': np.mean(rmse_scores),
        'RMSE_std': np.std(rmse_scores),
    }

def main():
    parser = argparse.ArgumentParser(description='Compare multiple trained models')
    parser.add_argument('--data', type=str, default='../sym_reg/feature1/10000.csv', help='Path to data file')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    args = parser.parse_args()
    
    # 读取数据
    data_path = args.data
    if not os.path.exists(data_path):
        alternative_paths = [
            '../sym_reg/feature1/1000.csv',
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
            print(f"Error: Data file not found at {args.data}")
            print("Tried alternative paths but none exist.")
            return
    
    data = pd.read_csv(data_path)
    print(f"Data shape: {data.shape}")
    print(f"Data columns: {data.columns.tolist()}")
    
    # 从数据中提取特征（排除目标变量和相关列）
    print("\nExtracting features from data...")
    # 排除：lev, power, area, delay, gates, cap, and_gates
    exclude_cols = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
    exclude_cols = [col for col in exclude_cols if col in data.columns]
    feature_cols = [col for col in data.columns if col not in exclude_cols]
    print(f"Excluded columns: {exclude_cols}")
    print(f"Final feature count: {len(feature_cols)}")
    print(f"Feature columns: {feature_cols}")
    
    X = data[feature_cols].values
    # 选择目标变量
    if args.target == 'area':
        y = data['area'].values
    else:
        y = data['delay'].values
    
    print(f"\nFeature shape: {X.shape}")
    print(f"Number of features: {X.shape[1]}")
    print(f"Target shape: {y.shape}")
    print(f"Using {X.shape[0]} test samples for evaluation")
    
    # 定义要对比的模型
    models = {}
    results = {}
    
    print("\n" + "="*80)
    print("Model Comparison: XGBoost vs Random Forest vs LightGBM")
    print("Loading pre-trained models and evaluating on test set")
    print("="*80)
    
    # 检测是否有 GPU
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    
    # 1. XGBoost - 从 Python 代码或模型文件加载
    print("\n[1/3] XGBoost")
    xgb_py_path = f'xgb_data/xgb_model_{args.target}.py'
    xgb_model_path = f'xgb_data/xgb_best_model_{args.target}.model'
    
    if os.path.exists(xgb_py_path):
        print(f"  Loading XGBoost model from {xgb_py_path}...")
        try:
            # 动态导入 Python 模型代码
            import importlib.util
            spec = importlib.util.spec_from_file_location("xgb_model", xgb_py_path)
            xgb_model_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(xgb_model_module)
            
            # 创建预测函数包装器
            def xgb_predict(X_data):
                predictions = []
                for row in X_data:
                    pred = xgb_model_module.score(row.tolist())
                    predictions.append(pred)
                return np.array(predictions)
            
            # 在测试集上评估
            print("  Evaluating on test set...")
            y_pred = xgb_predict(X)
            results['XGBoost'] = {
                'MAE': mean_absolute_error(y, y_pred),
                'MAPE': mape(y, y_pred),
                'RMSE': np.sqrt(mean_squared_error(y, y_pred)),
                'R²': r2_score(y, y_pred),
                'RRSE': rrse(y, y_pred),
            }
            print("  ✓ XGBoost model loaded and evaluated")
        except Exception as e:
            print(f"  ✗ Error loading XGBoost Python model: {e}")
            # 尝试使用 .model 文件作为后备
            if os.path.exists(xgb_model_path):
                print(f"  Trying to load from {xgb_model_path}...")
                try:
                    models['XGBoost'] = xgb.XGBRegressor()
                    models['XGBoost'].load_model(xgb_model_path)
                    y_pred = models['XGBoost'].predict(X)
                    results['XGBoost'] = {
                        'MAE': mean_absolute_error(y, y_pred),
                        'MAPE': mape(y, y_pred),
                        'RMSE': np.sqrt(mean_squared_error(y, y_pred)),
                        'R²': r2_score(y, y_pred),
                        'RRSE': rrse(y, y_pred),
                    }
                    print("  ✓ XGBoost model loaded from .model file")
                except Exception as e2:
                    print(f"  ✗ Error loading XGBoost model: {e2}")
                    return
            else:
                print(f"  ✗ Error: Model files not found")
                print("  Please train the model first using train.py")
                return
    elif os.path.exists(xgb_model_path):
        print(f"  Loading pre-trained XGBoost model from {xgb_model_path}...")
        try:
            models['XGBoost'] = xgb.XGBRegressor()
            models['XGBoost'].load_model(xgb_model_path)
            print("  ✓ Model loaded successfully")
            print("  Evaluating on test set...")
            y_pred = models['XGBoost'].predict(X)
            results['XGBoost'] = {
                'MAE': mean_absolute_error(y, y_pred),
                'MAPE': mape(y, y_pred),
                'RMSE': np.sqrt(mean_squared_error(y, y_pred)),
                'R²': r2_score(y, y_pred),
                'RRSE': rrse(y, y_pred),
            }
        except Exception as e:
            print(f"  ✗ Error loading XGBoost model: {e}")
            return
    else:
        print(f"  ✗ Error: Model files not found")
        print("  Please train the model first using train.py")
        return
    
    # 2. Random Forest - 从 Python 代码加载模型
    print("\n[2/3] Random Forest")
    rf_model_path = f'rf_data/rf_model_{args.target}.py'
    if os.path.exists(rf_model_path):
        print(f"  Loading Random Forest model from {rf_model_path}...")
        try:
            # 动态导入 Python 模型代码
            import importlib.util
            spec = importlib.util.spec_from_file_location("rf_model", rf_model_path)
            rf_model_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(rf_model_module)
            
            # 创建预测函数包装器
            def rf_predict(X_data):
                predictions = []
                for row in X_data:
                    pred = rf_model_module.score(row.tolist())
                    predictions.append(pred)
                return np.array(predictions)
            
            # 在测试集上评估
            print("  Evaluating on test set...")
            y_pred_rf = rf_predict(X)
            results['Random Forest'] = {
                'MAE': mean_absolute_error(y, y_pred_rf),
                'MAPE': mape(y, y_pred_rf),
                'RMSE': np.sqrt(mean_squared_error(y, y_pred_rf)),
                'R²': r2_score(y, y_pred_rf),
                'RRSE': rrse(y, y_pred_rf),
            }
            print("  ✓ Random Forest model loaded and evaluated")
        except Exception as e:
            print(f"  ✗ Error loading Random Forest model: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"  ✗ Error: Model file not found at {rf_model_path}")
        print("  Please train the model first using RF_train.py")
    
    # 3. LightGBM - 从 Python 代码加载模型
    print("\n[3/3] LightGBM")
    lgbm_model_path = f'lgbm_data/lgbm_model_{args.target}.py'
    if os.path.exists(lgbm_model_path):
        print(f"  Loading LightGBM model from {lgbm_model_path}...")
        try:
            # 动态导入 Python 模型代码
            import importlib.util
            spec = importlib.util.spec_from_file_location("lgbm_model", lgbm_model_path)
            lgbm_model_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(lgbm_model_module)
            
            # 创建预测函数包装器
            def lgbm_predict(X_data):
                predictions = []
                for row in X_data:
                    pred = lgbm_model_module.score(row.tolist())
                    predictions.append(pred)
                return np.array(predictions)
            
            # 在测试集上评估
            print("  Evaluating on test set...")
            y_pred_lgb = lgbm_predict(X)
            results['LightGBM'] = {
                'MAE': mean_absolute_error(y, y_pred_lgb),
                'MAPE': mape(y, y_pred_lgb),
                'RMSE': np.sqrt(mean_squared_error(y, y_pred_lgb)),
                'R²': r2_score(y, y_pred_lgb),
                'RRSE': rrse(y, y_pred_lgb),
            }
            print("  ✓ LightGBM model loaded and evaluated")
        except Exception as e:
            print(f"  ✗ Error loading LightGBM model: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"  ✗ Error: Model file not found at {lgbm_model_path}")
        print("  Please train the model first using LightGBM_train.py")
    
    # 打印对比结果
    print("\n" + "="*80)
    print("Model Comparison Results (Test Set Evaluation)")
    print("="*80)
    
    # 创建结果 DataFrame
    comparison_df = pd.DataFrame(results).T
    comparison_df = comparison_df.sort_values('MAPE')  # 按 MAPE 排序
    
    # 格式化输出
    print(f"\n{'Model':<20} {'MAE':<15} {'MAPE (%)':<15} {'RRSE':<15} {'R²':<15} {'RMSE':<15}")
    print("-" * 100)
    
    for model_name in comparison_df.index:
        metrics = results[model_name]
        print(f"{model_name:<20} "
              f"{metrics['MAE']:>6.2f}      "
              f"{metrics['MAPE']:>6.2f}      "
              f"{metrics['RRSE']:>6.4f}      "
              f"{metrics['R²']:>6.4f}      "
              f"{metrics['RMSE']:>6.2f}")
    
    # 保存结果到 CSV
    csv_filename = f'model_comparison_results_{args.target}.csv'
    comparison_df.to_csv(csv_filename)
    print(f"\nResults saved to '{csv_filename}'")
    
    # 找出最佳模型
    best_model_mape = comparison_df.index[0]
    best_mape = comparison_df.loc[best_model_mape, 'MAPE']
    best_model_r2 = comparison_df['R²'].idxmax()
    best_r2 = comparison_df.loc[best_model_r2, 'R²']
    best_model_mae = comparison_df['MAE'].idxmin()
    best_mae = comparison_df.loc[best_model_mae, 'MAE']
    best_model_rmse = comparison_df['RMSE'].idxmin()
    best_rmse = comparison_df.loc[best_model_rmse, 'RMSE']
    best_model_rrse = comparison_df['RRSE'].idxmin()
    best_rrse = comparison_df.loc[best_model_rrse, 'RRSE']
    
    print("\n" + "="*80)
    print("Summary:")
    print("="*80)
    print(f"Best model by MAE:   {best_model_mae} (MAE: {best_mae:.2f})")
    print(f"Best model by MAPE:  {best_model_mape} (MAPE: {best_mape:.2f}%)")
    print(f"Best model by RRSE:  {best_model_rrse} (RRSE: {best_rrse:.4f})")
    print(f"Best model by R²:    {best_model_r2} (R²: {best_r2:.4f})")
    print(f"Best model by RMSE:  {best_model_rmse} (RMSE: {best_rmse:.2f})")
    print("="*80)
    
    # 绘制对比图（只显示这5个指标）
    try:
        import matplotlib.pyplot as plt
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        
        # 定义颜色（三个模型）
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 蓝色、橙色、绿色
        
        # 1. MAE 对比
        ax1 = axes[0, 0]
        comparison_df_sorted = comparison_df.sort_values('MAE', ascending=True)
        ax1.barh(comparison_df_sorted.index, comparison_df_sorted['MAE'], 
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted))])
        ax1.set_xlabel('MAE')
        ax1.set_title('Model Comparison: MAE (Lower is Better)')
        ax1.grid(axis='x', alpha=0.3)
        
        # 2. MAPE 对比
        ax2 = axes[0, 1]
        comparison_df_sorted_mape = comparison_df.sort_values('MAPE', ascending=True)
        ax2.barh(comparison_df_sorted_mape.index, comparison_df_sorted_mape['MAPE'], 
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted_mape))])
        ax2.set_xlabel('MAPE (%)')
        ax2.set_title('Model Comparison: MAPE (Lower is Better)')
        ax2.grid(axis='x', alpha=0.3)
        
        # 3. RRSE 对比
        ax3 = axes[0, 2]
        comparison_df_sorted_rrse = comparison_df.sort_values('RRSE', ascending=True)
        ax3.barh(comparison_df_sorted_rrse.index, comparison_df_sorted_rrse['RRSE'],
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted_rrse))])
        ax3.set_xlabel('RRSE')
        ax3.set_title('Model Comparison: RRSE (Lower is Better)')
        ax3.grid(axis='x', alpha=0.3)
        
        # 4. R² 对比
        ax4 = axes[1, 0]
        comparison_df_sorted_r2 = comparison_df.sort_values('R²', ascending=False)
        ax4.barh(comparison_df_sorted_r2.index, comparison_df_sorted_r2['R²'],
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted_r2))])
        ax4.set_xlabel('R²')
        ax4.set_title('Model Comparison: R² (Higher is Better)')
        ax4.grid(axis='x', alpha=0.3)
        
        # 5. RMSE 对比
        ax5 = axes[1, 1]
        comparison_df_sorted_rmse = comparison_df.sort_values('RMSE', ascending=True)
        ax5.barh(comparison_df_sorted_rmse.index, comparison_df_sorted_rmse['RMSE'],
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted_rmse))])
        ax5.set_xlabel('RMSE')
        ax5.set_title('Model Comparison: RMSE (Lower is Better)')
        ax5.grid(axis='x', alpha=0.3)
        
        # 6. 综合对比（所有5个指标的归一化综合得分）
        ax6 = axes[1, 2]
        # 归一化指标用于综合对比
        normalized_mae = 1 - (comparison_df['MAE'] - comparison_df['MAE'].min()) / (comparison_df['MAE'].max() - comparison_df['MAE'].min())
        normalized_mape = 1 - (comparison_df['MAPE'] - comparison_df['MAPE'].min()) / (comparison_df['MAPE'].max() - comparison_df['MAPE'].min())
        normalized_rrse = 1 - (comparison_df['RRSE'] - comparison_df['RRSE'].min()) / (comparison_df['RRSE'].max() - comparison_df['RRSE'].min())
        normalized_r2 = (comparison_df['R²'] - comparison_df['R²'].min()) / (comparison_df['R²'].max() - comparison_df['R²'].min())
        normalized_rmse = 1 - (comparison_df['RMSE'] - comparison_df['RMSE'].min()) / (comparison_df['RMSE'].max() - comparison_df['RMSE'].min())
        composite_score = (normalized_mae + normalized_mape + normalized_rrse + normalized_r2 + normalized_rmse) / 5
        
        comparison_df_sorted_comp = comparison_df.copy()
        comparison_df_sorted_comp['Composite'] = composite_score
        comparison_df_sorted_comp = comparison_df_sorted_comp.sort_values('Composite', ascending=False)
        
        ax6.barh(comparison_df_sorted_comp.index, comparison_df_sorted_comp['Composite'],
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted_comp))])
        ax6.set_xlabel('Composite Score (Normalized)')
        ax6.set_title('Model Comparison: Composite Score (Higher is Better)')
        ax6.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        plot_filename = f'model_comparison_{args.target}.png'
        plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
        print(f"Comparison plots saved to '{plot_filename}'")
        
    except Exception as e:
        print(f"Warning: Could not create plots: {e}")

if __name__ == "__main__":
    main()