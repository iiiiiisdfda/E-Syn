import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, TensorDataset
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
import os

# 评估指标函数（与 train.py 保持一致）
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rrse(y_true, y_pred):
    return np.sqrt(np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2))

def r(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]

# MLP 模型定义
class MLPRegressor(nn.Module):
    def __init__(self, input_dim, hidden_dims=[128, 64, 32], dropout_rate=0.2):
        super(MLPRegressor, self).__init__()
        layers = []
        prev_dim = input_dim
        
        for hidden_dim in hidden_dims:
            layers.append(nn.Linear(prev_dim, hidden_dim))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout_rate))
            prev_dim = hidden_dim
        
        # 输出层
        layers.append(nn.Linear(prev_dim, 1))
        self.model = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.model(x).squeeze()

# 训练函数
def train_model(model, train_loader, val_loader, epochs=200, lr=0.001, device='cuda', early_stop_patience=30):
    model = model.to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    # PyTorch 新版本移除了 verbose 参数
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=10)
    
    train_losses = []
    val_losses = []
    best_val_loss = float('inf')
    patience_counter = 0
    
    for epoch in range(epochs):
        # 训练阶段
        model.train()
        train_loss = 0.0
        for batch_x, batch_y in train_loader:
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)
            
            optimizer.zero_grad()
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
        
        # 验证阶段
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for batch_x, batch_y in val_loader:
                batch_x = batch_x.to(device)
                batch_y = batch_y.to(device)
                
                outputs = model(batch_x)
                loss = criterion(outputs, batch_y)
                val_loss += loss.item()
        
        train_loss /= len(train_loader)
        val_loss /= len(val_loader)
        train_losses.append(train_loss)
        val_losses.append(val_loss)
        
        scheduler.step(val_loss)
        
        # 早停机制
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            # 保存最佳模型（只保存 state_dict，不包含 sklearn 对象）
            torch.save(model.state_dict(), 'mlp_best_model.pth')
        else:
            patience_counter += 1
            if patience_counter >= early_stop_patience:
                print(f"Early stopping at epoch {epoch+1}")
                break
        
        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}")
    
    # 加载最佳模型（PyTorch 2.6+ 需要设置 weights_only=False）
    model.load_state_dict(torch.load('mlp_best_model.pth', weights_only=False))
    return model, train_losses, val_losses

# 预测函数
def predict(model, X, device='cuda', batch_size=256):
    model.eval()
    predictions = []
    
    with torch.no_grad():
        for i in range(0, len(X), batch_size):
            batch = X[i:i+batch_size]
            batch_tensor = torch.FloatTensor(batch).to(device)
            pred = model(batch_tensor).cpu().numpy()
            predictions.extend(pred)
    
    return np.array(predictions)

