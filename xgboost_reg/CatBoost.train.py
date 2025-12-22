import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
import m2cgen as m2c
import os
import argparse
import joblib

# 评估指标函数（与 train.py 保持一致）
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))

def r(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]

def generate_catboost_rust_code(model, feature_names, target_name):
    """
    手动生成 CatBoost 模型的 Rust 代码
    提取树结构并转换为 Rust 代码
    """
    rust_code = []
    rust_code.append("// Auto-generated CatBoost model code")
    rust_code.append("// This code implements a CatBoost regression model")
    rust_code.append(f"// Target: {target_name}")
    rust_code.append(f"// Number of features: {len(feature_names)}")
    rust_code.append("")
    rust_code.append("pub struct CatBoostModel {")
    rust_code.append("    // Model parameters embedded in predict function")
    rust_code.append("}")
    rust_code.append("")
    rust_code.append("impl CatBoostModel {")
    rust_code.append("    pub fn new() -> Self {")
    rust_code.append("        CatBoostModel {}")
    rust_code.append("    }")
    rust_code.append("")
    rust_code.append("    pub fn predict(&self, features: &[f64]) -> f64 {")
    rust_code.append(f"        assert_eq!(features.len(), {len(feature_names)});")
    rust_code.append("")
    rust_code.append("        // CatBoost uses sum of tree predictions")
    rust_code.append("        let mut result = 0.0;")
    rust_code.append("")
    
    # 获取模型信息并提取树结构
    try:
        tree_count = model.tree_count_
        rust_code.append(f"        // Number of trees: {tree_count}")
        rust_code.append("")
        
        # 提取所有树的结构
        trees_implemented = 0
        for tree_idx in range(tree_count):
            try:
                tree = model.get_tree(tree_idx)
                # 提取树结构
                tree_code = _extract_tree_structure(tree, tree_idx, feature_names)
                if tree_code:
                    rust_code.append(f"        result += self.tree_{tree_idx}(features);")
                    trees_implemented += 1
                    if trees_implemented >= 50:  # 限制生成的树数量，避免文件过大
                        rust_code.append(f"        // ... ({tree_count - trees_implemented} more trees)")
                        break
            except Exception as e:
                # 如果无法提取单棵树，跳过
                continue
        
        if trees_implemented == 0:
            rust_code.append("        // Tree extraction failed, using template")
            rust_code.append("        result += self.tree_0(features);")
        
    except Exception as e:
        # 如果无法获取树信息，生成通用模板
        rust_code.append("        // Tree structure extraction failed, using template")
        rust_code.append("        result += self.tree_0(features);")
    
    rust_code.append("")
    rust_code.append("        result")
    rust_code.append("    }")
    rust_code.append("")
    
    # 生成实际的树函数
    try:
        tree_count = model.tree_count_
        trees_generated = 0
        for tree_idx in range(min(tree_count, 50)):  # 限制前50棵树
            try:
                tree = model.get_tree(tree_idx)
                tree_func = _generate_tree_function(tree, tree_idx, feature_names)
                if tree_func:
                    rust_code.append(tree_func)
                    rust_code.append("")
                    trees_generated += 1
            except Exception as e:
                continue
        
        if trees_generated == 0:
            # 生成模板树函数
            rust_code.append("    // Tree prediction function (template)")
            rust_code.append("    fn tree_0(&self, features: &[f64]) -> f64 {")
            rust_code.append("        // TODO: Extract actual tree structure")
            rust_code.append("        // Use: tree = model.get_tree(0)")
            rust_code.append("        0.0")
            rust_code.append("    }")
    except Exception as e:
        # 生成模板
        rust_code.append("    // Tree prediction function (template)")
        rust_code.append("    fn tree_0(&self, features: &[f64]) -> f64 {")
        rust_code.append("        // TODO: Extract actual tree structure")
        rust_code.append("        0.0")
        rust_code.append("    }")
    
    rust_code.append("}")
    rust_code.append("")
    rust_code.append("// Note: This is a template. To extract full tree structure:")
    rust_code.append("// 1. Use CatBoost's get_tree() method to get tree structure")
    rust_code.append("// 2. Parse splits and leaf values")
    rust_code.append("// 3. Convert to Rust if-else statements")
    rust_code.append("")
    rust_code.append("// Alternative: Use catboost-portable crate:")
    rust_code.append("// use catboost_portable::Model;")
    rust_code.append(f"// let model = Model::load(\"catboost_best_model_{target_name}.cbm\")?;")
    rust_code.append("// let prediction = model.predict(&features)?;")
    
    return "\n".join(rust_code)

def _extract_tree_structure(tree, tree_idx, feature_names):
    """提取单棵树的结构信息（辅助函数）"""
    # CatBoost 树结构比较复杂，这里返回 None 表示使用模板
    # 实际实现需要解析 tree 对象的结构
    return None

