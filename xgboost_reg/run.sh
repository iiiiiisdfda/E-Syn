#!/bin/bash

# 一键运行所有模型训练和比较的脚本
# 用法: ./run.sh [--data CSV_PATH] [--target area|delay] [--eval-data EVAL_CSV_PATH] [--skip-comparison] [--cpu]

set -e  # 遇到错误立即退出

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 解析命令行参数
DATA_PATH="../sym_reg/large_50000_filtered.csv"
TARGET="area"
EVAL_DATA_PATH="../sym_reg/large_10000_filtered.csv"
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
            echo "                         (default: ../sym_reg/new_10000.csv)"
            echo "  --skip-comparison      Skip model comparison step"
            echo "  --cpu                  Force CPU mode for MLP training"
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

echo "=========================================="
echo "One-Click Model Training and Comparison"
echo "=========================================="
echo "Working directory: $SCRIPT_DIR"
echo "Training data: $DATA_PATH"
echo "Evaluation data: $EVAL_DATA_PATH"
echo "Target variable: $TARGET"
echo ""

# 检查 train_all.sh 是否存在
if [ ! -f "train_all.sh" ]; then
    echo "✗ Error: train_all.sh not found in $SCRIPT_DIR"
    exit 1
fi

# 构建参数
ARGS="--data \"$DATA_PATH\" --target \"$TARGET\" --eval-data \"$EVAL_DATA_PATH\""
if [ "$SKIP_COMPARISON" = true ]; then
    ARGS="$ARGS --skip-comparison"
fi
if [ "$USE_CPU" = true ]; then
    ARGS="$ARGS --cpu"
fi

# 运行 train_all.sh
echo "Starting training pipeline..."
echo ""
eval ./train_all.sh $ARGS

echo ""
echo "=========================================="
echo "All tasks completed!"
echo "=========================================="

