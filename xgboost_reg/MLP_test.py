import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np
import os

# 评估指标函数
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# MLP 模型定义（简化版，用于快速测试）
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
        
        layers.append(nn.Linear(prev_dim, 1))
        self.model = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.model(x).squeeze()

# 训练函数（简化版）
def train_model_cv(model, train_loader, val_loader, epochs=100, lr=0.001, device='cuda', early_stopping_rounds=10):
    model = model.to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    best_val_loss = float('inf')
    patience_counter = 0
    
    for epoch in range(epochs):
        # 训练
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
        
        # 验证
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for batch_x, batch_y in val_loader:
                batch_x = batch_x.to(device)
                batch_y = batch_y.to(device)
                outputs = model(batch_x)
                loss = criterion(outputs, batch_y)
                val_loss += loss.item()
        
        val_loss /= len(val_loader)
        
        # 早停
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= early_stopping_rounds:
                break
    
    return best_val_loss

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

# 主函数
def main():
    # 设置设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    # 读取数据（与 test.py 类似，使用 data.csv）
    data_path = '../sym_reg/10000.csv'
    
    # 如果 data.csv 不存在，尝试其他路径
    if not os.path.exists(data_path):
        alternative_paths = [
            '../sym_reg/mig_circuit_analysis.csv',
            '../sym_reg/simple_circuit_analysis_large.csv',
            '/data/guangyuh/coding_env/E-Brush/xgboost_reg/collect_dataset/fuzz_circuit_analysis_merge_size_51000_23_10_26.csv'
        ]
        for alt_path in alternative_paths:
            if os.path.exists(alt_path):
                data_path = alt_path
                print(f"Using alternative data path: {data_path}")
                break
        else:
            print(f"Error: Data file not found. Please create 'data.csv' or specify the path.")
            return
    
    data = pd.read_csv(data_path)
    
    # 提取特征和目标（与 test.py 类似，但使用前8列作为特征）
    # test.py 使用 data.drop('delay', axis=1)，这里使用前8列
    if 'delay' in data.columns:
        X = data.drop('delay', axis=1).values
        y = data['delay'].values
    elif 'area' in data.columns:
        # 排除最后3列（power, area, delay），使用前面的列作为特征
        X = data.iloc[:, :-3].values
        y = data['area'].values
    else:
        # 默认排除最后3列作为特征，最后一列作为目标
        X = data.iloc[:, :-3].values
        y = data.iloc[:, -1].values
    
    print(f"Data shape: {X.shape}, Target shape: {y.shape}")
    
    # 数据标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 转换为 PyTorch 张量
    X_tensor = torch.FloatTensor(X_scaled)
    y_tensor = torch.FloatTensor(y)
    
    # 交叉验证参数（与 test.py 类似）
    num_folds = 10
    num_epochs = 100
    early_stopping_rounds = 10
    learning_rate = 0.001
    
    print(f"\nStarting {num_folds}-fold cross-validation...")
    print(f"Epochs: {num_epochs}, Early stopping rounds: {early_stopping_rounds}")
    
    # 交叉验证
    kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)
    cv_mape_scores = []
    
    for fold, (train_idx, val_idx) in enumerate(kf.split(X_scaled)):
        print(f"\nFold {fold + 1}/{num_folds}")
        
        X_train_fold = X_tensor[train_idx]
        y_train_fold = y_tensor[train_idx]
        X_val_fold = X_tensor[val_idx]
        y_val_fold = y_tensor[val_idx]
        
        train_dataset = TensorDataset(X_train_fold, y_train_fold)
        val_dataset = TensorDataset(X_val_fold, y_val_fold)
        
        train_loader = DataLoader(train_dataset, batch_size=256, shuffle=True)
        val_loader = DataLoader(val_dataset, batch_size=256, shuffle=False)
        
        # 创建模型
        model = MLPRegressor(input_dim=X.shape[1])
        
        # 训练
        best_val_loss = train_model_cv(
            model, train_loader, val_loader,
            epochs=num_epochs, lr=learning_rate,
            device=device, early_stopping_rounds=early_stopping_rounds
        )
        
        # 在验证集上评估
        y_val_pred = predict(model, X_val_fold.numpy(), device=device)
        val_mape = mape(y_val_fold.numpy(), y_val_pred)
        cv_mape_scores.append(val_mape)
        
        print(f"Fold {fold + 1} - Val MAPE: {val_mape:.4f}")
    
    # 计算平均 MAPE
    mean_mape = np.mean(cv_mape_scores)
    std_mape = np.std(cv_mape_scores)
    
    print(f"\n{'='*50}")
    print(f"Cross-Validation Results:")
    print(f"{'='*50}")
    print(f"Mean MAPE: {mean_mape:.4f} ± {std_mape:.4f}")
    print(f"Best MAPE: {np.min(cv_mape_scores):.4f}")
    print(f"Worst MAPE: {np.max(cv_mape_scores):.4f}")
    print(f"{'='*50}")
    
    # 使用全部数据训练最终模型
    print("\nTraining final model on full dataset...")
    full_dataset = TensorDataset(X_tensor, y_tensor)
    full_loader = DataLoader(full_dataset, batch_size=256, shuffle=True)
    
    # 创建训练/验证分割用于早停
    train_size = int(0.8 * len(X_scaled))
    val_size = len(X_scaled) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(
        full_dataset, [train_size, val_size]
    )
    train_loader = DataLoader(train_dataset, batch_size=256, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=256, shuffle=False)
    
    final_model = MLPRegressor(input_dim=X.shape[1])
    train_model_cv(
        final_model, train_loader, val_loader,
        epochs=num_epochs, lr=learning_rate,
        device=device, early_stopping_rounds=early_stopping_rounds
    )
    
    # 保存模型
    torch.save({
        'model_state_dict': final_model.state_dict(),
        'scaler': scaler,
        'input_dim': X.shape[1],
        'hidden_dims': [128, 64, 32],
        'dropout_rate': 0.2
    }, 'mlp_best_model.pth')
    print("Model saved to 'mlp_best_model.pth'")
    
    # 加载模型并做预测（与 test.py 类似）
    print("\nLoading model and making predictions...")
    checkpoint = torch.load('mlp_best_model.pth')
    loaded_model = MLPRegressor(
        input_dim=checkpoint['input_dim'],
        hidden_dims=checkpoint.get('hidden_dims', [128, 64, 32]),
        dropout_rate=checkpoint.get('dropout_rate', 0.2)
    )
    loaded_model.load_state_dict(checkpoint['model_state_dict'])
    loaded_model = loaded_model.to(device)
    loaded_model.eval()
    
    # 预测
    preds = predict(loaded_model, X_scaled, device=device)
    
    # 显示结果（与 test.py 类似）
    pd.set_option('display.max_rows', None)
    results_df = pd.DataFrame({
        'true': y,
        'predicted': preds
    })
    print("\nPredictions vs True Values:")
    print(results_df)
    
    # 计算评估指标
    mape_score = mape(y, preds)
    mae_score = mean_absolute_error(y, preds)
    rmse_score = np.sqrt(mean_squared_error(y, preds))
    r2_score_val = r2_score(y, preds)
    
    print(f"\n{'='*50}")
    print("Final Model Evaluation:")
    print(f"{'='*50}")
    print(f"MAPE: {mape_score:.4f}")
    print(f"MAE: {mae_score:.4f}")
    print(f"RMSE: {rmse_score:.4f}")
    print(f"R²: {r2_score_val:.4f}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()

