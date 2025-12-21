#!/usr/bin/env python3
"""
简单的脚本：读取 Random Forest 模型并转换为 Rust 代码
用法: python convert_rf_to_rust.py [--model MODEL_PATH] [--output OUTPUT_PATH]
"""

import argparse
import joblib
import m2cgen as m2c
import os

def main():
    parser = argparse.ArgumentParser(description='Convert Random Forest model to Rust code')
    parser.add_argument('--model', type=str, default='rf_best_model.pkl',
                        help='Path to the saved RF model file (default: rf_best_model.pkl)')
    parser.add_argument('--output', type=str, default='rf_model.rs',
                        help='Output Rust file path (default: rf_model.rs)')
    args = parser.parse_args()
    
    # 检查模型文件是否存在
    if not os.path.exists(args.model):
        print(f"✗ Error: Model file not found: {args.model}")
        print(f"Please train the model first using RF_train.py")
        return
    
    print(f"Loading Random Forest model from: {args.model}")
    try:
        # 加载模型
        checkpoint = joblib.load(args.model)
        model = checkpoint['model']
        
        print(f"✓ Model loaded successfully")
        print(f"  Model type: {type(model).__name__}")
        print(f"  Number of trees: {model.n_estimators}")
        print(f"  Number of features: {model.n_features_in_}")
        
        # 导出为 Rust 代码
        print(f"\nConverting to Rust code...")
        rust_code = m2c.export_to_rust(model)
        
        # 写入文件
        with open(args.output, 'w') as f:
            f.write(rust_code)
        
        print(f"✓ Rust code exported to: {args.output}")
        print(f"  File size: {os.path.getsize(args.output) / 1024:.2f} KB")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return

if __name__ == "__main__":
    main()

