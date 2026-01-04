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


### 2.3 Model Outputs

Trained models are saved in the following directories:
- `xgb_data_2/` - XGBoost 
- `rf_data/` - Random Forest
- `lgbm_data/` - LightGBM
- `mlp_data/` - MLP
- `catboost_data/` - CatBoost

Each directory contains:
- Trained model files (`.model`, `.pth`, `.pkl`, `.cbm`)
- Feature importance plots
- Permutation importance analysis
- Rust code exports (`.rs` files)

## 3. How to Use Trained Models in E-Syn

<!-- This section will be filled in later -->

