import os
import pandas as pd
import matplotlib.pyplot as plt


script_dir = os.path.dirname(os.path.abspath(__file__))

# 回到上级目录的路径
parent_dir = os.path.join(script_dir, '..')

# 构建 data_folder 的完整路径
data_folder = os.path.join(parent_dir, 'analyze/sample/')

# 遍历每个文件夹
for folder_name in os.listdir(data_folder):
    folder_path = os.path.join(data_folder, folder_name)
    
    # 仅处理文件夹名字以数字开头的文件夹
    if folder_name.split('_')[0].isdigit():
        x = int(folder_name.split('_')[0])
        x = 6*x +2
        # 构建area_delay_product_total.csv文件路径
        csv_file = os.path.join(folder_path, 'area_delay_product_total.csv')
        
        # 使用pandas读取CSV文件
        df = pd.read_csv(csv_file, sep=',')
        print(df.columns)
        # 获取第一个数据点的score值
        score = df.loc[0, 'Score']
        
        # 绘制图表
        plt.scatter(x, score, color='b')

# 设置图表标题和轴标签
plt.title('Score vs. X')
plt.xlabel('X')
plt.ylabel('Score')

# 显示图表
plt.show()