import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

# 评估指标函数
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))

def r(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]

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

# 评估函数
def evaluate_model(model, X_test, y_test, model_name="Model"):
    """在测试集上评估模型"""
    print(f"Evaluating {model_name} on test set (size: {len(X_test)})...")
    y_pred = model.predict(X_test)
    
    mae_score = mean_absolute_error(y_test, y_pred)
    mape_score = mape(y_test, y_pred)
    rrse_score = rrse(y_test, y_pred)
    r_score = r(y_test, y_pred)
    rmse_score = np.sqrt(mean_squared_error(y_test, y_pred))
    r2_score_val = r2_score(y_test, y_pred)
    
    return {
        'MAE': mae_score,
        'MAPE': mape_score,
        'RRSE': rrse_score,
        'R': r_score,
        'RMSE': rmse_score,
        'R²': r2_score_val,
    }

def main():
    # 读取数据
    data_path = '../sym_reg/feature1/10000.csv'
    
    # 如果文件不存在，尝试其他路径
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
    
    data = pd.read_csv(data_path)
    print(f"Data shape: {data.shape}")
    print(f"Data columns: {data.columns.tolist()}")
    
    # 提取特征和目标
    # 排除最后3列（power, area, delay），使用前面的列作为特征
    X = data.iloc[:, :-3].values  # 排除最后3列
    y = data['area'].values
    
    # 打印详细的特征信息
    print(f"\nData columns: {data.columns.tolist()}")
    print(f"Total columns: {len(data.columns)}")
    print(f"Excluded columns (last 3): {data.columns[-3:].tolist()}")
    print(f"Feature columns: {data.columns[:-3].tolist()}")
    print(f"\nFeature shape: {X.shape}")
    print(f"Number of features: {X.shape[1]}")
    print(f"Feature names: {data.columns[:-3].tolist()}")
    print(f"Target shape: {y.shape}")
    print(f"Target statistics: mean={np.mean(y):.2f}, std={np.std(y):.2f}, min={np.min(y):.2f}, max={np.max(y):.2f}")
    
    # 使用全部数据作为测试集
    X_test = X
    y_test = y
    print(f"\nTest set: {X_test.shape[0]} samples (using all data)")
    
    # 定义要对比的模型
    models = {}
    results = {}
    
    print("\n" + "="*80)
    print("Model Comparison: XGBoost vs MLP vs Random Forest")
    print("="*80)
    
    # 检测是否有 GPU
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    
    # 1. XGBoost - 加载预训练模型
    print("\n[1/2] XGBoost")
    xgb_model_path = 'xgb_best_model.model'
    if os.path.exists(xgb_model_path):
        print(f"  Loading pre-trained XGBoost model from {xgb_model_path}...")
        models['XGBoost'] = xgb.XGBRegressor()
        models['XGBoost'].load_model(xgb_model_path)
        print("  ✓ Model loaded successfully")
        results['XGBoost'] = evaluate_model(models['XGBoost'], X_test, y_test, "XGBoost")
    else:
        print(f"  ✗ Error: Pre-trained model not found at {xgb_model_path}")
        print("  Please train the model first using train.py")
        return
    
    # 2. MLP - 加载预训练模型
    print("\n[2/3] MLP (Multi-Layer Perceptron)")
    mlp_model_path = 'mlp_model_complete.pth'
    if os.path.exists(mlp_model_path):
        print(f"  Loading pre-trained MLP model from {mlp_model_path}...")
        try:
            checkpoint = torch.load(mlp_model_path, weights_only=False)
            
            # 从 checkpoint 中读取实际的模型结构参数
            # 优先从 model_params 中读取（如果存在），否则从顶层读取
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
            results['MLP'] = evaluate_model(models['MLP'], X_test, y_test, "MLP")
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
    print("\n[3/3] Random Forest")
    rf_model_path = 'rf_best_model.pkl'
    if os.path.exists(rf_model_path):
        print(f"  Loading pre-trained Random Forest model from {rf_model_path}...")
        try:
            checkpoint = joblib.load(rf_model_path)
            models['Random Forest'] = checkpoint['model']
            print("  ✓ Model loaded successfully")
            print(f"  Best parameters: {checkpoint.get('best_params', 'N/A')}")
            results['Random Forest'] = evaluate_model(models['Random Forest'], X_test, y_test, "Random Forest")
        except Exception as e:
            print(f"  ✗ Error loading Random Forest model: {e}")
            import traceback
            traceback.print_exc()
            return
    else:
        print(f"  ✗ Error: Pre-trained model not found at {rf_model_path}")
        print("  Please train the model first using RF_train.py or RF_test.py")
        return
    
    # 打印对比结果
    print("\n" + "="*80)
    print("Model Comparison Results")
    print("="*80)
    
    # 创建结果 DataFrame
    comparison_df = pd.DataFrame(results).T
    comparison_df = comparison_df.sort_values('MAPE')  # 按 MAPE 排序
    
    # 格式化输出
    print(f"\n{'Model':<20} {'MAPE (%)':<12} {'R²':<10} {'R':<10} {'RRSE':<10} {'MAE':<10} {'RMSE':<10}")
    print("-" * 80)
    
    for model_name in comparison_df.index:
        row = comparison_df.loc[model_name]
        print(f"{model_name:<20} "
              f"{row['MAPE']:>10.2f} "
              f"{row['R²']:>9.4f} "
              f"{row['R']:>9.4f} "
              f"{row['RRSE']:>9.4f} "
              f"{row['MAE']:>9.2f} "
              f"{row['RMSE']:>9.2f}")
    
    # 保存结果到 CSV
    comparison_df.to_csv('model_comparison_results.csv')
    print(f"\nResults saved to 'model_comparison_results.csv'")
    
    # 找出最佳模型
    best_model_mape = comparison_df.index[0]
    best_mape = comparison_df.loc[best_model_mape, 'MAPE']
    best_model_r2 = comparison_df.loc[comparison_df['R²'].idxmax(), :]
    
    print("\n" + "="*80)
    print("Summary:")
    print("="*80)
    print(f"Best model by MAPE: {best_model_mape} (MAPE: {best_mape:.2f}%)")
    print(f"Best model by R²: {comparison_df['R²'].idxmax()} (R²: {comparison_df['R²'].max():.4f})")
    print("="*80)
    
    # 绘制对比图
    try:
        import matplotlib.pyplot as plt
        
        # MAPE 对比图
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # 定义颜色（三个模型）
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 蓝色、橙色、绿色
        
        # 1. MAPE 对比
        ax1 = axes[0, 0]
        comparison_df_sorted = comparison_df.sort_values('MAPE', ascending=True)
        ax1.barh(comparison_df_sorted.index, comparison_df_sorted['MAPE'], 
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted))])
        ax1.set_xlabel('MAPE (%)')
        ax1.set_title('Model Comparison: MAPE (Lower is Better)')
        ax1.grid(axis='x', alpha=0.3)
        
        # 2. R² 对比
        ax2 = axes[0, 1]
        comparison_df_sorted_r2 = comparison_df.sort_values('R²', ascending=False)
        ax2.barh(comparison_df_sorted_r2.index, comparison_df_sorted_r2['R²'],
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted_r2))])
        ax2.set_xlabel('R²')
        ax2.set_title('Model Comparison: R² (Higher is Better)')
        ax2.grid(axis='x', alpha=0.3)
        
        # 3. RMSE 对比
        ax3 = axes[1, 0]
        comparison_df_sorted_rmse = comparison_df.sort_values('RMSE', ascending=True)
        ax3.barh(comparison_df_sorted_rmse.index, comparison_df_sorted_rmse['RMSE'],
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted_rmse))])
        ax3.set_xlabel('RMSE')
        ax3.set_title('Model Comparison: RMSE (Lower is Better)')
        ax3.grid(axis='x', alpha=0.3)
        
        # 4. 综合对比（归一化后的多个指标）
        ax4 = axes[1, 1]
        # 归一化指标用于综合对比
        normalized_mape = 1 - (comparison_df['MAPE'] - comparison_df['MAPE'].min()) / (comparison_df['MAPE'].max() - comparison_df['MAPE'].min())
        normalized_r2 = (comparison_df['R²'] - comparison_df['R²'].min()) / (comparison_df['R²'].max() - comparison_df['R²'].min())
        normalized_r = (comparison_df['R'] - comparison_df['R'].min()) / (comparison_df['R'].max() - comparison_df['R'].min())
        composite_score = (normalized_mape + normalized_r2 + normalized_r) / 3
        
        comparison_df_sorted_comp = comparison_df.copy()
        comparison_df_sorted_comp['Composite'] = composite_score
        comparison_df_sorted_comp = comparison_df_sorted_comp.sort_values('Composite', ascending=False)
        
        ax4.barh(comparison_df_sorted_comp.index, comparison_df_sorted_comp['Composite'],
                color=[colors[i % len(colors)] for i in range(len(comparison_df_sorted_comp))])
        ax4.set_xlabel('Composite Score (Normalized)')
        ax4.set_title('Model Comparison: Composite Score (Higher is Better)')
        ax4.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
        print("Comparison plots saved to 'model_comparison.png'")
        
    except Exception as e:
        print(f"Warning: Could not create plots: {e}")

if __name__ == "__main__":
    main()
