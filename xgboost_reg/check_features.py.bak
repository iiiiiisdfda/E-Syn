#!/usr/bin/env python3
import pandas as pd
import os

files = [
    '../sym_reg/simple_circuit_analysis_project_train_val.csv',
    '../sym_reg/new_50000.csv',
    '../sym_reg/mig_circuit_analysis.csv',
    '../sym_reg/simple_circuit_analysis_large.csv',
    '../sym_reg/simple_circuit_analysis_project_test.csv'
]

exclude = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']

# 检查 new_50000.csv (35 features) 和 test.csv (36 features) 的差异
new_file = '../sym_reg/new_50000.csv'
test_file = '../sym_reg/simple_circuit_analysis_project_test.csv'

if os.path.exists(new_file) and os.path.exists(test_file):
    new_df = pd.read_csv(new_file)
    test_df = pd.read_csv(test_file)
    
    new_exclude = [c for c in exclude if c in new_df.columns]
    test_exclude = [c for c in exclude if c in test_df.columns]
    
    new_features = [c for c in new_df.columns if c not in new_exclude]
    test_features = [c for c in test_df.columns if c not in test_exclude]
    
    print("="*80)
    print("Feature Comparison: new_50000.csv (35) vs test.csv (36)")
    print("="*80)
    
    print(f"\nnew_50000.csv features ({len(new_features)}):")
    for i, f in enumerate(new_features, 1):
        print(f"  {i:2d}. {f}")
    
    print(f"\ntest.csv features ({len(test_features)}):")
    for i, f in enumerate(test_features, 1):
        print(f"  {i:2d}. {f}")
    
    # 找出差异
    new_set = set(new_features)
    test_set = set(test_features)
    
    missing_in_new = test_set - new_set
    extra_in_new = new_set - test_set
    
    print(f"\n{'='*80}")
    print("Differences:")
    print(f"{'='*80}")
    
    if missing_in_new:
        print(f"\nFeatures in test.csv but NOT in new_50000.csv ({len(missing_in_new)}):")
        for f in sorted(missing_in_new):
            print(f"  - {f}")
    
    if extra_in_new:
        print(f"\nFeatures in new_50000.csv but NOT in test.csv ({len(extra_in_new)}):")
        for f in sorted(extra_in_new):
            print(f"  - {f}")

print("\n" + "="*80)
for f in files:
    if os.path.exists(f):
        df = pd.read_csv(f)
        exclude_cols = [c for c in exclude if c in df.columns]
        features = [c for c in df.columns if c not in exclude_cols]
        print(f'\n{f}:')
        print(f'  Total columns: {len(df.columns)}')
        print(f'  Excluded: {exclude_cols}')
        print(f'  Feature count: {len(features)}')

