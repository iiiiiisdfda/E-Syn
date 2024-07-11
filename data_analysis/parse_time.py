import os
import re

os.chdir('..')
# folder_path = '/data/cchen/E-Brush/log/'
folder_path = os.path.join(os.curdir, 'log')
output_file = 'result.csv'

# 遍历文件夹
file_list = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_list.append(os.path.join(root, file))

# 提取时间数据并保存到文件
with open(output_file, 'w') as f:
    f.write('File Name,Time 1,Time 2\n')

    for file_path in file_list:
        file_name = os.path.basename(file_path)
        time_1 = 'TO'
        time_2 = 'TO'

        with open(file_path, 'r') as file:
            content = file.read()

            # 提取eqn to sexpr时间
            match = re.search(r'eqn to sexpr time: (\d+\.\d+) seconds', content)
            if match:
                time_1 = match.group(1)

            # 提取sexpr to eqn时间
            match = re.search(r'sexpr to eqn: (\d+\.\d+) 秒', content)
            if match:
                time_2 = match.group(1)

            # 检查是否只有一行且内容为"结束"
            if len(content.strip().split('\n')) == 1 and content.strip() == '结束':
                time_1 = 'TO'
                time_2 = 'TO'

            # 检查执行时间是否超过300秒
            if time_1 != 'TO' and float(time_1) > 300:
                time_1 = 'TO'
            if time_2 != 'TO' and float(time_2) > 300:
                time_2 = 'TO'

        f.write(f'{file_name},{time_1},{time_2}\n')

print("数据提取完成并保存到文件中。")

