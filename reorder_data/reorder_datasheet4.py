import csv
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.join(script_dir, '..')

input_csv_path = os.path.join(parent_dir, 'res_var3.csv')
output_csv_delay_path = os.path.join(parent_dir, 'sorted_delay_var3.csv')
output_csv_area_path = os.path.join(parent_dir, 'sorted_area_var3.csv')

data = []
with open(input_csv_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    for row in reader:
        data.append([row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4])])

data_sorted = sorted(data, key=lambda x: x[4])

data_sorted1 = sorted(data, key=lambda x: x[3])


with open(output_csv_delay_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['WireLoad', 'Gates', 'Cap', 'Area', 'Delay'])  
    writer.writerows(data_sorted)  

with open(output_csv_area_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['WireLoad', 'Gates', 'Cap', 'Area', 'Delay'])  
    writer.writerows(data_sorted1)  

res_data = pd.read_csv(input_csv_path)