def _generate_tree_function(tree, tree_idx, feature_names):
    """生成单棵树的 Rust 函数（辅助函数）"""
    # 尝试提取树结构
    try:
        func_code = []
        func_code.append(f"    fn tree_{tree_idx}(&self, features: &[f64]) -> f64 {{")
        
        # CatBoost 树是一个字典，包含 'splits', 'values' 等
        if isinstance(tree, dict):
            splits = tree.get('splits', [])
            values = tree.get('values', [])
            
            if splits and values:
                # 生成实际的树结构
                func_code.extend(_generate_tree_logic(splits, values, feature_names, 0, 0))
            else:
                func_code.append("        // Tree structure extraction incomplete")
                func_code.append("        0.0")
        else:
            # 如果 tree 不是字典，尝试其他方法
            try:
                # 尝试获取树的字符串表示
                tree_str = str(tree)
                func_code.append(f"        // Tree {tree_idx}: {len(tree_str)} chars")
                func_code.append("        // TODO: Parse tree structure manually")
                func_code.append("        0.0")
            except:
                func_code.append("        0.0")
        
        func_code.append("    }")
        return "\n".join(func_code)
    except Exception as e:
        # 生成模板
        func_code = []
        func_code.append(f"    fn tree_{tree_idx}(&self, features: &[f64]) -> f64 {{")
        func_code.append(f"        // Tree {tree_idx} - extraction failed: {str(e)[:50]}")
        func_code.append("        0.0")
        func_code.append("    }")
        return "\n".join(func_code)

def _generate_tree_logic(splits, values, feature_names, node_idx, indent_level):
    """递归生成树的逻辑代码"""
    code_lines = []
    indent = "        " + "    " * indent_level
    
    if node_idx >= len(values):
        code_lines.append(f"{indent}0.0")
        return code_lines
    
    # 如果是叶子节点
    if node_idx >= len(splits) or splits[node_idx] is None:
        value = values[node_idx] if node_idx < len(values) else 0.0
        code_lines.append(f"{indent}{value:.10e}")
        return code_lines
    
    # 获取分割信息
    split = splits[node_idx]
    if isinstance(split, dict):
        feature_idx = split.get('float_feature_index', split.get('feature_index', 0))
        border = split.get('border', 0.0)
        
        # 左子树（小于等于）
        left_idx = node_idx * 2 + 1
        # 右子树（大于）
        right_idx = node_idx * 2 + 2
        
        feature_name = feature_names[feature_idx] if feature_idx < len(feature_names) else f"features[{feature_idx}]"
        code_lines.append(f"{indent}if features[{feature_idx}] <= {border:.10e} {{")
        code_lines.extend(_generate_tree_logic(splits, values, feature_names, left_idx, indent_level + 1))
        code_lines.append(f"{indent}}} else {{")
        code_lines.extend(_generate_tree_logic(splits, values, feature_names, right_idx, indent_level + 1))
        code_lines.append(f"{indent}}}")
    else:
        # 如果分割格式不同，使用模板
        code_lines.append(f"{indent}// TODO: Parse split structure")
        code_lines.append(f"{indent}0.0")
    
    return code_lines

