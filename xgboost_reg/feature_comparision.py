import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import os
import argparse
import warnings
warnings.filterwarnings('ignore')

# 评估指标函数
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))


def main():
    parser = argparse.ArgumentParser(description='Compare multiple trained models')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    args = parser.parse_args()
    
    # Model 1 使用指定的数据文件
    data_path_1 = '/home/ice890425/E-Syn/sym_reg/1000.csv'
    if not os.path.exists(data_path_1):
        print(f"✗ Error: Model 1 data file not found at {data_path_1}")
        return
    
    # Model 2 使用 graph5000new.csv
    data_path_2 = '../sym_reg/graph5000new.csv'
    if not os.path.exists(data_path_2):
        print(f"✗ Error: Model 2 data file not found at {data_path_2}")
        return
    
    # 读取 Model 1 的数据
    print(f"Loading Model 1 data from: {data_path_1}")
    data = pd.read_csv(data_path_1)
    print(f"Data shape: {data.shape}")
    print(f"Data columns: {data.columns.tolist()}")
    
    # 从数据中提取特征（排除目标变量和相关列）
    print("\nExtracting features from data...")
    # 基本排除：lev, power, area, delay, gates, cap, and_gates
    exclude_cols = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
    
    # Model 1 (xgb_data_1) 使用所有特征（只排除基本特征）
    exclude_cols_1 = [col for col in exclude_cols if col in data.columns]
    feature_cols_1 = [col for col in data.columns if col not in exclude_cols_1]
    
    # Model 2 (xgb_data_2) 额外排除 '&' 列
    exclude_cols_2 = exclude_cols + ['&']
    exclude_cols_2 = [col for col in exclude_cols_2 if col in data.columns]
    feature_cols_2 = [col for col in data.columns if col not in exclude_cols_2]
    
    print(f"\nFor Model 1 (xgb_data_1):")
    print(f"  Data file: {data_path_1}")
    print(f"  Excluded columns: {exclude_cols_1}")
    print(f"  Feature count: {len(feature_cols_1)}")
    print(f"\nFor Model 2 (xgb_data_2):")
    print(f"  Data file: {data_path_2}")
    print(f"  Will exclude: {exclude_cols}")
    print(f"  Note: Model 2 uses different test set")
    
    # 选择目标变量
    if args.target == 'area':
        y = data['area'].values
    else:
        y = data['delay'].values
    
    print(f"\nTarget shape: {y.shape}")
    print(f"Using {len(y)} samples for evaluation")
    
    # 定义要对比的模型结果
    results = {}
    
    print("\n" + "="*80)
    print("Feature Comparison: Model 1 (xgb_data_1) vs Model 2 (xgb_data_2)")
    print(f"Model 1: Using {data_path_1}")
    print(f"Model 2: Using {data_path_2}")
    print("Loading pre-trained models and evaluating on test sets")
    print("="*80)
    
    # 创建输出文件夹
    output_dir = 'feature_comparison_results'
    os.makedirs(output_dir, exist_ok=True)
    
    def load_xgb_model_from_rs_folder(folder_path, target):
        """从文件夹中加载 XGBoost 模型（优先使用 .model 文件）"""
        model_path = os.path.join(folder_path, f'xgb_best_model_{target}.model')
        rs_path = os.path.join(folder_path, f'model_{target}.rs')
        
        # 优先使用 .model 文件
        if os.path.exists(model_path):
            print(f"  Loading XGBoost model from {model_path}...")
            try:
                model = xgb.XGBRegressor()
                model.load_model(model_path)
                print("  ✓ Model loaded successfully")
                return model
            except Exception as e:
                print(f"  ✗ Error loading XGBoost model: {e}")
                return None
        elif os.path.exists(rs_path):
            print(f"  Found .rs file at {rs_path}, but Rust code cannot be executed in Python.")
            print(f"  Please ensure .model file exists at {model_path}")
            return None
        else:
            print(f"  ✗ Error: Model files not found in {folder_path}")
            print(f"  Expected: {model_path} or {rs_path}")
            return None
    
    # 1. XGBoost Model 1 from xgb_data_1
    print("\n[1/2] XGBoost Model 1 (xgb_data_1)")
    xgb_model_1 = load_xgb_model_from_rs_folder('xgb_data_1', args.target)
    if xgb_model_1 is None:
        print("  Please train the model first using train.py")
        return
    
    # 使用第一个特征集（Model 1 不排除 '&'）
    X_1 = data[feature_cols_1].values
    print(f"  Using {len(feature_cols_1)} features for prediction")
    
    # 验证特征数量
    try:
        # XGBoost 模型会检查特征数量
        test_pred = xgb_model_1.predict(X_1[:1])  # 测试单个样本
        print("  ✓ Feature count matches model expectations")
    except Exception as e:
        print(f"  ⚠ Warning: Feature validation failed: {e}")
        print(f"  Model expects different feature count or order")
    
    print("  Evaluating on test set...")
    y_pred_1 = xgb_model_1.predict(X_1)
    results['Model 1 (xgb_data_1)'] = {
        'MAE': mean_absolute_error(y, y_pred_1),
        'MAPE': mape(y, y_pred_1),
        'RMSE': np.sqrt(mean_squared_error(y, y_pred_1)),
        'R²': r2_score(y, y_pred_1),
        'RRSE': rrse(y, y_pred_1),
    }
    print("  ✓ Model 1 (xgb_data_1) loaded and evaluated")
    
    # 2. XGBoost Model 2 from xgb_data_2
    print("\n[2/2] XGBoost Model 2 (xgb_data_2)")
    xgb_model_2 = load_xgb_model_from_rs_folder('xgb_data_2', args.target)
    if xgb_model_2 is None:
        print("  Please train the model first using train.py")
        return
    
    # Model 2 使用 graph5000new.csv 作为测试集
    print(f"  Loading test data from {data_path_2}...")
    data_2 = pd.read_csv(data_path_2)
    print(f"  Test data shape: {data_2.shape}")
    print(f"  Test data columns: {data_2.columns.tolist()}")
    
    # 为 Model 2 准备特征（排除 '&'）
    exclude_cols_2 = exclude_cols 
    exclude_cols_2 = [col for col in exclude_cols_2 if col in data_2.columns]
    feature_cols_2 = [col for col in data_2.columns if col not in exclude_cols_2]
    
    print(f"  Excluded columns for Model 2: {exclude_cols_2}")
    print(f"  Feature count for Model 2: {len(feature_cols_2)}")
    if '&' in exclude_cols_2:
        print(f"  Note: '&' column excluded for Model 2")
    
    # 使用第二个特征集（Model 2 排除 '&'）
    X_2 = data_2[feature_cols_2].values
    
    # 选择目标变量
    if args.target == 'area':
        y_2 = data_2['area'].values
    else:
        y_2 = data_2['delay'].values
    
    print(f"  Using {len(feature_cols_2)} features for prediction")
    print(f"  Test set size: {len(y_2)} samples")
    
    # 验证特征数量
    try:
        test_pred = xgb_model_2.predict(X_2[:1])  # 测试单个样本
        print("  ✓ Feature count matches model expectations")
    except Exception as e:
        print(f"  ⚠ Warning: Feature validation failed: {e}")
        print(f"  Model expects different feature count or order")
    
    print("  Evaluating on graph5000new.csv test set...")
    y_pred_2 = xgb_model_2.predict(X_2)
    results['Model 2 (xgb_data_2)'] = {
        'MAE': mean_absolute_error(y_2, y_pred_2),
        'MAPE': mape(y_2, y_pred_2),
        'RMSE': np.sqrt(mean_squared_error(y_2, y_pred_2)),
        'R²': r2_score(y_2, y_pred_2),
        'RRSE': rrse(y_2, y_pred_2),
    }
    print("  ✓ Model 2 (xgb_data_2) loaded and evaluated on graph5000new.csv")
    
    # 打印对比结果
    print("\n" + "="*80)
    print("Feature Comparison Results")
    print(f"Model 1: Evaluated on {data_path_1}")
    print(f"Model 2: Evaluated on {data_path_2}")
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
    csv_filename = os.path.join(output_dir, f'feature_comparison_results_{args.target}.csv')
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
        plot_filename = os.path.join(output_dir, f'feature_comparison_{args.target}.png')
        plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
        print(f"Comparison plots saved to '{plot_filename}'")
        
    except Exception as e:
        print(f"Warning: Could not create plots: {e}")

if __name__ == "__main__":
    main()
