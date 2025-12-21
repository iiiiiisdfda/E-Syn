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
            print(f"Error: Data file not found at {args.data}")
            print("Tried alternative paths but none exist.")
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

    X = df[feature_cols].values
    # 保存特征名称用于后续绘图
    feature_names = feature_cols
    
    # 选择目标变量
    if args.target == 'area':
        y = df['area'].values
    else:
        y = df['delay'].values

    print(f"\nExcluded columns: {exclude_cols}")
    print(f"Final feature count: {len(feature_cols)}")
    print(f"Feature columns: {feature_cols}")
    # Scale the features
    # scaler = StandardScaler()
    # X = scaler.fit_transform(X)

    # Split the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
    grid_search = GridSearchCV(estimator=model, param_grid=params, scoring='neg_mean_absolute_percentage_error', cv=kf, verbose=1)
    grid_search.fit(X,y)

    best_params = grid_search.best_params_
    print("Best parameters found:", best_params)

    # Train the model with the best parameters on the entire dataset for feature importance
    model_full = xgb.XGBRegressor(**best_params).fit(X_train, y_train)
    plot_importance(model_full)
    plt.savefig(f'feature_importance_{args.target}.png')

    # Performing permutation importance
    result = permutation_importance(
        model_full, X_train, y_train, n_repeats=10, random_state=42, n_jobs=2
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
    fig.savefig(f'permutation_importance_{args.target}.png')

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
    model_filename = f'xgb_best_model_{args.target}.model'
    model_full.save_model(model_filename)
    print(f"XGBoost model saved to '{model_filename}'")

    # 导出为 Rust 代码（用于 Rust 项目）
    code = m2c.export_to_rust(model_full)

    # write code in model.rs
    rust_filename = f'model_{args.target}.rs'
    with open(rust_filename, 'w') as f:
        f.write(code)
    print(f"Rust code exported to '{rust_filename}'")

if __name__ == "__main__":
    main()