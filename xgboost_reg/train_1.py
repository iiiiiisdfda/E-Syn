import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn import metrics
import m2cgen as m2c
from sklearn.inspection import permutation_importance
import argparse
import os

def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))

def r(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]

def main():
    parser = argparse.ArgumentParser(description='Train XGBoost model')
    parser.add_argument('--data', type=str, default='../sym_reg/simple_circuit_analysis_project_train_val.csv', help='Path to data file')
    # 注意：确保训练数据和测试数据使用相同的特征集
    # 如果使用 new_50000.csv (35 features)，测试时也要使用相同特征集
    # 如果使用 simple_circuit_analysis_project_train_val.csv (36 features)，测试时也要使用相同特征集
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    args = parser.parse_args()
    
    # 读取数据
    data_path = args.data
    if not os.path.exists(data_path):
        # 优先使用与测试数据相同格式的文件（36 features）
        alternative_paths = [
            '../sym_reg/simple_circuit_analysis_project_train_val.csv',  # 36 features
            '../sym_reg/simple_circuit_analysis_large.csv',  # 可能也是 36 features
            '../sym_reg/new_50000.csv',  # 35 features (不同格式)
            '../sym_reg/mig_circuit_analysis.csv',
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
    
    df = pd.read_csv(data_path)
    print(f"Data shape: {df.shape}")
    print(f"Data columns: {df.columns.tolist()}")

    # 提取特征和目标
    # 明确排除目标变量和相关列，避免数据泄漏
    # 排除：lev, power, area, delay, gates, cap, and_gates, count_xor
    exclude_cols = [
        'lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates', 'count_xor'    ]
    # 只保留存在的列（避免某些列不存在时报错）
    exclude_cols = [col for col in exclude_cols if col in df.columns]
    feature_cols = [col for col in df.columns if col not in exclude_cols]
    
    # 打印特征信息，提醒用户特征数量
    print(f"\n⚠️  Important: This model will be trained with {len(feature_cols)} features")
    print(f"   Make sure your test data has the same {len(feature_cols)} features!")

    # 使用 DataFrame 而不是 values，这样 XGBoost 可以保存特征名称
    X_df = df[feature_cols]
    # 保存特征名称用于后续绘图和模型保存
    feature_names = feature_cols
    
    # 选择目标变量
    if args.target == 'area':
        y = df['area'].values
    else:
        y = df['delay'].values

    print(f"\nExcluded columns: {exclude_cols}")
    print(f"Final feature count: {len(feature_cols)}")
    print(f"Feature columns: {feature_cols}")
    
    # 限制数据量：最多使用 50000 条（40000 训练 + 10000 验证）
    max_total_samples = 50000
    max_train_samples = 40000
    max_val_samples = 10000
    
    if len(X_df) > max_total_samples:
        print(f"\n⚠️  Data has {len(X_df)} samples, limiting to {max_total_samples} samples")
        # 打乱数据
        indices = np.random.RandomState(seed=42).permutation(len(X_df))
        selected_indices = indices[:max_total_samples]
        X_df = X_df.iloc[selected_indices].reset_index(drop=True)
        y = y[selected_indices]
        print(f"   Using {len(X_df)} samples for training and validation")
    
    # Split the dataset into train and validation sets
    # 使用 DataFrame 进行分割，保持特征名称
    # 确保训练集最多 40000，验证集 10000
    if len(X_df) >= max_total_samples:
        # 如果数据足够，使用固定数量
        train_size = max_train_samples
        X_train_df = X_df.iloc[:train_size].reset_index(drop=True)
        X_val_df = X_df.iloc[train_size:train_size+max_val_samples].reset_index(drop=True)
        y_train = y[:train_size]
        y_val = y[train_size:train_size+max_val_samples]
    else:
        # 如果数据不足，按比例分割
        val_ratio = max_val_samples / len(X_df) if len(X_df) > max_val_samples else 0.2
        X_train_df, X_val_df, y_train, y_val = train_test_split(
            X_df, y, test_size=val_ratio, random_state=42
        )
        # 限制训练集大小
        if len(X_train_df) > max_train_samples:
            X_train_df = X_train_df.iloc[:max_train_samples].reset_index(drop=True)
            y_train = y_train[:max_train_samples]
    
    # 为了兼容性，将验证集命名为 test
    X_test_df = X_val_df
    y_test = y_val
    # 转换为 numpy array 用于训练（XGBoost 也支持 DataFrame）
    X_train = X_train_df.values
    X_test = X_test_df.values

    params = {
        'max_depth': [3, 5, 10],
        'learning_rate': [0.01, 0.1, 0.2],
        'n_estimators': [100, 160, 200],
        'objective': ['reg:gamma'],
        'booster': ['gbtree'],
        'tree_method': ['hist'],  # 使用 hist 而不是 gpu_hist（已弃用）
        'device': ['cuda'],  # 新版本使用 device 参数
        'n_jobs': [-1],
        'seed': [123]
    }

    model = xgb.XGBRegressor()
    kf = KFold(n_splits=10, shuffle=True, random_state=0)
    # print data size
    print("X_train size:", X_train.shape)
    print("X_test size:", X_test.shape)
    # 使用 DataFrame 进行训练，这样模型会保存特征名称
    grid_search = GridSearchCV(estimator=model, param_grid=params, scoring='neg_mean_absolute_percentage_error', cv=kf, verbose=1)
    grid_search.fit(X_df, y)  # 使用 DataFrame 而不是 numpy array

    best_params = grid_search.best_params_
    print("Best parameters found:", best_params)

    # 创建输出文件夹
    output_dir = f'xgb_data_1'
    os.makedirs(output_dir, exist_ok=True)
    
    # Train the model with the best parameters on the entire dataset for feature importance
    # 使用 DataFrame 进行训练，这样模型会保存特征名称
    model_full = xgb.XGBRegressor(**best_params).fit(X_train_df, y_train)
    plot_importance(model_full)
    plt.savefig(os.path.join(output_dir, f'feature_importance_{args.target}.png'))

    # Performing permutation importance
    # 使用 DataFrame 进行 permutation importance，保持特征名称
    result = permutation_importance(
        model_full, X_train_df, y_train, n_repeats=10, random_state=42, n_jobs=2
    )

    # Sorting importances
    sorted_importances_idx = result.importances_mean.argsort()
    # 使用之前保存的特征名称
    df_columns_sorted = [feature_names[i] for i in sorted_importances_idx]

    # Creating DataFrame for plotting
    importances = pd.DataFrame(
        result.importances[sorted_importances_idx].T,
        columns=df_columns_sorted,
    )

    # Plotting the permutation importances
    ax = importances.plot.box(vert=False, whis=10)
    ax.set_title("Permutation Importances (train set)")
    ax.axvline(x=0, color="k", linestyle="--")
    ax.set_xlabel("Decrease in accuracy score")
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, f'permutation_importance_{args.target}.png'))
    
    # 保存 Permutation Importance 为 CSV
    perm_importance_df = pd.DataFrame({
        'feature': df_columns_sorted,
        'importance_mean': result.importances_mean[sorted_importances_idx],
        'importance_std': result.importances_std[sorted_importances_idx]
    })
    perm_importance_df = perm_importance_df.sort_values('importance_mean', ascending=False)
    perm_csv_filename = os.path.join(output_dir, f'permutation_importance_{args.target}.csv')
    perm_importance_df.to_csv(perm_csv_filename, index=False)
    print(f"Permutation importance CSV saved to '{perm_csv_filename}'")

    # Print the best score (mean absolute error)
    best_mape_score = -grid_search.best_score_
    print("Best Mean Percentage Absolute Error:", best_mape_score)

    #best_mape_score = -grid_search.best_score_

    y_pred = model_full.predict(X_test)
    print("Mean Absolute Error Percentage (MAPE):", metrics.mean_absolute_percentage_error(y_test, y_pred))
    print("Root Relative Square Error (RRSE):", rrse(y_test, y_pred))
    print("Correlation Coefficient (R):", r(y_test, y_pred))
    print("Coeff Determination (R^2):", metrics.r2_score(y_test, y_pred))
    print("Mean Absolute Error (MAE):", metrics.mean_absolute_error(y_test, y_pred))
    print("RMSE (Root Mean Squared Error):", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    # 保存 XGBoost 模型文件（用于 Python 加载）
    model_filename = os.path.join(output_dir, f'xgb_best_model_{args.target}.model')
    model_full.save_model(model_filename)
    print(f"XGBoost model saved to '{model_filename}'")

    # 导出为 Rust 代码（用于 Rust 项目）
    try:
        print("\nExporting model to Rust code...")
        code = m2c.export_to_rust(model_full)
        
        # write code in model.rs
        rust_filename = os.path.join(output_dir, f'model_{args.target}.rs')
        with open(rust_filename, 'w') as f:
            f.write(code)
        print(f"Rust code exported to '{rust_filename}'")
    except Exception as e:
        print(f"Warning: Could not export to Rust code: {e}")
    
    # 导出为 Python 代码（用于 Python 加载）
    try:
        print("\nExporting model to Python code...")
        py_code = m2c.export_to_python(model_full)
        
        # write code in xgb_model.py
        py_filename = os.path.join(output_dir, f'xgb_model_{args.target}.py')
        with open(py_filename, 'w') as f:
            f.write(py_code)
        print(f"Python code exported to '{py_filename}'")
    except Exception as e:
        print(f"Warning: Could not export to Python code: {e}")

if __name__ == "__main__":
    main()