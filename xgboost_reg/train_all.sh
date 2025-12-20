#!/bin/bash

# 训练所有模型的脚本
# 依次训练 XGBoost、MLP、Random Forest

set -e  # 遇到错误立即退出

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================="
echo "Training All Models"
echo "=========================================="
echo "Working directory: $SCRIPT_DIR"
echo ""

# 记录开始时间
START_TIME=$(date +%s)

# 1. 训练 XGBoost 模型
echo "=========================================="
echo "[1/3] Training XGBoost Model"
echo "=========================================="
if [ -f "train.py" ]; then
    python train.py
    if [ $? -eq 0 ]; then
        echo "✓ XGBoost training completed successfully"
    else
        echo "✗ XGBoost training failed"
        exit 1
    fi
else
    echo "✗ Error: train.py not found"
    exit 1
fi
echo ""

# 2. 训练 MLP 模型
echo "=========================================="
echo "[2/3] Training MLP Model"
echo "=========================================="
if [ -f "MLP_train.py" ]; then
    python MLP_train.py
    if [ $? -eq 0 ]; then
        echo "✓ MLP training completed successfully"
    else
        echo "✗ MLP training failed"
        exit 1
    fi
else
    echo "✗ Error: MLP_train.py not found"
    exit 1
fi
echo ""

# 3. 训练 Random Forest 模型
echo "=========================================="
echo "[3/3] Training Random Forest Model"
echo "=========================================="
if [ -f "RF_train.py" ]; then
    python RF_train.py
    if [ $? -eq 0 ]; then
        echo "✓ Random Forest training completed successfully"
    else
        echo "✗ Random Forest training failed"
        exit 1
    fi
else
    echo "✗ Error: RF_train.py not found"
    exit 1
fi
echo ""

# 计算总耗时
END_TIME=$(date +%s)
ELAPSED_TIME=$((END_TIME - START_TIME))
HOURS=$((ELAPSED_TIME / 3600))
MINUTES=$(((ELAPSED_TIME % 3600) / 60))
SECONDS=$((ELAPSED_TIME % 60))

echo "=========================================="
echo "All Models Training Completed!"
echo "=========================================="
echo "Total time: ${HOURS}h ${MINUTES}m ${SECONDS}s"
echo ""

# 检查生成的模型文件
echo "Generated model files:"
if [ -f "xgb_best_model.model" ]; then
    echo "  ✓ xgb_best_model.model"
else
    echo "  ✗ xgb_best_model.model (not found)"
fi

if [ -f "mlp_model_complete.pth" ]; then
    echo "  ✓ mlp_model_complete.pth"
else
    echo "  ✗ mlp_model_complete.pth (not found)"
fi

if [ -f "rf_best_model.pkl" ]; then
    echo "  ✓ rf_best_model.pkl"
else
    echo "  ✗ rf_best_model.pkl (not found)"
fi

echo ""
echo "=========================================="
echo "Training Summary"
echo "=========================================="
echo "You can now run model comparison:"
echo "  python model_comparision.py"
echo "=========================================="

