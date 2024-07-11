import os
import csv
import re
directory1 = input("input the directory name:")
directory = input("file name:")
output_directory = f"./analyze/{directory1}/" + directory
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


command1 = f"cp ./sorted_delay.csv ./analyze/{directory1}/{directory}/sorted_delay.csv"
command2 = f"cp ./sorted_area.csv ./analyze/{directory1}/{directory}/sorted_area.csv"
command3 = f"cp ./new_data.csv ./analyze/{directory1}/{directory}/new_data.csv"
command4 = f"cp ./res_data_rc64b.csv ./analyze/{directory1}/{directory}/res_data_rc64b.csv"
command5 = f"cp ./pareto_optimal_points.csv ./analyze/{directory1}/{directory}/pareto_optimal_points.csv"
command6 = f"cp ./area_delay_product_total.csv ./analyze/{directory1}/{directory}/area_delay_product_total.csv"
os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)
os.system(command5)
os.system(command6)