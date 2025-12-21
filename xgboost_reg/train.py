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

def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))

def r(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]

df = pd.read_csv('../sym_reg/feature1/10000.csv')
# 排除最后3列（power, area, delay），使用前面的列作为特征
X = df.iloc[:, :-4].values
# 保存特征名称用于后续绘图
feature_names = df.columns[:-3].tolist()
#y = ( 0.4 * df['area'] + 0.6 * df['delay']).values
#y = df['delay'].values
y = df['area'].values
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
plt.savefig('feature_importance.png')

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
fig.savefig('permutation_importance.png')

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
model_full.save_model('xgb_best_model.model')
print("XGBoost model saved to 'xgb_best_model.model'")

# 导出为 Rust 代码（用于 Rust 项目）
code = m2c.export_to_rust(model_full)

# write code in model.rs
with open('model.rs', 'w') as f:
    f.write(code)
print("Rust code exported to 'model.rs'")