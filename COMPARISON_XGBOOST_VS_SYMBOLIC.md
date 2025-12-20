# XGBoost vs 符号回归对比

## 主要区别

### 1. **算法类型**

| 特性 | xgboost_reg | sym_reg |
|------|-------------|---------|
| **算法** | XGBoost (梯度提升树) | PySR (符号回归) |
| **类型** | 机器学习模型（黑盒） | 符号回归（可解释公式） |
| **库** | `xgboost` | `pysr` |

### 2. **模型输出**

**XGBoost (xgboost_reg):**
- 输出：决策树模型（黑盒）
- 保存格式：`.model` 文件
- 可以导出为 Rust 代码（`model.rs`）
- 无法直接看到数学公式

**符号回归 (sym_reg):**
- 输出：数学公式（可解释）
- 保存格式：`checkpoint.pkl` + `hall_of_fame.csv`
- 公式示例：`delay = cos2(cube(x1)) * x2 + 123.45`
- 可以直接看到和使用公式

### 3. **特征使用**

**XGBoost (xgboost_reg):**
```python
# train.py 第 22 行
X = df.iloc[:, :8].values  # 使用前 8 列特征
```

**符号回归 (sym_reg):**
```python
# symbolic_reg.py 第 49 行
X = df.iloc[:,[0, 1, 2, 4, 5]].to_numpy()  # +, !, *, ASTSize, ASTDepth
```

### 4. **目标变量**

**XGBoost (xgboost_reg):**
```python
# train.py 第 25 行
y = df['area'].values  # 可以预测 area 或 delay
# 或
# y = df['delay'].values
# y = (0.4 * df['area'] + 0.6 * df['delay']).values  # 组合目标
```

**符号回归 (sym_reg):**
```python
# symbolic_reg.py 第 55 行
y = df.iloc[:, -1].to_numpy()  # delay（最后一列）
```

### 5. **训练方式**

**XGBoost:**
- 使用 GridSearchCV 进行超参数搜索
- 10 折交叉验证
- 支持 GPU 加速（`tree_method: 'gpu_hist'`）
- 训练速度快

**符号回归:**
- 使用遗传算法搜索最佳公式
- 可以设置多个种群并行
- 需要 Julia 后端
- 训练时间较长（但会提前停止）

### 6. **模型文件位置**

**XGBoost 模型:**
- 保存位置：`xgboost_reg/` 目录
- 文件：`xgb_best_model.model`（如果使用 test.py）
- Rust 代码：`xgboost_reg/model.rs`

**符号回归模型:**
- 保存位置：`sym_reg/outputs/YYYYMMDD_HHMMSS_随机ID/`
- 文件：
  - `checkpoint.pkl` - 完整模型
  - `hall_of_fame.csv` - 所有发现的方程

### 7. **使用场景**

**XGBoost 适合：**
- 需要高精度预测
- 不需要解释模型
- 需要快速训练和预测
- 需要集成到 Rust 代码中

**符号回归适合：**
- 需要可解释的数学公式
- 需要理解特征之间的关系
- 需要将公式用于理论分析
- 需要简单的数学表达式

### 8. **评估指标**

两者都使用相同的评估指标：
- **MSE** (Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **MAPE** (Mean Absolute Percentage Error)
- **RRSE** (Root Relative Squared Error)

XGBoost 额外提供：
- **R²** (决定系数)
- **R** (相关系数)
- **特征重要性** (feature importance)

## 模型文件位置总结

### XGBoost 模型
```bash
cd /home/ice890425/E-Syn/xgboost_reg

# 模型文件（如果使用 test.py）
ls -lh xgb_best_model.model

# Rust 代码（如果使用 train.py）
ls -lh model.rs
```

### 符号回归模型
```bash
cd /home/ice890425/E-Syn/sym_reg

# 列出所有模型
ls -lh outputs/*/checkpoint.pkl

# 查看模型信息
python list_models.py
```

## 使用示例

### XGBoost 预测
```python
import xgboost as xgb

# 加载模型
model = xgb.Booster()
model.load_model('xgb_best_model.model')

# 预测
dtest = xgb.DMatrix(X_test)
preds = model.predict(dtest)
```

### 符号回归预测
```python
from pysr import PySRRegressor

# 加载模型
model = PySRRegressor.from_file('outputs/.../checkpoint.pkl')

# 预测
preds = model.predict(X_test)

# 查看公式
print(model.sympy())  # 数学公式
print(model.latex())  # LaTeX 格式
```

## 总结

| 特性 | XGBoost | 符号回归 |
|------|---------|----------|
| **可解释性** | ❌ 黑盒模型 | ✅ 数学公式 |
| **训练速度** | ✅ 快 | ⚠️ 较慢 |
| **预测精度** | ✅ 通常更高 | ⚠️ 取决于公式复杂度 |
| **特征数量** | ✅ 可以使用更多特征 | ⚠️ 特征数量有限制 |
| **部署** | ✅ 可导出为 Rust | ✅ 公式可直接使用 |
| **适用场景** | 生产环境，高精度需求 | 研究分析，需要解释 |

## 建议

- **如果只需要预测**：使用 XGBoost（更快、更准确）
- **如果需要理解关系**：使用符号回归（可解释的公式）
- **如果两者都需要**：可以同时训练两个模型，XGBoost 用于预测，符号回归用于分析



