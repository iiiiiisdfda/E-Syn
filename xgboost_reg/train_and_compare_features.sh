#!/bin/bash
# Script to train models with different feature sets and compare their performance
# This script trains:
# 1. xgb_data_0: Model with original features only
# 2. xgb_data_2: Model with all features
# Then compares their performance using feature_comparision.py
# Target: area (fixed)

set -e  # Exit on error

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Fixed target: area
TARGET="area"

echo "=========================================="
echo "Feature Training and Comparison Script"
echo "Target: $TARGET"
echo "=========================================="
echo ""

# Step 1: Train model with original features (xgb_data_0)
echo "=========================================="
echo "Step 1/3: Training model with original features (xgb_data_0)"
echo "=========================================="
echo "Training data: ../sym_reg/original_feature_train.csv"
echo ""

python train_0.py --data ../sym_reg/original_feature_train.csv --target "$TARGET"

if [ $? -ne 0 ]; then
    echo "Error: Failed to train model with original features"
    exit 1
fi

echo ""
echo "✓ Model with original features trained successfully"
echo ""

# Step 2: Train model with all features (xgb_data_2)
echo "=========================================="
echo "Step 2/3: Training model with all features (xgb_data_2)"
echo "=========================================="
echo "Training data: ../sym_reg/large_50000_filtered.csv"
echo ""

python train_2.py --data ../sym_reg/large_50000_filtered.csv --target "$TARGET"

if [ $? -ne 0 ]; then
    echo "Error: Failed to train model with all features"
    exit 1
fi

echo ""
echo "✓ Model with all features trained successfully"
echo ""

# Step 3: Compare the two models
echo "=========================================="
echo "Step 3/3: Comparing model performance"
echo "=========================================="
echo "Test data for xgb_data_0: ../sym_reg/original_feature_test.csv"
echo "Test data for xgb_data_2: ../sym_reg/large_10000_filtered.csv"
echo ""

python feature_comparision.py --target "$TARGET"

if [ $? -ne 0 ]; then
    echo "Error: Failed to compare models"
    exit 1
fi

echo ""
echo "=========================================="
echo "Feature Training and Comparison Complete!"
echo "=========================================="
echo ""
echo "Results saved in: feature_comparison_results/"
echo "  - feature_comparison_results_${TARGET}.csv"
echo "  - feature_comparison_mape_${TARGET}.png"
echo ""
echo "Trained models saved in:"
echo "  - xgb_data_0/ (original features)"
echo "  - xgb_data_2/ (all features)"
echo ""

