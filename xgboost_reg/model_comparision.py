import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostRegressor
import joblib
import os
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
    # 读取数据
    data_path = '../sym_reg/feature1/1000.csv'
    
    
    
    data = pd.read_csv(data_path)
    print(f"Data shape: {data.shape}")
    print(f"Data columns: {data.columns.tolist()}")
    
    # 提取特征和目标
    # 明确排除目标变量和相关列，避免数据泄漏
    # 排除：lev, power, area, delay
    exclude_cols = ['lev', 'power', 'area', 'delay']
    # 只保留存在的列（避免某些列不存在时报错）
    exclude_cols = [col for col in exclude_cols if col in data.columns]
    feature_cols = [col for col in data.columns if col not in exclude_cols]
    
    X = data[feature_cols].values
    y = data['area'].values
    
    print(f"\nFeature shape: {X.shape}")
    print(f"Number of features: {X.shape[1]}")
    print(f"Target shape: {y.shape}")
    print(f"Using {X.shape[0]} test samples for evaluation")
    
    # 定义要对比的模型
    models = {}
    results = {}
    
    print("\n" + "="*80)
    print("Model Comparison: XGBoost vs MLP vs Random Forest vs LightGBM vs CatBoost")
    print("Loading pre-trained models and evaluating on test set")
    print("="*80)
    
    # 检测是否有 GPU
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    
    # 1. XGBoost - 加载预训练模型并在测试集上评估
    print("\n[1/5] XGBoost")
    xgb_model_path = 'xgb_best_model.model'
    if os.path.exists(xgb_model_path):
        print(f"  Loading pre-trained XGBoost model from {xgb_model_path}...")
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
    else:
        print(f"  ✗ Error: Pre-trained model not found at {xgb_model_path}")
        print("  Please train the model first using train.py")
        return
    
    # 2. MLP - 加载预训练模型
    print("\n[2/5] MLP (Multi-Layer Perceptron)")
    mlp_model_path = 'mlp_model_complete.pth'
    if os.path.exists(mlp_model_path):
        print(f"  Loading pre-trained MLP model from {mlp_model_path}...")
        try:
            checkpoint = torch.load(mlp_model_path, weights_only=False)
            
            # 从 checkpoint 中读取实际的模型结构参数
            model_params = checkpoint.get('model_params', {})
            input_dim = checkpoint.get('input_dim', X.shape[1])
            hidden_dims = model_params.get('hidden_dims', checkpoint.get('hidden_dims', [128, 64, 32]))
            dropout_rate = model_params.get('dropout', checkpoint.get('dropout_rate', 0.2))
            
            print(f"  Model architecture: input_dim={input_dim}, hidden_dims={hidden_dims}, dropout_rate={dropout_rate}")
            
            # 使用从 checkpoint 读取的参数创建模型
            mlp_model = MLPRegressor(
                input_dim=input_dim,
                hidden_dims=hidden_dims,
                dropout_rate=dropout_rate
            )
            mlp_model.load_state_dict(checkpoint['model_state_dict'])
            mlp_model = mlp_model.to(device)
            mlp_model.eval()
            
            # 创建包装类用于评估
            mlp_scaler = checkpoint.get('scaler', StandardScaler())
            models['MLP'] = MLPWrapper(mlp_model, mlp_scaler, device=device)
            print("  ✓ Model loaded successfully")
            print("  Evaluating on test set...")
            y_pred = models['MLP'].predict(X)
            results['MLP'] = {
                'MAE': mean_absolute_error(y, y_pred),
                'MAPE': mape(y, y_pred),
                'RMSE': np.sqrt(mean_squared_error(y, y_pred)),
                'R²': r2_score(y, y_pred),
                'RRSE': rrse(y, y_pred),
            }
        except Exception as e:
            print(f"  ✗ Error loading MLP model: {e}")
            import traceback
            traceback.print_exc()
            return
    else:
        print(f"  ✗ Error: Pre-trained model not found at {mlp_model_path}")
        print("  Please train the model first using MLP_train.py")
        return
    
    # 3. Random Forest - 加载预训练模型
    print("\n[3/5] Random Forest")
    rf_model_path = 'rf_best_model.pkl'
    if os.path.exists(rf_model_path):
        print(f"  Loading pre-trained Random Forest model from {rf_model_path}...")
        try:
            checkpoint = joblib.load(rf_model_path)
            models['Random Forest'] = checkpoint['model']
            print("  ✓ Model loaded successfully")
            print(f"  Best parameters: {checkpoint.get('best_params', 'N/A')}")
            print("  Evaluating on test set...")
            y_pred = models['Random Forest'].predict(X)
            results['Random Forest'] = {
                'MAE': mean_absolute_error(y, y_pred),
                'MAPE': mape(y, y_pred),
                'RMSE': np.sqrt(mean_squared_error(y, y_pred)),
                'R²': r2_score(y, y_pred),
                'RRSE': rrse(y, y_pred),
            }
        except Exception as e:
            print(f"  ✗ Error loading Random Forest model: {e}")
            import traceback
            traceback.print_exc()
            return
    else:
        print(f"  ✗ Error: Pre-trained model not found at {rf_model_path}")
        print("  Please train the model first using RF_train.py or RF_test.py")
        return
    
    # 4. LightGBM - 加载预训练模型
    print("\n[4/5] LightGBM")
    lgbm_model_path = 'lgbm_best_model.pkl'
    if os.path.exists(lgbm_model_path):
        print(f"  Loading pre-trained LightGBM model from {lgbm_model_path}...")
        try:
            checkpoint = joblib.load(lgbm_model_path)
            models['LightGBM'] = checkpoint['model']
            print("  ✓ Model loaded successfully")
            print(f"  Best parameters: {checkpoint.get('best_params', 'N/A')}")
            print("  Evaluating on test set...")
            y_pred = models['LightGBM'].predict(X)
            results['LightGBM'] = {
                'MAE': mean_absolute_error(y, y_pred),
                'MAPE': mape(y, y_pred),
                'RMSE': np.sqrt(mean_squared_error(y, y_pred)),
                'R²': r2_score(y, y_pred),
                'RRSE': rrse(y, y_pred),
            }
            # 立即打印结果
            print(f"  LightGBM Results:")
            print(f"    MAE:   {results['LightGBM']['MAE']:.4f}")
            print(f"    MAPE:  {results['LightGBM']['MAPE']:.4f}%")
            print(f"    RMSE:  {results['LightGBM']['RMSE']:.4f}")
            print(f"    R²:    {results['LightGBM']['R²']:.4f}")
            print(f"    RRSE:  {results['LightGBM']['RRSE']:.4f}")
        except Exception as e:
            print(f"  ✗ Error loading LightGBM model: {e}")
            import traceback
            traceback.print_exc()
            return
    else:
        print(f"  ✗ Error: Pre-trained model not found at {lgbm_model_path}")
        print("  Please train the model first using LightGBM_train.py")
        return
    
    # 5. CatBoost - 加载预训练模型
    print("\n[5/5] CatBoost")
    catboost_model_path = 'catboost_best_model.pkl'
    if os.path.exists(catboost_model_path):
        print(f"  Loading pre-trained CatBoost model from {catboost_model_path}...")
        try:
            checkpoint = joblib.load(catboost_model_path)
            models['CatBoost'] = checkpoint['model']
            print("  ✓ Model loaded successfully")
            print(f"  Best parameters: {checkpoint.get('best_params', 'N/A')}")
            print("  Evaluating on test set...")
            y_pred = models['CatBoost'].predict(X)
            results['CatBoost'] = {
                'MAE': mean_absolute_error(y, y_pred),
                'MAPE': mape(y, y_pred),
                'RMSE': np.sqrt(mean_squared_error(y, y_pred)),
                'R²': r2_score(y, y_pred),
                'RRSE': rrse(y, y_pred),
            }
            # 立即打印结果
            print(f"  CatBoost Results:")
            print(f"    MAE:   {results['CatBoost']['MAE']:.4f}")
            print(f"    MAPE:  {results['CatBoost']['MAPE']:.4f}%")
            print(f"    RMSE:  {results['CatBoost']['RMSE']:.4f}")
            print(f"    R²:    {results['CatBoost']['R²']:.4f}")
            print(f"    RRSE:  {results['CatBoost']['RRSE']:.4f}")
        except Exception as e:
            print(f"  ✗ Error loading CatBoost model: {e}")
            import traceback
            traceback.print_exc()
            return
    else:
        print(f"  ✗ Error: Pre-trained model not found at {catboost_model_path}")
        print("  Please train the model first using CatBoost_train.py")
        return
    
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
    comparison_df.to_csv('model_comparison_results.csv')
    print(f"\nResults saved to 'model_comparison_results.csv'")
    
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
        plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
        print("Comparison plots saved to 'model_comparison.png'")
        
    except Exception as e:
        print(f"Warning: Could not create plots: {e}")

if __name__ == "__main__":
    main()
