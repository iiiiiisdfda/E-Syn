# E-Syn Regression Model Training and Usage

This document provides instructions for setting up the environment, training regression models, and using trained models in the E-Syn framework.

## 1. Setup

To set up the development environment, run the setup script:

```bash
./setup.sh
```

This script will:
1. Build the ABC tool
2. Install Python dependencies (including resolving sympy version conflicts)
3. Build all Rust projects (s-converter, analyzer, circuitparser, e-rewriter, infix2lisp, lisp2infix)

### Prerequisites

- **Conda** (required) - Install from https://docs.conda.io/en/latest/miniconda.html
- Python 3.x with pip
- Rust toolchain (install from https://www.rust-lang.org/tools/install)
- Make (for building ABC)

### Notes

- Conda is required for installing packages from `packages.txt`
- The script will automatically upgrade sympy to resolve dependency conflicts with torch
- All Rust projects will be built in release mode

## 2. How to Train Models

### 2.1 Prepare Training Data

<!-- This section will be filled in later -->

### 2.2 Train All Models

To train all regression models, first modify the input data path in `xgboost_reg/run.sh`:

```bash
cd xgboost_reg
# Edit run.sh to set your desired data path
# The current default settings can reproduce the results reported in the paper
./run.sh
```

The default data paths in `run.sh` are configured to reproduce the results reported in the paper:
- Training data: `../sym_reg/large_50000_filtered.csv`
- Evaluation data: `../sym_reg/large_10000_filtered.csv`
- Target: `area`

**Output:**
After training completes, the following results will be generated:

- **Trained models** (saved in respective directories):
  - `xgb_data_2/` - XGBoost model files and exports
  - `rf_data/` - Random Forest model files and exports
  - `lgbm_data/` - LightGBM model files and exports
  - `mlp_data/` - MLP model files and exports
  - `catboost_data/` - CatBoost model files and exports

- **Model comparison results** (in `xgboost_reg/` directory):
  - `model_comparison_results_area.csv` - Comparison metrics (MAE, MAPE, RMSE, R², RRSE) for all models
  - `model_comparison_area.png` - Visualization comparing all models across different metrics

Each model directory contains:
- Trained model files (`.model`, `.pth`, `.pkl`, `.cbm`)
- Feature importance plots
- Rust code exports (`.rs` files)
- Python code exports (`.py` files)


### 2.3 Feature Set Comparison

To train and compare models with different feature sets (original features vs. all features), use the feature comparison script:

```bash
cd xgboost_reg
./train_and_compare_features.sh 
```

This script will:
1. Train `xgb_data_0` model with original features only (using `../sym_reg/original_feature_train.csv`)
2. Train `xgb_data_2` model with all features (using `../sym_reg/large_50000_filtered.csv`)
3. Compare the two models using:
   - Test data for original features: `../sym_reg/original_feature_test.csv`
   - Test data for all features: `../sym_reg/large_10000_filtered.csv`

**Output:**
- Comparison results CSV: `feature_comparison_results/feature_comparison_results_area.csv`
- MAPE comparison plot: `feature_comparison_results/feature_comparison_mape_area.png`
- Trained models: `xgb_data_0/` and `xgb_data_2/`


## 3. How to Use Trained Models in E-Syn

<!-- This section will be filled in later -->

