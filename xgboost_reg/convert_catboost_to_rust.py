#!/usr/bin/env python3
"""
简单的脚本：读取 CatBoost 模型并尝试转换为 Rust 代码
注意：m2cgen 目前不支持 CatBoost，此脚本会尝试转换并显示错误信息
用法: python convert_catboost_to_rust.py [--model MODEL_PATH] [--output OUTPUT_PATH] [--target TARGET]
"""

import argparse
import joblib
import m2cgen as m2c
import os

def main():
    parser = argparse.ArgumentParser(description='Convert CatBoost model to Rust code')
    parser.add_argument('--model', type=str, default='catboost_best_model_area.pkl',
                        help='Path to the saved CatBoost model file (default: catboost_best_model_area.pkl)')
    parser.add_argument('--output', type=str, default='catboost_model.rs',
                        help='Output Rust file path (default: catboost_model.rs)')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'],
                        help='Target variable: area or delay (default: area)')
    args = parser.parse_args()
    
    # 如果模型路径是默认值，尝试使用 target 后缀
    if args.model == 'catboost_best_model_area.pkl' and args.target != 'area':
        args.model = f'catboost_best_model_{args.target}.pkl'
    
    # 如果输出路径是默认值，使用 target 后缀
    if args.output == 'catboost_model.rs':
        args.output = f'catboost_model_{args.target}.rs'
    
    # 检查模型文件是否存在
    if not os.path.exists(args.model):
        print(f"✗ Error: Model file not found: {args.model}")
        print(f"Please train the model first using CatBoost_train.py")
        return
    
    print(f"Loading CatBoost model from: {args.model}")
    try:
        # 加载模型
        checkpoint = joblib.load(args.model)
        model = checkpoint['model']
        
        print(f"✓ Model loaded successfully")
        print(f"  Model type: {type(model).__name__}")
        print(f"  Number of iterations: {model.get_params().get('iterations', 'N/A')}")
        print(f"  Number of features: {model.feature_names_ if hasattr(model, 'feature_names_') else 'N/A'}")
        
        # 尝试导出为 Rust 代码
        print(f"\nAttempting to convert to Rust code...")
        print(f"Note: m2cgen may not support CatBoost models")
        
        try:
            rust_code = m2c.export_to_rust(model)
            
            # 写入文件
            with open(args.output, 'w') as f:
                f.write(rust_code)
            
            print(f"✓ Rust code exported to: {args.output}")
            print(f"  File size: {os.path.getsize(args.output) / 1024:.2f} KB")
            
        except Exception as e:
            print(f"✗ Error: Could not export to Rust code")
            print(f"  Reason: {e}")
            print(f"\n" + "="*80)
            print("CatBoost 无法直接转换为纯 Rust 代码")
            print("="*80)
            print("\nm2cgen 目前不支持 CatBoost 模型。")
            print("\n替代方案：")
            print("\n1. 【推荐】使用 CatBoost Rust 绑定库（运行时推理）")
            print("   - catboost-portable: https://crates.io/crates/catboost-portable")
            print("   - catboost-rs: https://crates.io/crates/catboost-rs")
            print("   使用方法：")
            print("     • 在 Cargo.toml 中添加: catboost-portable = \"0.1\"")
            print("     • 加载模型文件（.cbm 格式）进行推理")
            print("     • 注意：需要链接 CatBoost 的 C++ 库")
            print("\n2. 导出为 ONNX 格式")
            print("   • CatBoost 支持导出为 ONNX")
            print("   • 在 Rust 中使用 onnxruntime-rs 进行推理")
            print("   • 命令: model.save_model('model.onnx', format='onnx')")
            print("\n3. 使用 CatBoost C API via FFI")
            print("   • CatBoost 提供 C API")
            print("   • 在 Rust 中使用 FFI 调用")
            print("\n4. 使用 PyO3 调用 Python CatBoost")
            print("   • 在 Rust 中通过 PyO3 调用 Python 的 CatBoost API")
            print("   • 适合已有 Python 环境的场景")
            print("\n" + "="*80)
            print("\n建议：如果需要在 Rust 中使用 CatBoost，优先考虑方案 1（catboost-portable）")
            print("="*80)
            return
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return

if __name__ == "__main__":
    main()