# 生成 MLP 模型的 Rust 代码
def generate_mlp_rust_code(model, model_params, scaler_mean, scaler_scale, feature_names):
    """生成 MLP 模型的 Rust 代码模板"""
    rust_code = []
    rust_code.append("// Auto-generated MLP model code")
    rust_code.append("// This code implements a Multi-Layer Perceptron regression model")
    rust_code.append("// Note: This is a template. You need to extract actual weights from the PyTorch model")
    rust_code.append("")
    rust_code.append("pub struct MLPModel {")
    rust_code.append("    // Model parameters will be embedded here")
    rust_code.append("}")
    rust_code.append("")
    rust_code.append("impl MLPModel {")
    rust_code.append("    pub fn new() -> Self {")
    rust_code.append("        MLPModel {}")
    rust_code.append("    }")
    rust_code.append("")
    rust_code.append("    pub fn predict(&self, features: &[f64]) -> f64 {")
    rust_code.append("        // Standardize features")
    rust_code.append(f"        assert_eq!(features.len(), {len(feature_names)});")
    rust_code.append("")
    
    # 添加标准化代码
    rust_code.append("        // Standardization: (x - mean) / scale")
    rust_code.append("        let mut standardized: Vec<f64> = Vec::new();")
    for i, (mean, scale) in enumerate(zip(scaler_mean, scaler_scale)):
        rust_code.append(f"        standardized.push((features[{i}] - {mean:.10e}) / {scale:.10e});")
    
    rust_code.append("")
    rust_code.append("        // Forward pass through the network")
    
    # 获取模型结构信息
    hidden_dims = model_params.get('hidden_dims', [128, 64, 32])
    input_dim = len(feature_names)
    
    rust_code.append(f"        let mut x = standardized;")
    rust_code.append("")
    
    # 为每一层生成代码模板
    prev_dim = input_dim
    for layer_idx, hidden_dim in enumerate(hidden_dims):
        rust_code.append(f"        // Layer {layer_idx + 1}: {prev_dim} -> {hidden_dim}")
        rust_code.append(f"        let mut layer_{layer_idx}_out = vec![0.0; {hidden_dim}];")
        rust_code.append(f"        for j in 0..{hidden_dim} {{")
        rust_code.append(f"            let mut sum = 0.0;")
        rust_code.append(f"            for i in 0..{prev_dim} {{")
        rust_code.append(f"                // TODO: Replace with actual weight: weights[{layer_idx}][j][i]")
        rust_code.append(f"                sum += x[i] * 0.0;")
        rust_code.append(f"            }}")
        rust_code.append(f"            // TODO: Add bias term")
        rust_code.append(f"            layer_{layer_idx}_out[j] = sum.max(0.0); // ReLU")
        rust_code.append(f"        }}")
        rust_code.append(f"        x = layer_{layer_idx}_out;")
        rust_code.append("")
        prev_dim = hidden_dim
    
    # 输出层
    rust_code.append(f"        // Output layer: {prev_dim} -> 1")
    rust_code.append(f"        let mut output = 0.0;")
    rust_code.append(f"        for i in 0..{prev_dim} {{")
    rust_code.append(f"            // TODO: Replace with actual weight: output_weights[i]")
    rust_code.append(f"            output += x[i] * 0.0;")
    rust_code.append(f"        }}")
    rust_code.append("        // TODO: Add output bias")
    rust_code.append("")
    rust_code.append("        output")
    rust_code.append("    }")
    rust_code.append("}")
    rust_code.append("")
    rust_code.append("// Instructions:")
    rust_code.append("// 1. Extract weights and biases from PyTorch model using:")
    rust_code.append("//    for name, param in model.named_parameters():")
    rust_code.append("//        print(f'{name}: {param.data}')")
    rust_code.append("// 2. Replace TODO comments with actual weight values")
    rust_code.append("// 3. Implement proper matrix multiplication")
    
    return "\n".join(rust_code)

