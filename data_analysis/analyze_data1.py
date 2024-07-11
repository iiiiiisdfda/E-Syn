import csv
import re
import os
headers = ['WireLoad', 'Gates', 'Cap', 'Area', 'Delay']

table = []
parent_dir = os.path.dirname(os.path.abspath(__file__))
grandparent_dir = os.path.join(parent_dir, os.pardir)  
log_file_path = os.path.join(grandparent_dir, 'log_var.txt')
output_csv_path = os.path.join(grandparent_dir, 'res_data_var.csv')
i = 0
with open(log_file_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if 'WireLoad' in line:
            row = []
            i += 1
            if i == 1:
                row.append("origin")
            else:
                row.append("op" + str(i - 1))
            gates_match = re.search(r'Gates\s*=\s*(\d+)', line)
            if gates_match:
                gates = gates_match.group(1)
                row.append(gates)
            cap_match = re.search(r'Cap\s*=\s*([\d.]+)\s+ff', line)
            if cap_match:
                cap = cap_match.group(1)
                row.append(cap)
            area_match = re.search(r'Area\s*=\s*(\d+)', line)
            if area_match:
                area = area_match.group(1)
                row.append(area)
            delay_match = re.search(r'Delay\s*=\s*([\d.]+)\s+ps', line)
            if delay_match:
                delay = delay_match.group(1)
                row.append(delay)
            if len(row) == len(headers):
                table.append(row)
with open(output_csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)  
    writer.writerows(table)  