def main():
    parser = argparse.ArgumentParser(description='Train CatBoost model')
    parser.add_argument('--data', type=str, default='../sym_reg/feature1/10000.csv', help='Path to data file')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'], help='Target variable')
    args = parser.parse_args()
    
    # 读取数据
    data_path = args.data
    if not os.path.exists(data_path):
        alternative_paths = [
            '../sym_reg/new_50000.csv',
            '../sym_reg/mig_circuit_analysis.csv',
            '../sym_reg/simple_circuit_analysis_large.csv',
            'data.csv'
        ]
        for alt_path in alternative_paths:
            if os.path.exists(alt_path):
                data_path = alt_path
                print(f"Using alternative data path: {data_path}")
                break
        else:
            print(f"Error: Data file not found.")
            return
    
    df = pd.read_csv(data_path)
    print(f"Data shape: {df.shape}")
    print(f"Data columns: {df.columns.tolist()}")
    
    # 提取特征和目标
    # 明确排除目标变量和相关列，避免数据泄漏
    # 排除：lev, power, area, delay, gates, cap, and_gates
    exclude_cols = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
    # 只保留存在的列（避免某些列不存在时报错）
    exclude_cols = [col for col in exclude_cols if col in df.columns]
    feature_cols = [col for col in df.columns if col not in exclude_cols]
    
    print(f"\nExcluded columns: {exclude_cols}")
    print(f"Final feature count: {len(feature_cols)}")
    print(f"Feature columns: {feature_cols}")
    
    # 使用 DataFrame 而不是 values，这样 CatBoost 可以使用特征名称，避免警告
    X_df = df[feature_cols]
    # 保存特征名称用于后续绘图
    feature_names = feature_cols
    
    # 选择目标变量
    if args.target == 'area':
        y = df['area'].values
    else:
        y = df['delay'].values
    
    print(f"\nFeature shape: {X_df.shape}")
    print(f"Target shape: {y.shape}")
    print(f"Target: {args.target}")
    print(f"Target statistics: mean={np.mean(y):.2f}, std={np.std(y):.2f}, min={np.min(y):.2f}, max={np.max(y):.2f}")
    
    # 分割数据集（使用 DataFrame）
    X_train, X_test, y_train, y_test = train_test_split(X_df, y, test_size=0.2, random_state=42)
    print(f"\nTrain set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    
    # 定义超参数网格（简化，与 XGBoost 一致）
    param_grid = {
        'iterations': [100, 160, 200],  # 对应 XGBoost 的 n_estimators
        'depth': [3, 5, 10],  # 对应 XGBoost 的 max_depth
        'learning_rate': [0.01, 0.1, 0.2],  # 与 XGBoost 一致
        'random_state': [42],
        'verbose': [False],  # 减少输出
        'thread_count': [-1]  # 使用所有 CPU 核心
    }
    
    # 创建模型，禁用文件写入以避免并行冲突
    model = CatBoostRegressor(allow_writing_files=False)
    
    # 使用 KFold 交叉验证进行网格搜索
    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    print("\nStarting GridSearchCV with CatBoost...")
    print(f"Total parameter combinations: {np.prod([len(v) for v in param_grid.values()])}")
    
    # 减少并行度以避免文件写入冲突
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring='neg_mean_absolute_percentage_error',
        cv=kf,
        verbose=1,
        n_jobs=4  # 减少并行度，避免文件冲突
    )
    
    # 在训练集上进行网格搜索（交叉验证会自动分割），避免数据泄漏
    grid_search.fit(X_train, y_train)
    
    # 获取最佳参数
    best_params = grid_search.best_params_
    # sklearn 的 neg_mean_absolute_percentage_error 返回负数的小数形式（0-1），需要转换为百分比
    best_cv_mape = -grid_search.best_score_ * 100
    print("\n" + "="*80)
    print("Best parameters found:")
    print("="*80)
    for param, value in best_params.items():
        print(f"  {param}: {value}")
    print(f"\nBest Cross-Validation MAPE: {best_cv_mape:.2f}%")
    
    # 使用最佳参数在训练集上训练最终模型
    print("\nTraining final model with best parameters on training set...")
    # 从 best_params 中移除 allow_writing_files（如果存在），然后单独设置
    final_params = {k: v for k, v in best_params.items() if k != 'allow_writing_files'}
    best_model = CatBoostRegressor(**final_params, allow_writing_files=True)  # 最终训练时可以写入文件
    best_model.fit(X_train, y_train, verbose=False)
    
    # 在测试集上评估
    y_pred = best_model.predict(X_test)
    
    # 计算评估指标
    test_mape = mape(y_test, y_pred)
    test_rrse = rrse(y_test, y_pred)
    test_r = r(y_test, y_pred)
    test_r2 = r2_score(y_test, y_pred)
    test_mae = mean_absolute_error(y_test, y_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print("\n" + "="*80)
    print("Test Set Evaluation Metrics:")
    print("="*80)
    print(f"Mean Absolute Percentage Error (MAPE): {test_mape:.4f}%")
    print(f"Root Relative Square Error (RRSE): {test_rrse:.4f}")
    print(f"Correlation Coefficient (R): {test_r:.4f}")
    print(f"Coefficient of Determination (R²): {test_r2:.4f}")
    print(f"Mean Absolute Error (MAE): {test_mae:.4f}")
    print(f"RMSE (Root Mean Squared Error): {test_rmse:.4f}")
    print("="*80)
    
    # Permutation Importance
    # 注意：permutation_importance 需要数组格式，所以转换为 values
    print("\nComputing permutation importance...")
    perm_result = permutation_importance(
        best_model, X_train.values, y_train, n_repeats=10, random_state=42, n_jobs=-1
    )
    
    # 排序重要性
    sorted_importances_idx = perm_result.importances_mean.argsort()
    df_columns_sorted = [feature_names[i] for i in sorted_importances_idx]
    
    # 创建 DataFrame 用于绘图
    importances = pd.DataFrame(
        perm_result.importances[sorted_importances_idx].T,
        columns=df_columns_sorted,
    )
    
    # 创建输出文件夹
    output_dir = 'catboost_data'
    os.makedirs(output_dir, exist_ok=True)
    
    # 绘制 Permutation Importance
    fig, ax = plt.subplots(figsize=(10, 6))
    importances.plot.box(vert=False, whis=10, ax=ax)
    ax.set_title("CatBoost Permutation Importances (train set)")
    ax.axvline(x=0, color="k", linestyle="--")
    ax.set_xlabel("Decrease in accuracy score")
    fig.tight_layout()
    perm_importance_filename = os.path.join(output_dir, f'permutation_importance_{args.target}.png')
    fig.savefig(perm_importance_filename, dpi=300, bbox_inches='tight')
    print(f"Permutation importance plot saved to '{perm_importance_filename}'")
    
    # 保存 Permutation Importance 为 CSV
    perm_importance_df = pd.DataFrame({
        'feature': df_columns_sorted,
        'importance_mean': perm_result.importances_mean[sorted_importances_idx],
        'importance_std': perm_result.importances_std[sorted_importances_idx]
    })
    perm_importance_df = perm_importance_df.sort_values('importance_mean', ascending=False)
    perm_csv_filename = os.path.join(output_dir, f'permutation_importance_{args.target}.csv')
    perm_importance_df.to_csv(perm_csv_filename, index=False)
    print(f"Permutation importance CSV saved to '{perm_csv_filename}'")
    
    # 绘制预测 vs 真实值
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title(f'CatBoost Predictions vs True Values (R² = {test_r2:.4f})')
    plt.tight_layout()
    predictions_filename = os.path.join(output_dir, f'catboost_predictions_{args.target}.png')
    plt.savefig(predictions_filename, dpi=300, bbox_inches='tight')
    print(f"Predictions plot saved to '{predictions_filename}'")
    
    # 保存模型
    model_filename = os.path.join(output_dir, f'catboost_best_model_{args.target}.pkl')
    joblib.dump({
        'model': best_model,
        'best_params': best_params,
        'feature_names': feature_names,
        'target': args.target,
        'input_dim': X_train.shape[1]
    }, model_filename)
    print(f"\nModel saved to '{model_filename}'")
    print(f"To load the model, use: joblib.load('{model_filename}')")
    
    # 导出为 Rust 可用的格式
    print("\n" + "="*80)
    print("Exporting Model for Rust Usage")
    print("="*80)
    
    # 1. 保存为 .cbm 格式（CatBoost 原生格式，可用于 Rust 绑定库）
    try:
        cbm_filename = os.path.join(output_dir, f'catboost_best_model_{args.target}.cbm')
        best_model.save_model(cbm_filename)
        print(f"✓ CatBoost model saved: '{cbm_filename}'")
        print("  Can be loaded by catboost-portable or catboost-rs in Rust")
    except Exception as e:
        print(f"⚠️  Could not save .cbm format: {e}")
    
    # 2. 尝试导出为 ONNX 格式（如果支持）
    try:
        onnx_filename = os.path.join(output_dir, f'catboost_best_model_{args.target}.onnx')
        best_model.save_model(onnx_filename, format='onnx')
        print(f"✓ ONNX model saved: '{onnx_filename}'")
        print("  Can be used with onnxruntime-rs in Rust")
    except Exception as e:
        # ONNX 可能不支持，这是正常的
        if 'onnx' not in str(e).lower() and 'format' not in str(e).lower():
            print(f"⚠️  Could not save ONNX format: {e}")
    
    # 3. 生成 Rust 代码（手动实现）
    print("\nGenerating Rust code (.rs file)...")
    try:
        rust_code = generate_catboost_rust_code(best_model, feature_names, args.target)
        rust_filename = os.path.join(output_dir, f'catboost_model_{args.target}.rs')
        with open(rust_filename, 'w') as f:
            f.write(rust_code)
        print(f"✓ Rust code template generated: '{rust_filename}'")
        print("  Note: This is a template. You need to extract tree structure manually.")
        print("  See comments in the .rs file for instructions.")
    except Exception as e:
        print(f"⚠️  Could not generate Rust code: {e}")
        import traceback
        traceback.print_exc()
    
    # 4. 尝试使用 m2cgen（虽然不支持，但尝试一下）
    print("\nAttempting m2cgen export (will likely fail)...")
    try:
        rust_code_m2c = m2c.export_to_rust(best_model)
        rust_filename_m2c = os.path.join(output_dir, f'catboost_model_m2cgen_{args.target}.rs')
        with open(rust_filename_m2c, 'w') as f:
            f.write(rust_code_m2c)
        print(f"✓ Rust code exported via m2cgen: '{rust_filename_m2c}'")
    except Exception as e:
        print(f"  m2cgen does not support CatBoost (expected): {e}")
    
    print("\n" + "="*80)
    print("Training completed successfully!")
    print("="*80)

if __name__ == "__main__":
    main()

