import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import os
import argparse
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

# 评估指标函数
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))


def load_xgb_model_from_rs_folder(folder_path, target):
    """从文件夹中加载 XGBoost 模型（优先使用 .model 文件）"""
    model_path = os.path.join(folder_path, f'xgb_best_model_{target}.model')
    
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
    else:
        print(f"  ✗ Error: Model file not found in {folder_path}")
        print(f"  Expected: {model_path}")
        return None


def main():
    parser = argparse.ArgumentParser(description='Compare xgb_data_0 (original features) vs xgb_data_2 (all features)')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    args = parser.parse_args()
    
    # 定义测试数据文件
    test_file_0 = '../sym_reg/original_feature_test.csv'  # xgb_data_0 的测试文件
    test_file_2 = '../sym_reg/large_10000_filtered.csv'     # xgb_data_2 的测试文件
    
    # 创建输出文件夹
    output_dir = 'feature_comparison_results'
    os.makedirs(output_dir, exist_ok=True)
    
    results = {}
    
    print("="*80)
    print("Model Comparison: xgb_data_0 vs xgb_data_2")
    print(f"Target: {args.target}")
    print("="*80)
    
    # ========== Model 1: xgb_data_0 (original features) ==========
    print("\n[1/2] XGBoost Model 1 (xgb_data_0 - original features)")
    print(f"Test data: {test_file_0}")
    
    if not os.path.exists(test_file_0):
        print(f"  ✗ Error: Test data file not found at {test_file_0}")
        return
    
    # 加载测试数据
    data_0 = pd.read_csv(test_file_0)
    print(f"  Data shape: {data_0.shape}")
    print(f"  Data columns: {data_0.columns.tolist()}")
    
    # 选择目标变量
    if args.target == 'area':
        y_0 = data_0['area'].values
    else:
        y_0 = data_0['delay'].values
    
    # 准备原始特征
    original_features = ['ASTSize', 'ASTDepth', '+', '!', '*', '&', 'SUM_LIB', 'SUM_NODE', 'AVE_LIB']
    available_original_features = [col for col in original_features if col in data_0.columns]
    missing_original = [col for col in original_features if col not in data_0.columns]
    
    if missing_original:
        print(f"  ⚠️  Warning: Some original features are missing: {missing_original}")
    
    if len(available_original_features) == 0:
        print("  ✗ Error: No original E-Syn features found in the data!")
        return
    
    feature_cols_0 = available_original_features
    print(f"  Using {len(feature_cols_0)} original features: {feature_cols_0}")
    
    # 加载模型
    xgb_model_0 = load_xgb_model_from_rs_folder('xgb_data_0', args.target)
    if xgb_model_0 is None:
        print("  Please train the model first using train_0.py")
        return
    
    # 准备特征数据
    X_0 = data_0[feature_cols_0].values
    
    # 验证特征数量
    try:
        test_pred = xgb_model_0.predict(X_0[:1])
        print("  ✓ Feature count matches model expectations")
    except Exception as e:
        print(f"  ✗ Error: Feature validation failed: {e}")
        if hasattr(xgb_model_0, 'n_features_in_'):
            print(f"  Model expects {xgb_model_0.n_features_in_} features")
        print(f"  Got {len(feature_cols_0)} features")
        return
    
    # 评估模型
    print("  Evaluating on test set...")
    y_pred_0 = xgb_model_0.predict(X_0)
    results['xgb_data_0 (original)'] = {
        'MAE': mean_absolute_error(y_0, y_pred_0),
        'MAPE': mape(y_0, y_pred_0),
        'RMSE': np.sqrt(mean_squared_error(y_0, y_pred_0)),
        'R²': r2_score(y_0, y_pred_0),
        'RRSE': rrse(y_0, y_pred_0),
        'Test File': test_file_0,
        'Feature Count': len(feature_cols_0)
    }
    print("  ✓ Model 1 (xgb_data_0) evaluated")
    
    # ========== Model 2: xgb_data_2 (all features) ==========
    print("\n[2/2] XGBoost Model 2 (xgb_data_2 - all features)")
    print(f"Test data: {test_file_2}")
    
    if not os.path.exists(test_file_2):
        print(f"  ✗ Error: Test data file not found at {test_file_2}")
        return
    
    # 加载测试数据
    data_2 = pd.read_csv(test_file_2)
    print(f"  Data shape: {data_2.shape}")
    print(f"  Data columns: {data_2.columns.tolist()}")
    
    # 选择目标变量
    if args.target == 'area':
        y_2 = data_2['area'].values
    else:
        y_2 = data_2['delay'].values
    
    # 准备所有特征（排除基本列）
    exclude_cols_2 = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
    exclude_cols_2 = [col for col in exclude_cols_2 if col in data_2.columns]
    feature_cols_2 = [col for col in data_2.columns if col not in exclude_cols_2]
    
    print(f"  Excluded columns: {exclude_cols_2}")
    print(f"  Using {len(feature_cols_2)} features")
    print(f"  First 10 features: {feature_cols_2[:10]}")
    
    # 加载模型
    xgb_model_2 = load_xgb_model_from_rs_folder('xgb_data_2', args.target)
    if xgb_model_2 is None:
        print("  Please train the model first using train_2.py")
        return
    
    # 准备特征数据
    X_2 = data_2[feature_cols_2].values
    
    # 验证特征数量
    try:
        test_pred = xgb_model_2.predict(X_2[:1])
        print("  ✓ Feature count matches model expectations")
    except Exception as e:
        print(f"  ✗ Error: Feature validation failed: {e}")
        if hasattr(xgb_model_2, 'n_features_in_'):
            print(f"  Model expects {xgb_model_2.n_features_in_} features")
            if hasattr(xgb_model_2, 'feature_names_in_') and xgb_model_2.feature_names_in_ is not None:
                print(f"  Model feature names: {list(xgb_model_2.feature_names_in_)}")
        print(f"  Got {len(feature_cols_2)} features")
        return
    
    # 评估模型
    print("  Evaluating on test set...")
    y_pred_2 = xgb_model_2.predict(X_2)
    results['xgb_data_2 (all features)'] = {
        'MAE': mean_absolute_error(y_2, y_pred_2),
        'MAPE': mape(y_2, y_pred_2),
        'RMSE': np.sqrt(mean_squared_error(y_2, y_pred_2)),
        'R²': r2_score(y_2, y_pred_2),
        'RRSE': rrse(y_2, y_pred_2),
        'Test File': test_file_2,
        'Feature Count': len(feature_cols_2)
    }
    print("  ✓ Model 2 (xgb_data_2) evaluated")
    
    # ========== 打印对比结果 ==========
    print("\n" + "="*80)
    print("Model Comparison Results")
    print(f"Target: {args.target}")
    print("="*80)
    
    # 创建结果 DataFrame
    comparison_df = pd.DataFrame(results).T
    # 只保留评估指标列用于显示和保存
    metric_cols = ['MAE', 'MAPE', 'RMSE', 'R²', 'RRSE']
    display_df = comparison_df[metric_cols + ['Test File', 'Feature Count']]
    
    # 格式化输出
    print(f"\n{'Model':<25} {'MAE':<12} {'MAPE (%)':<12} {'RRSE':<12} {'R²':<12} {'RMSE':<12}")
    print("-" * 100)
    
    for model_name in display_df.index:
        metrics = results[model_name]
        print(f"{model_name:<25} "
              f"{metrics['MAE']:>10.2f}  "
              f"{metrics['MAPE']:>10.2f}  "
              f"{metrics['RRSE']:>10.4f}  "
              f"{metrics['R²']:>10.4f}  "
              f"{metrics['RMSE']:>10.2f}")
    
    # 保存结果到 CSV
    csv_filename = os.path.join(output_dir, f'feature_comparison_results_{args.target}.csv')
    display_df.to_csv(csv_filename)
    print(f"\nResults saved to '{csv_filename}'")
    
    # ========== 绘制 MAPE 对比图 ==========
    print("\nGenerating MAPE comparison plot...")
    try:
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        
        # 准备数据
        model_names = list(comparison_df.index)
        mape_values = [results[name]['MAPE'] for name in model_names]
        
        # 创建条形图
        colors = ['#1f77b4', '#ff7f0e']  # 蓝色、橙色
        bars = ax.barh(model_names, mape_values, color=colors)
        
        # 添加数值标签
        for i, (bar, value) in enumerate(zip(bars, mape_values)):
            ax.text(value, i, f' {value:.2f}%', 
                   va='center', ha='left', fontsize=12, fontweight='bold')
        
        ax.set_xlabel('MAPE (%)', fontsize=12)
        ax.set_title(f'Model Comparison: MAPE ({args.target.capitalize()})', fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        
        # 反转 y 轴，使数值小的在上方
        ax.invert_yaxis()
        
        plt.tight_layout()
        plot_filename = os.path.join(output_dir, f'feature_comparison_mape_{args.target}.png')
        plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
        print(f"MAPE comparison plot saved to '{plot_filename}'")
        plt.close()
        
    except Exception as e:
        print(f"Warning: Could not create MAPE plot: {e}")
        import traceback
        traceback.print_exc()
    
    # ========== 总结 ==========
    print("\n" + "="*80)
    print("Summary:")
    print("="*80)
    best_model_mape = comparison_df['MAPE'].idxmin()
    best_mape = comparison_df.loc[best_model_mape, 'MAPE']
    print(f"Best model by MAPE: {best_model_mape} (MAPE: {best_mape:.2f}%)")
    print("="*80)


if __name__ == "__main__":
    main()