# 主函数
def main(args=None):
    # 如果没有传入 args，使用默认值
    if args is None:
        class DefaultArgs:
            data = '../sym_reg/simple_circuit_analysis_project_train_val.csv'
            target = 'area'
            epochs = 300
            early_stop_patience = 30
            cpu = False
        args = DefaultArgs()
    
    # 设置设备
    if args.cpu:
        device = torch.device('cpu')
        print("Using CPU mode (--cpu flag set)")
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    print(f"Training epochs: {args.epochs}")
    print(f"Early stopping patience: {args.early_stop_patience}")
    
    # 读取数据
    data_path = args.data
    
    # 如果原路径不存在，尝试使用相对路径
    if not os.path.exists(data_path):
        # 尝试其他可能的路径
        alternative_paths = [
            '../sym_reg/mig_circuit_analysis.csv',
            '../sym_reg/simple_circuit_analysis_large.csv',
            'data.csv',
            '../sym_reg/aigfuzz_random/fuzz_circuit_analysis.csv'
        ]
        for alt_path in alternative_paths:
            if os.path.exists(alt_path):
                data_path = alt_path
                print(f"Using alternative data path: {data_path}")
                break
        else:
            print(f"Error: Data file not found: {args.data}")
            print(f"Tried paths: {data_path}, {alternative_paths}")
            print("\nPlease specify the data file path using --data argument.")
            return
    
    df = pd.read_csv(data_path)
    print(f"Data shape: {df.shape}")
    print(f"Data columns: {df.columns.tolist()}")
    
    # 提取特征和目标（与 train.py 相同）
    # 明确排除目标变量和相关列，避免数据泄漏
    # 排除：lev, power, area, delay, gates, cap, and_gates
    exclude_cols = ['lev', 'power', 'area', 'delay', 'gates', 'cap', 'and_gates']
    # 只保留存在的列（避免某些列不存在时报错）
    exclude_cols = [col for col in exclude_cols if col in df.columns]
    feature_cols = [col for col in df.columns if col not in exclude_cols]
    
    print(f"\nExcluded columns: {exclude_cols}")
    print(f"Final feature count: {len(feature_cols)}")
    print(f"Feature columns: {feature_cols}")
    
    X = df[feature_cols].values
    feature_names = feature_cols
    
    # 根据命令行参数选择目标变量
    if args.target == 'area':
        y = df['area'].values
    else:
        y = df['delay'].values
    
    print(f"Target variable: {args.target}")
    
    print(f"Feature shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    
    # 限制数据量：最多使用 50000 条（40000 训练 + 10000 验证）
    # 注意：测试集（5000）应从原始数据集中单独划分
    max_total_samples = 50000
    max_train_samples = 40000
    max_val_samples = 10000
    
    if len(X) > max_total_samples:
        print(f"\n⚠️  Data has {len(X)} samples, limiting to {max_total_samples} samples")
        # 打乱数据
        indices = np.random.RandomState(seed=42).permutation(len(X))
        selected_indices = indices[:max_total_samples]
        X = X[selected_indices]
        y = y[selected_indices]
        print(f"   Using {len(X)} samples for training and validation")
    
    # 数据标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 分割数据集：确保训练集最多 40000，验证集 10000
    if len(X_scaled) >= max_total_samples:
        # 如果数据足够，使用固定数量
        train_size = max_train_samples
        X_train = X_scaled[:train_size]
        X_val = X_scaled[train_size:train_size+max_val_samples]
        y_train = y[:train_size]
        y_val = y[train_size:train_size+max_val_samples]
        # 测试集使用剩余数据（如果有）
        if len(X_scaled) > train_size + max_val_samples:
            X_test = X_scaled[train_size+max_val_samples:]
            y_test = y[train_size+max_val_samples:]
        else:
            # 如果没有剩余数据，从验证集中分出一部分作为测试集
            test_size = min(2000, len(X_val) // 5)
            X_test = X_val[:test_size]
            y_test = y_val[:test_size]
            X_val = X_val[test_size:]
            y_val = y_val[test_size:]
    else:
        # 如果数据不足，按比例分割
        # 先分出测试集
        test_ratio = 0.2
        X_temp, X_test, y_temp, y_test = train_test_split(
            X_scaled, y, test_size=test_ratio, random_state=42
        )
        # 再从剩余数据中分出训练集和验证集
        val_ratio = max_val_samples / len(X_temp) if len(X_temp) > max_val_samples else 0.2
        X_train, X_val, y_train, y_val = train_test_split(
            X_temp, y_temp, test_size=val_ratio, random_state=42
        )
        # 限制训练集大小
        if len(X_train) > max_train_samples:
            X_train = X_train[:max_train_samples]
            y_train = y_train[:max_train_samples]
    
    print(f"Train size: {X_train.shape[0]}")
    print(f"Val size: {X_val.shape[0]}")
    print(f"Test size: {X_test.shape[0]}")
    
    # 转换为 PyTorch 张量
    train_dataset = TensorDataset(
        torch.FloatTensor(X_train),
        torch.FloatTensor(y_train)
    )
    val_dataset = TensorDataset(
        torch.FloatTensor(X_val),
        torch.FloatTensor(y_val)
    )
    test_dataset = TensorDataset(
        torch.FloatTensor(X_test),
        torch.FloatTensor(y_test)
    )
    
    train_loader = DataLoader(train_dataset, batch_size=256, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=256, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=256, shuffle=False)
    
    # 超参数搜索（可选）
    # 可以定义多个超参数组合进行搜索
    hidden_dims_options = [
        [128, 64, 32],
        [256, 128, 64],
        [64, 32, 16],
    ]
    
    learning_rates = [0.001, 0.0005, 0.0001]
    dropout_rates = [0.1, 0.2, 0.3]
    
    best_score = float('inf')
    best_params = None
    best_model = None
    
    print("\nStarting hyperparameter search...")
    print(f"Total combinations: {len(hidden_dims_options) * len(learning_rates) * len(dropout_rates)}")
    
    # 简化搜索：只搜索几个关键组合
    for hidden_dims in hidden_dims_options[:2]:  # 只测试前两个
        for lr in learning_rates[:2]:  # 只测试前两个
            for dropout in dropout_rates[:2]:  # 只测试前两个
                print(f"\nTesting: hidden_dims={hidden_dims}, lr={lr}, dropout={dropout}")
                
                model = MLPRegressor(
                    input_dim=X_train.shape[1],
                    hidden_dims=hidden_dims,
                    dropout_rate=dropout
                )
                
                model, train_losses, val_losses = train_model(
                    model, train_loader, val_loader,
                    epochs=args.epochs, lr=lr, device=device,
                    early_stop_patience=args.early_stop_patience
                )
                
                # 在验证集上评估
                y_val_pred = predict(model, X_val, device=device)
                val_mape = mape(y_val, y_val_pred)
                
                print(f"Val MAPE: {val_mape:.4f}")
                
                if val_mape < best_score:
                    best_score = val_mape
                    best_params = {
                        'hidden_dims': hidden_dims,
                        'lr': lr,
                        'dropout': dropout
                    }
                    best_model = model
                    print(f"New best model found! MAPE: {best_score:.4f}")
    
    print(f"\nBest parameters: {best_params}")
    print(f"Best validation MAPE: {best_score:.4f}")
    
    # 使用最佳模型在测试集上评估
    print("\nEvaluating on test set...")
    y_test_pred = predict(best_model, X_test, device=device)
    
    # 计算评估指标（与 train.py 保持一致）
    test_mape = mape(y_test, y_test_pred)
    test_rrse = rrse(y_test, y_test_pred)
    test_r = r(y_test, y_test_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    
    print("\n" + "="*50)
    print("Test Set Evaluation Metrics:")
    print("="*50)
    print(f"Mean Absolute Percentage Error (MAPE): {test_mape:.4f}")
    print(f"Root Relative Square Error (RRSE): {test_rrse:.4f}")
    print(f"Correlation Coefficient (R): {test_r:.4f}")
    print(f"Coefficient of Determination (R²): {test_r2:.4f}")
    print(f"Mean Absolute Error (MAE): {test_mae:.4f}")
    print(f"RMSE (Root Mean Squared Error): {test_rmse:.4f}")
    print("="*50)
    
    # 创建输出文件夹
    output_dir = 'mlp_data'
    os.makedirs(output_dir, exist_ok=True)
    
    # 保存模型和 scaler
    # 注意：此文件包含 sklearn 对象（scaler），加载时需要使用 weights_only=False
    # 例如：checkpoint = torch.load('mlp_model_complete.pth', weights_only=False)
    model_path = os.path.join(output_dir, f'mlp_model_complete_{args.target}.pth')
    torch.save({
        'model_state_dict': best_model.state_dict(),
        'model_params': best_params,
        'scaler': scaler,
        'input_dim': X_train.shape[1]
    }, model_path)
    print(f"\nModel saved to '{model_path}'")
    print("Note: To load this model, use: torch.load('mlp_model_complete.pth', weights_only=False)")
    
    # 导出为 Rust 代码（手动实现，因为 m2cgen 不支持 PyTorch 模型）
    try:
        print("\nExporting MLP model to Rust code...")
        # 获取模型参数
        model_params_list = list(best_model.parameters())
        
        # 获取 scaler 参数
        scaler_mean = scaler.mean_
        scaler_scale = scaler.scale_
        
        # 生成 Rust 代码
        rust_code = generate_mlp_rust_code(best_model, best_params, scaler_mean, scaler_scale, feature_names)
        
        # 写入文件
        rust_path = os.path.join(output_dir, f'mlp_model_{args.target}.rs')
        with open(rust_path, 'w') as f:
            f.write(rust_code)
        print(f"Rust code exported to '{rust_path}'")
        print("Note: This is a basic implementation. You may need to adjust the code for your specific use case.")
    except Exception as e:
        print(f"Warning: Could not export MLP to Rust code: {e}")
        import traceback
        traceback.print_exc()
    
    # 绘制预测 vs 真实值
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_test_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title(f'MLP Predictions vs True Values (R² = {test_r2:.4f})')
    predictions_path = os.path.join(output_dir, f'mlp_predictions_{args.target}.png')
    plt.savefig(predictions_path, dpi=300, bbox_inches='tight')
    print(f"Prediction plot saved to '{predictions_path}'")
    
    # 特征重要性（使用排列重要性）
    print("\nComputing permutation importance...")
    # 为了计算排列重要性，我们需要一个可以接受 numpy 数组的包装函数
    # 创建一个 sklearn 兼容的模型包装器
    from sklearn.base import BaseEstimator, RegressorMixin
    
    class MLPWrapper(BaseEstimator, RegressorMixin):
        def __init__(self, model, device='cpu'):
            self.model = model
            self.device = device
            
        def fit(self, X, y):
            # 模型已经训练好了，这里只是兼容接口
            return self
            
        def predict(self, X):
            return predict(self.model, X, device=self.device)
    
    # 使用训练集计算 permutation importance（与其他模型保持一致）
    # 使用 sklearn 的 permutation_importance，默认使用 R² 作为 scoring
    mlp_wrapper = MLPWrapper(best_model, device=device)
    perm_result = permutation_importance(
        mlp_wrapper, X_train, y_train, 
        n_repeats=10, random_state=42, n_jobs=-1,
        scoring='r2'  # 明确指定使用 R²，与其他模型保持一致
    )
    
    # 排序重要性
    sorted_importances_idx = perm_result.importances_mean.argsort()
    df_columns_sorted = [feature_names[i] for i in sorted_importances_idx]
    
    # 创建 DataFrame 用于绘图（与其他模型格式一致）
    importances = pd.DataFrame(
        perm_result.importances[sorted_importances_idx].T,
        columns=df_columns_sorted,
    )
    
    # 绘制 Permutation Importance（使用 box plot，与其他模型一致）
    fig, ax = plt.subplots(figsize=(10, 6))
    importances.plot.box(vert=False, whis=10, ax=ax)
    ax.set_title("MLP Permutation Importances (train set)")
    ax.axvline(x=0, color="k", linestyle="--")
    ax.set_xlabel("Decrease in accuracy score")
    fig.tight_layout()
    importance_path = os.path.join(output_dir, f'mlp_permutation_importance_{args.target}.png')
    fig.savefig(importance_path, dpi=300, bbox_inches='tight')
    print(f"Permutation importance plot saved to '{importance_path}'")
    
    # 保存 Permutation Importance 为 CSV（与其他模型格式一致）
    perm_importance_df = pd.DataFrame({
        'feature': df_columns_sorted,
        'importance_mean': perm_result.importances_mean[sorted_importances_idx],
        'importance_std': perm_result.importances_std[sorted_importances_idx]
    })
    perm_importance_df = perm_importance_df.sort_values('importance_mean', ascending=False)
    perm_csv_path = os.path.join(output_dir, f'permutation_importance_{args.target}.csv')
    perm_importance_df.to_csv(perm_csv_path, index=False)
    print(f"Permutation importance CSV saved to '{perm_csv_path}'")
    
    print("\nTraining completed!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Train MLP model for circuit area prediction')
    parser.add_argument('--data', type=str, default='../sym_reg/simple_circuit_analysis_project_train_val.csv', 
                        help='Path to CSV data file (default: ../sym_reg/simple_circuit_analysis_project_train_val.csv)')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'],
                        help='Target variable: area or delay (default: area)')
    parser.add_argument('--epochs', type=int, default=200, help='Number of training epochs (default: 200)')
    parser.add_argument('--early_stop_patience', type=int, default=30, help='Early stopping patience (default: 30)')
    parser.add_argument('--cpu', action='store_true', help='Force CPU mode (useful if GPU causes segmentation fault)')
    args = parser.parse_args()
    
    # 将 args 传递给 main 函数
    main(args)

