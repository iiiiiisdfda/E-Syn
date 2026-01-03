#!/usr/bin/env python3
"""检查 XGBoost 模型的特征数量"""

import sys
import os
sys.path.append('.')

try:
    import xgboost as xgb
    import pandas as pd
    
    model_path = 'xgb_data/xgb_best_model_area.model'
    if os.path.exists(model_path):
        print(f"Loading model from: {model_path}")
        model = xgb.XGBRegressor()
        model.load_model(model_path)
        
        # 检查特征数量
        if hasattr(model, 'n_features_in_'):
            print(f"Model n_features_in_: {model.n_features_in_}")
        else:
            print("Model does not have n_features_in_ attribute")
        
        if hasattr(model, 'feature_names_in_'):
            print(f"Model feature_names_in_: {model.feature_names_in_}")
            if model.feature_names_in_ is not None:
                print(f"Number of feature names: {len(model.feature_names_in_)}")
        else:
            print("Model does not have feature_names_in_ attribute")
        
        # 检查训练数据
        train_data_path = '../sym_reg/simple_circuit_analysis_project_train_val.csv'
        if os.path.exists(train_data_path):
            print(f"\nChecking training data: {train_data_path}")
            train_df = pd.read_csv(train_data_path)
            exclude_cols = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
            exclude_cols = [col for col in exclude_cols if col in train_df.columns]
            feature_cols = [col for col in train_df.columns if col not in exclude_cols]
            print(f"Training data - Total columns: {len(train_df.columns)}")
            print(f"Training data - Excluded columns: {exclude_cols}")
            print(f"Training data - Feature columns count: {len(feature_cols)}")
        
        # 检查测试数据
        test_data_path = '../sym_reg/simple_circuit_analysis_project_test.csv'
        if os.path.exists(test_data_path):
            print(f"\nChecking test data: {test_data_path}")
            test_df = pd.read_csv(test_data_path)
            exclude_cols = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
            exclude_cols = [col for col in exclude_cols if col in test_df.columns]
            feature_cols = [col for col in test_df.columns if col not in exclude_cols]
            print(f"Test data - Total columns: {len(test_df.columns)}")
            print(f"Test data - Excluded columns: {exclude_cols}")
            print(f"Test data - Feature columns count: {len(feature_cols)}")
            print(f"Test data - Feature columns: {feature_cols}")
    else:
        print(f"Model file not found: {model_path}")
        
except ImportError as e:
    print(f"Import error: {e}")
    print("Please install required packages: pip install xgboost pandas")

