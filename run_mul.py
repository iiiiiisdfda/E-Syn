import os
import sys
import subprocess
import time
from datetime import datetime
count = 0

test_list = [
    "/home/str367/lsv_final/E-Syn/benchmark/AIO/simple_circuit_0.eqn",
    "/home/str367/lsv_final/E-Syn/benchmark/AIO/simple_circuit_1.eqn",
    "/home/str367/lsv_final/E-Syn/benchmark/AIO/simple_circuit_2.eqn",
    "/home/str367/lsv_final/E-Syn/benchmark/AIO/simple_circuit_3.eqn",  
    "/home/str367/lsv_final/E-Syn/benchmark/AIO/simple_circuit_4.eqn",
    "/home/str367/lsv_final/E-Syn/benchmark/AIO/simple_circuit_5.eqn",
    "/home/str367/lsv_final/E-Syn/benchmark/AIO/simple_circuit_6.eqn",
    "/home/str367/lsv_final/E-Syn/benchmark/AIO/simple_circuit_7.eqn",
    "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/EPFL/adder.eqn",
    #          "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/EPFL/bar.eqn",
    #          "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/EPFL/max.eqn",
             "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/EPFL/calv.eqn",
            #  "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/OpenCores/qdiv.eqn",
            #  "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/LGSynth91/C5315.eqn",
             "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/LGSynth91/i7.eqn",
            #  "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/ISCAS85/c7552.eqn",
             "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/ISCAS85/c2670.eqn",
             "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/LGSynth89/frg2.eqn",
             "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/LGSynth89/C432.eqn",
             "/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/ITC99/b12.eqn"
    ]

def get_timestamp():
    """返回格式化的時間戳記"""
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

for files in test_list:
    # for files in os.listdir(f"/home/str367/lsv_final/E-Syn/benchmark/converted_circuit/{folder}"):
    #     if files.endswith(".eqn"):
    #         print(f"Processing {count} circuit {files}", flush=True)
    #         sys.stdout.flush()  # 确保输出立即刷新
    #     else:
    #         continue
        start_time = time.time()
        # clean all files in testdata folder
        print(f"{get_timestamp()} Processing {count} circuit {files}", flush=True)
        for file in os.listdir("test_data"):
            os.remove(f"test_data/{file}")
        os.system(f"cp {files} test_data/raw_circuit.eqn")
        
        # 使用 subprocess 代替 os.system，直接输出到 stdout/stderr，避免缓冲问题
        # -u 参数启用 Python 无缓冲模式，确保输出实时显示
        print(f"{get_timestamp()} Starting run.py for {files}", flush=True)
        result = subprocess.run(
            ["python", "-u", "run.py"],
            stdout=None,  # 直接输出到父进程的 stdout
            stderr=None,  # 直接输出到父进程的 stderr
        )
        
        if result.returncode != 0:
            print(f"{get_timestamp()} Warning: run.py exited with code {result.returncode}", flush=True)
        
        count += 1

        os.system(f"cp -r test_data test_data_{files.split('/')[-1].split('.')[0]}")
        elapsed_time = time.time() - start_time
        print(f"{get_timestamp()} Completed {files} - Time elapsed: {elapsed_time:.2f} seconds", flush=True)