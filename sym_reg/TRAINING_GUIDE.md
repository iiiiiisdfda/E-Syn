# 符号回归训练指南

## 准备数据

确保你已经生成了训练数据 CSV 文件：
- **MIG 数据**: `mig_circuit_analysis.csv`
- **AIG 数据**: `simple_circuit_analysis_large.csv`

## 训练步骤

### 1. 检查数据格式

```bash
cd /home/ice890425/E-Syn/sym_reg

# 查看数据
head mig_circuit_analysis.csv

# 检查数据统计
python -c "import pandas as pd; df = pd.read_csv('mig_circuit_analysis.csv'); print(df.describe()); print(f'\n数据行数: {len(df)}')"
```

### 2. 激活 conda 环境

```bash
conda activate esyn
```

### 3. 训练模型

**基本训练命令：**

```bash
# 使用默认模型（model 1）
python symbolic_reg.py --model 1

# 使用其他模型
python symbolic_reg.py --model 2
python symbolic_reg.py --model 3
python symbolic_reg.py --model 4
python symbolic_reg.py --model 5
python symbolic_reg.py --model 6
```

**训练参数说明：**
- `--model N`: 选择模型（1-6），不同模型有不同的超参数配置
- `--model-file PATH`: 用于验证已保存的模型
- `--validate`: 验证模式（需要配合 `--model-file` 使用）

### 4. 训练输出

训练过程中会显示：
- 数据加载信息
- 特征标准化后的值
- 训练进度（PySR 会自动显示）
- 最终评估指标：
  - **MSE** (Mean Squared Error): 均方误差
  - **MAE** (Mean Absolute Error): 平均绝对误差
  - **MAPE** (Mean Absolute Percentage Error): 平均绝对百分比误差
  - **RRSE** (Root Relative Squared Error): 根相对平方误差

### 5. 模型保存和加载

PySR 会自动保存模型。模型文件通常保存在当前目录，文件名类似：
- `hall_of_fame_*.pkl` - 最佳模型
- `equations_*.csv` - 所有发现的方程

**验证已保存的模型：**

```bash
python symbolic_reg.py --validate --model-file hall_of_fame_*.pkl
```

## 数据格式说明

### CSV 列格式

训练脚本期望的 CSV 格式：
```
+,!,*,&,ASTSize,ASTDepth,lev,power,area,delay
```

**特征列（X）：**
- `+`: OR 操作符数量（列 0）
- `!`: NOT 操作符数量（列 1）
- `*`: AND 操作符数量（列 2）
- `ASTSize`: AST 大小（列 4）
- `ASTDepth`: AST 深度（列 5）

**目标列（y）：**
- `delay`: 延迟（最后一列）

### 特征选择

当前配置（`symbolic_reg.py` 第 47 行）：
```python
X = df.iloc[:,[0, 1, 2, 4, 5]].to_numpy()  # +, !, *, ASTSize, ASTDepth
y = df.iloc[:, -1].to_numpy()              # delay
```

如果需要修改特征选择，编辑 `symbolic_reg.py` 第 47 行。

## 模型选择建议

根据 `symbolic_reg_model.py` 中的配置：

| 模型 | 特点 | 适用场景 |
|------|------|----------|
| **Model 1** | 快速训练，复杂度限制较低 | 快速测试，简单模型 |
| **Model 2** | 更多迭代，更严格的复杂度限制 | 平衡速度和精度 |
| **Model 3** | 更多迭代，中等复杂度 | 中等复杂度模型 |
| **Model 4** | 更多迭代，更高复杂度 | 复杂模型 |
| **Model 5** | 快速训练，高复杂度 | 快速复杂模型 |
| **Model 6** | 快速训练，低复杂度 | 快速简单模型 |

**推荐：**
- 初次训练：使用 `--model 1` 快速测试
- 正式训练：使用 `--model 2` 或 `--model 3`
- 复杂模型：使用 `--model 4`

## 训练时间估算

根据模型配置：
- **Model 1, 5, 6**: 较快（1000 次迭代）
- **Model 2, 3, 4**: 较慢（10,000,000 次迭代，但会提前停止）

实际训练时间取决于：
- 数据量大小
- 模型复杂度
- 硬件性能（CPU 核心数）

## 故障排除

### 问题 1: ModuleNotFoundError: No module named 'pysr'

```bash
# 安装 pysr
conda activate esyn
pip install pysr

# 如果失败，可能需要先安装 Julia
conda install -c conda-forge julia -y
```

### 问题 2: 数据文件不存在

确保 CSV 文件在 `sym_reg/` 目录下：
```bash
ls -lh mig_circuit_analysis.csv
```

### 问题 3: 特征列不匹配

检查 CSV 列名：
```bash
python -c "import pandas as pd; df = pd.read_csv('mig_circuit_analysis.csv'); print(df.columns.tolist())"
```

如果列顺序不同，修改 `symbolic_reg.py` 第 47 行的索引。

### 问题 4: 训练时间过长

- 使用较小的模型（model 1, 5, 6）
- 减少数据量（在 CSV 中只保留部分行）
- 调整 `symbolic_reg_model.py` 中的 `niterations` 参数

## 完整训练示例

```bash
# 1. 进入目录
cd /home/ice890425/E-Syn/sym_reg

# 2. 激活环境
conda activate esyn

# 3. 检查数据
head mig_circuit_analysis.csv

# 4. 开始训练（使用 model 1 快速测试）
python symbolic_reg.py --model 1

# 5. 查看结果
# 训练完成后会显示 MSE, MAE, MAPE, RRSE
# 模型文件会保存在当前目录
```

## 下一步

训练完成后：
1. 查看评估指标（MSE, MAE, MAPE, RRSE）
2. 检查保存的模型文件
3. 使用 `--validate` 验证模型
4. 根据结果调整模型参数或数据



