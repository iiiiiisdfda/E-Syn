import argparse
import subprocess
import threading
import sys
import os

def run_command(i, delay, base_dir):
    command = f"abc -c \"read_eqn {base_dir}/test_data_beta_runner/raw_circuit.eqn; read_lib {base_dir}/asap7_clean.lib; st; ifraig; scorr; dc2; dretime; retime -o -D {delay}; st; &get -n; &dch -f; &nf -D {delay}; &put; buffer; upsize -D {delay}; dnsize -D {delay}; stime -p\""

    subprocess.run(command, shell=True, cwd=base_dir)

    print(f"Thread {i} completed with delay {delay} ps")  

def main():
    parser = argparse.ArgumentParser(description="Test Variation Script")
    parser.add_argument("delay", type=int, help="目标延迟值 以ps为单位")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    

    base_dir = os.path.abspath(os.path.join(script_dir, '..'))
    os.chdir(base_dir)

    with open('log_var1.txt', 'w') as f:
        sys.stdout = f  

        threads = []
        increment = (args.delay // (15*3))

        for i in range(30):
            curr_delay = args.delay + (i - 14) * increment
            thread = threading.Thread(target=run_command, args=(i, curr_delay, base_dir))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    sys.stdout.close()
    sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()