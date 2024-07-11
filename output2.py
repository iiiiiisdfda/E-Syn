import argparse
import os
import time

parser = argparse.ArgumentParser(description="Output 2 Script")
parser.add_argument("delay", type=int, help="target delay (ps)")
parser.add_argument("directory1", type=str, help="directory1")
args = parser.parse_args()

start_time = time.time()

os.system(f"python exp_yosys_script/test_variation.py {args.delay} > log_var.txt")
os.system("python aanalyze_data1.py")
os.system("python reorder_datasheet1.py")

os.system(f"python exp_yosys_script/test_variation1.py {args.delay} > log_var1.txt")
os.system("python analyze_data2.py")
os.system("python reorder_datasheet2.py")

os.system(f"python exp_yosys_script/test_variation2.py {args.delay} > log_var2.txt")
os.system("python analyze_data3.py")
os.system("python reorder_datasheet3.py")

os.system(f"python exp_yosys_script/test_variation3.py {args.delay} > log_var3.txt")
os.system("python analyze_data4.py")
os.system("python reorder_datasheet4.py")


output_directory = f"./analyze/var3/{args.directory1}/" 
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

command1 = f"cp ./sorted_delay_var.csv {output_directory}/sorted_delay_var.csv"
command2 = f"cp ./sorted_area_var.csv {output_directory}/sorted_area_var.csv"
command3 = f"cp ./sorted_delay_var1.csv {output_directory}/sorted_delay_var1.csv"
command4 = f"cp ./sorted_area_var1.csv {output_directory}/sorted_area_var1.csv"
command5 = f"cp ./log_var.txt {output_directory}/log_var.txt"
command6 = f"cp ./log_var1.txt {output_directory}/log_var1.txt"
command7 = f"cp ./log_var2.txt {output_directory}/log_var2.txt"
command8 = f"cp ./log_var3.txt {output_directory}/log_var3.txt"
command9 = f"cp ./sorted_delay_var2.csv {output_directory}/sorted_delay_var2.csv"
command10 = f"cp ./sorted_area_var2.csv {output_directory}/sorted_area_var2.csv"
command11 = f"cp ./sorted_delay_var3.csv {output_directory}/sorted_delay_var3.csv"
command12 = f"cp ./sorted_area_var3.csv {output_directory}/sorted_area_var3.csv"
os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)
os.system(command5)
os.system(command6)
os.system(command7)
os.system(command8)
os.system(command9)
os.system(command10)
os.system(command11)
os.system(command12)