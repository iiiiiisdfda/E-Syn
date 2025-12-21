#!/bin/bash

# 训练所有模型的脚本
# 依次训练 XGBoost、Random Forest、LightGBM，然后进行模型比较
# 用法: ./train_all.sh [--data CSV_PATH] [--target area|delay] [--eval-data EVAL_CSV_PATH] [--skip-comparison]

set -e  # 遇到错误立即退出

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 解析命令行参数
DATA_PATH="../sym_reg/new_50000.csv"
TARGET="delay"
EVAL_DATA_PATH="../sym_reg/new_10000.csv"  # 如果为空，使用训练数据路径
SKIP_COMPARISON=false
USE_CPU=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --data)
            DATA_PATH="$2"
            shift 2
            ;;
        --target)
            TARGET="$2"
            shift 2
            ;;
        --eval-data)
            EVAL_DATA_PATH="$2"
            shift 2
            ;;
        --skip-comparison)
            SKIP_COMPARISON=true
            shift
            ;;
        --cpu)
            USE_CPU=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --data CSV_PATH         Path to CSV data file for training (default: ../sym_reg/new_50000.csv)"
            echo "  --target TARGET        Target variable: 'area' or 'delay' (default: area)"
            echo "  --eval-data CSV_PATH   Path to CSV data file for evaluation/comparison"
            echo "                         (default: same as --data if not specified)"
            echo "  --skip-comparison      Skip model comparison step"
            echo "  --cpu                  Force CPU mode for MLP training (useful if GPU causes segmentation fault)"
            echo "  -h, --help            Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# 如果未指定评估数据路径，使用训练数据路径
if [ -z "$EVAL_DATA_PATH" ]; then
    EVAL_DATA_PATH="$DATA_PATH"
fi

echo "=========================================="
echo "Training All Models"
echo "=========================================="
echo "Working directory: $SCRIPT_DIR"
echo "Training data file: $DATA_PATH"
echo "Evaluation data file: $EVAL_DATA_PATH"
echo "Target variable: $TARGET"
echo ""

# 检查数据文件是否存在
if [ ! -f "$DATA_PATH" ]; then
    echo "✗ Error: Data file not found: $DATA_PATH"
    exit 1
fi

# 记录开始时间
START_TIME=$(date +%s)

# 1. 训练 XGBoost 模型
echo "=========================================="
echo "[1/3] Training XGBoost Model"
echo "=========================================="
if [ -f "train.py" ]; then
    python train.py --data "$DATA_PATH" --target "$TARGET"
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

# 2. 训练 Random Forest 模型
echo "=========================================="
echo "[2/3] Training Random Forest Model"
echo "=========================================="
if [ -f "RF_train.py" ]; then
    python RF_train.py --data "$DATA_PATH" --target "$TARGET"
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

# 3. 训练 LightGBM 模型
echo "=========================================="
echo "[3/3] Training LightGBM Model"
echo "=========================================="
if [ -f "LightGBM_train.py" ]; then
    python LightGBM_train.py --data "$DATA_PATH" --target "$TARGET"
    if [ $? -eq 0 ]; then
        echo "✓ LightGBM training completed successfully"
    else
        echo "✗ LightGBM training failed"
        exit 1
    fi
else
    echo "✗ Error: LightGBM_train.py not found"
    exit 1
fi
echo ""

# 4. 模型比较（可选）
if [ "$SKIP_COMPARISON" = false ]; then
    echo "=========================================="
    echo "[4/4] Model Comparison"
    echo "=========================================="
    if [ -f "model_comparision.py" ]; then
        # 检查评估数据文件是否存在
        if [ ! -f "$EVAL_DATA_PATH" ]; then
            echo "✗ Warning: Evaluation data file not found: $EVAL_DATA_PATH"
            echo "  Skipping model comparison..."
        else
            python model_comparision.py --data "$EVAL_DATA_PATH" --target "$TARGET"
            if [ $? -eq 0 ]; then
                echo "✓ Model comparison completed successfully"
            else
                echo "✗ Model comparison failed"
                # 不退出，因为训练已经完成
            fi
        fi
    else
        echo "✗ Warning: model_comparision.py not found, skipping comparison"
    fi
    echo ""
fi

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
if [ -f "xgb_best_model_${TARGET}.model" ]; then
    echo "  ✓ xgb_best_model_${TARGET}.model"
else
    echo "  ✗ xgb_best_model_${TARGET}.model (not found)"
fi

if [ -f "rf_best_model_${TARGET}.pkl" ]; then
    echo "  ✓ rf_best_model_${TARGET}.pkl"
else
    echo "  ✗ rf_best_model_${TARGET}.pkl (not found)"
fi

if [ -f "lgbm_best_model_${TARGET}.pkl" ]; then
    echo "  ✓ lgbm_best_model_${TARGET}.pkl"
else
    echo "  ✗ lgbm_best_model_${TARGET}.pkl (not found)"
fi

echo ""
echo "=========================================="
echo "Training Summary"
echo "=========================================="
if [ "$SKIP_COMPARISON" = true ]; then
    echo "To run model comparison manually:"
    echo "  python model_comparision.py --data \"$EVAL_DATA_PATH\" --target \"$TARGET\""
else
    echo "Model comparison has been completed."
    if [ -f "model_comparison_results_${TARGET}.csv" ]; then
        echo "  Results saved to: model_comparison_results_${TARGET}.csv"
    fi
    if [ -f "model_comparison_${TARGET}.png" ]; then
        echo "  Plots saved to: model_comparison_${TARGET}.png"
    fi
fi
echo "=========================================="

