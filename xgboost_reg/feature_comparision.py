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
    parser = argparse.ArgumentParser(description='Compare xgb_data_0 (original features) vs xgb_data_1 (no count_xor) vs xgb_data_2 (all features)')
    parser.add_argument('--data', type=str, default='../sym_reg/simple_circuit_analysis_project_test.csv', help='Path to test data file')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    args = parser.parse_args()
    
    # 读取测试数据
    data_path = args.data
    if not os.path.exists(data_path):
        # 尝试备用路径
        alternative_paths = [
            '../sym_reg/simple_circuit_analysis_project_test.csv',
            '../sym_reg/simple_circuit_analysis_project_train_val.csv',
            '../sym_reg/new_50000.csv',
            '../sym_reg/mig_circuit_analysis.csv',
            'data.csv'
        ]
        for alt_path in alternative_paths:
            if os.path.exists(alt_path):
                data_path = alt_path
                print(f"Using alternative data path: {data_path}")
                break
        else:
            print(f"✗ Error: Test data file not found at {args.data}")
            print("Tried alternative paths but none exist.")
            return
    
    print(f"Loading test data from: {data_path}")
    data = pd.read_csv(data_path)
    print(f"Data shape: {data.shape}")
    print(f"Data columns: {data.columns.tolist()}")
    
    # 选择目标变量
    if args.target == 'area':
        y = data['area'].values
    else:
        y = data['delay'].values
    
    print(f"\nTarget shape: {y.shape}")
    print(f"Using {len(y)} samples for evaluation")
    
    # 准备特征
    # Model 1 (xgb_data_0): 只使用原始 E-Syn 特征（9个）
    original_features = ['ASTSize', 'ASTDepth', '+', '!', '*', '&', 'SUM_LIB', 'SUM_NODE', 'AVE_LIB']
    available_original_features = [col for col in original_features if col in data.columns]
    missing_original = [col for col in original_features if col not in data.columns]
    
    if missing_original:
        print(f"⚠️  Warning: Some original features are missing: {missing_original}")
    
    if len(available_original_features) == 0:
        print("✗ Error: No original E-Syn features found in the data!")
        return
    
    feature_cols_1 = available_original_features
    
    # Model 2 (xgb_data_1): 使用所有特征（排除基本列和 count_xor）
    exclude_cols_2 = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates', 'count_xor']
    exclude_cols_2 = [col for col in exclude_cols_2 if col in data.columns]
    feature_cols_2 = [col for col in data.columns if col not in exclude_cols_2]
    
    # Model 3 (xgb_data_2): 使用所有特征（只排除基本列）
    exclude_cols_3 = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
    exclude_cols_3 = [col for col in exclude_cols_3 if col in data.columns]
    feature_cols_3 = [col for col in data.columns if col not in exclude_cols_3]
    
    print(f"\nFor Model 1 (xgb_data_0 - original features):")
    print(f"  Feature count: {len(feature_cols_1)}")
    print(f"  Features: {feature_cols_1}")
    print(f"\nFor Model 2 (xgb_data_1 - all features except count_xor):")
    print(f"  Excluded columns: {exclude_cols_2}")
    print(f"  Feature count: {len(feature_cols_2)}")
    print(f"  First 10 features: {feature_cols_2[:10]}")
    print(f"\nFor Model 3 (xgb_data_2 - all features):")
    print(f"  Excluded columns: {exclude_cols_3}")
    print(f"  Feature count: {len(feature_cols_3)}")
    print(f"  First 10 features: {feature_cols_3[:10]}")
    
    # 定义要对比的模型结果
    results = {}
    
    print("\n" + "="*80)
    print("Model Comparison: xgb_data_0 vs xgb_data_1 vs xgb_data_2")
    print(f"Test data: {data_path}")
    print(f"Model 1 (xgb_data_0): {len(feature_cols_1)} original features")
    print(f"Model 2 (xgb_data_1): {len(feature_cols_2)} features (all features except count_xor)")
    print(f"Model 3 (xgb_data_2): {len(feature_cols_3)} features (all features)")
    print("Loading pre-trained models and evaluating on test set")
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
    
    # 1. XGBoost Model 1 from xgb_data_0 (original features)
    print("\n[1/3] XGBoost Model 1 (xgb_data_0 - original features)")
    xgb_model_1 = load_xgb_model_from_rs_folder('xgb_data_0', args.target)
    if xgb_model_1 is None:
        print("  Please train the model first using train_0.py")
        return
    
    # 使用原始特征集（9个特征）
    X_1 = data[feature_cols_1].values
    print(f"  Using {len(feature_cols_1)} original features for prediction")
    print(f"  Features: {feature_cols_1}")
    
    # 验证特征数量
    try:
        # XGBoost 模型会检查特征数量
        test_pred = xgb_model_1.predict(X_1[:1])  # 测试单个样本
        print("  ✓ Feature count matches model expectations")
    except Exception as e:
        print(f"  ✗ Error: Feature validation failed: {e}")
        print(f"  Model expects {xgb_model_1.n_features_in_ if hasattr(xgb_model_1, 'n_features_in_') else 'unknown'} features")
        print(f"  Got {len(feature_cols_1)} features")
        return
    
    print("  Evaluating on test set...")
    y_pred_1 = xgb_model_1.predict(X_1)
    results['xgb_data_0 (original)'] = {
        'MAE': mean_absolute_error(y, y_pred_1),
        'MAPE': mape(y, y_pred_1),
        'RMSE': np.sqrt(mean_squared_error(y, y_pred_1)),
        'R²': r2_score(y, y_pred_1),
        'RRSE': rrse(y, y_pred_1),
    }
    print("  ✓ Model 1 (xgb_data_0) loaded and evaluated")
    
    # 2. XGBoost Model 2 from xgb_data_1 (all features except count_xor)
    print("\n[2/3] XGBoost Model 2 (xgb_data_1 - all features except count_xor)")
    xgb_model_2 = load_xgb_model_from_rs_folder('xgb_data_1', args.target)
    if xgb_model_2 is None:
        print("  Please train the model first using train_1.py")
        return
    
    # 使用所有特征集（排除 count_xor）
    X_2 = data[feature_cols_2].values
    print(f"  Using {len(feature_cols_2)} features for prediction")
    
    # 验证特征数量
    try:
        test_pred = xgb_model_2.predict(X_2[:1])  # 测试单个样本
        print("  ✓ Feature count matches model expectations")
    except Exception as e:
        print(f"  ✗ Error: Feature validation failed: {e}")
        if hasattr(xgb_model_2, 'n_features_in_'):
            print(f"  Model expects {xgb_model_2.n_features_in_} features")
            if hasattr(xgb_model_2, 'feature_names_in_') and xgb_model_2.feature_names_in_ is not None:
                print(f"  Model feature names: {list(xgb_model_2.feature_names_in_)}")
        print(f"  Got {len(feature_cols_2)} features")
        print(f"  Test data features: {feature_cols_2[:10]}...")
        return
    
    print("  Evaluating on test set...")
    y_pred_2 = xgb_model_2.predict(X_2)
    results['xgb_data_1 (no count_xor)'] = {
        'MAE': mean_absolute_error(y, y_pred_2),
        'MAPE': mape(y, y_pred_2),
        'RMSE': np.sqrt(mean_squared_error(y, y_pred_2)),
        'R²': r2_score(y, y_pred_2),
        'RRSE': rrse(y, y_pred_2),
    }
    print("  ✓ Model 2 (xgb_data_1) loaded and evaluated")
    
    # 3. XGBoost Model 3 from xgb_data_2 (all features)
    print("\n[3/3] XGBoost Model 3 (xgb_data_2 - all features)")
    xgb_model_3 = load_xgb_model_from_rs_folder('xgb_data_2', args.target)
    if xgb_model_3 is None:
        print("  Please train the model first using train_2.py")
        return
    
    # 使用所有特征集
    X_3 = data[feature_cols_3].values
    print(f"  Using {len(feature_cols_3)} features for prediction")
    
    # 验证特征数量
    try:
        test_pred = xgb_model_3.predict(X_3[:1])  # 测试单个样本
        print("  ✓ Feature count matches model expectations")
    except Exception as e:
        print(f"  ✗ Error: Feature validation failed: {e}")
        if hasattr(xgb_model_3, 'n_features_in_'):
            print(f"  Model expects {xgb_model_3.n_features_in_} features")
            if hasattr(xgb_model_3, 'feature_names_in_') and xgb_model_3.feature_names_in_ is not None:
                print(f"  Model feature names: {list(xgb_model_3.feature_names_in_)}")
        print(f"  Got {len(feature_cols_3)} features")
        print(f"  Test data features: {feature_cols_3[:10]}...")
        return
    
    print("  Evaluating on test set...")
    y_pred_3 = xgb_model_3.predict(X_3)
    results['xgb_data_2 (all features)'] = {
        'MAE': mean_absolute_error(y, y_pred_3),
        'MAPE': mape(y, y_pred_3),
        'RMSE': np.sqrt(mean_squared_error(y, y_pred_3)),
        'R²': r2_score(y, y_pred_3),
        'RRSE': rrse(y, y_pred_3),
    }
    print("  ✓ Model 3 (xgb_data_2) loaded and evaluated")
    
    # 打印对比结果
    print("\n" + "="*80)
    print("Model Comparison Results")
    print(f"Test data: {data_path}")
    print(f"Model 1 (xgb_data_0): {len(feature_cols_1)} original features")
    print(f"Model 2 (xgb_data_1): {len(feature_cols_2)} features (all features except count_xor)")
    print(f"Model 3 (xgb_data_2): {len(feature_cols_3)} features (all features)")
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
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # 蓝色、橙色、绿色、红色
        
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
