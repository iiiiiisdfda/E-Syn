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
            data = '../sym_reg/feature1/10000.csv'
            target = 'area'
            epochs = 200
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
    
    # 数据标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    
    # 进一步分割训练集和验证集
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=0.2, random_state=42
    )
    
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
    
    # 保存模型和 scaler
    # 注意：此文件包含 sklearn 对象（scaler），加载时需要使用 weights_only=False
    # 例如：checkpoint = torch.load('mlp_model_complete.pth', weights_only=False)
    torch.save({
        'model_state_dict': best_model.state_dict(),
        'model_params': best_params,
        'scaler': scaler,
        'input_dim': X_train.shape[1]
    }, 'mlp_model_complete.pth')
    print("\nModel saved to 'mlp_model_complete.pth'")
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
        with open('mlp_model.rs', 'w') as f:
            f.write(rust_code)
        print("Rust code exported to 'mlp_model.rs'")
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
    plt.savefig('mlp_predictions.png', dpi=300, bbox_inches='tight')
    print("Prediction plot saved to 'mlp_predictions.png'")
    
    # 特征重要性（使用排列重要性）
    print("\nComputing permutation importance...")
    # 为了计算排列重要性，我们需要一个可以接受 numpy 数组的包装函数
    def model_predict_wrapper(X):
        return predict(best_model, X, device=device)
    
    # 注意：permutation_importance 需要 sklearn 模型，这里我们手动实现简化版本
    # 或者可以使用更小的样本集来加速
    sample_size = min(1000, len(X_test))
    sample_indices = np.random.choice(len(X_test), sample_size, replace=False)
    X_sample = X_test[sample_indices]
    y_sample = y_test[sample_indices]
    
    baseline_pred = predict(best_model, X_sample, device=device)
    baseline_score = mean_squared_error(y_sample, baseline_pred)
    
    feature_importances = []
    for i in range(X_sample.shape[1]):
        X_permuted = X_sample.copy()
        np.random.shuffle(X_permuted[:, i])
        permuted_pred = predict(best_model, X_permuted, device=device)
        permuted_score = mean_squared_error(y_sample, permuted_pred)
        importance = permuted_score - baseline_score
        feature_importances.append(importance)
    
    # 绘制特征重要性
    # 使用与特征提取相同的逻辑：使用之前定义的 feature_names
    # 确保特征名称和重要性数量匹配
    if len(feature_names) != len(feature_importances):
        print(f"Warning: Feature names count ({len(feature_names)}) != importance count ({len(feature_importances)})")
        # 如果数量不匹配，使用索引作为特征名
        feature_names = [f'Feature_{i}' for i in range(len(feature_importances))]
    importances_df = pd.DataFrame({
        'feature': feature_names,
        'importance': feature_importances
    }).sort_values('importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    plt.barh(importances_df['feature'], importances_df['importance'])
    plt.xlabel('Permutation Importance (MSE increase)')
    plt.title('MLP Feature Importance (Permutation)')
    plt.tight_layout()
    plt.savefig('mlp_feature_importance.png', dpi=300, bbox_inches='tight')
    print("Feature importance plot saved to 'mlp_feature_importance.png'")
    
    print("\nTraining completed!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Train MLP model for circuit area prediction')
    parser.add_argument('--data', type=str, default='../sym_reg/feature1/10000.csv', 
                        help='Path to CSV data file (default: ../sym_reg/feature1/10000.csv)')
    parser.add_argument('--target', type=str, default='area', choices=['area', 'delay'],
                        help='Target variable: area or delay (default: area)')
    parser.add_argument('--epochs', type=int, default=200, help='Number of training epochs (default: 200)')
    parser.add_argument('--early_stop_patience', type=int, default=30, help='Early stopping patience (default: 30)')
    parser.add_argument('--cpu', action='store_true', help='Force CPU mode (useful if GPU causes segmentation fault)')
    args = parser.parse_args()
    
    # 将 args 传递给 main 函数
    main(args)

