
import os 
import subprocess
print("\n\n------------------------------------Original circuit------------------------------------")
#command = "./abc/abc -c \"read_eqn test_data_beta_runner/original_circuit.eqn; balance; refactor; print_stats -p; read_lib asap7_clean.lib ; map ; stime; strash ; andpos; write_aiger test_data_beta_runner/original_circuit.aig\""
#command = "./abc/abc -c \"read_eqn test_data_beta_runner/original_circuit.eqn; balance; refactor; print_stats; read_lib asap7_clean.lib ; map ; stime; strash ; write_aiger test_data_beta_runner/original_circuit.aig\""
#command = "./abc/abc -c \"read_eqn test_data_beta_runner/original_circuit.eqn;balance; refactor; balance; rewrite; rewrite -z; balance; rewrite -z; balance; print_stats -p; read_lib asap7_clean.lib ; map ; stime; collapse; write_blif test_data_beta_runner/original_circuit.blif\""



# command = "./abc/abc -c \"read_eqn test_data_beta_runner/raw_circuit.eqn; st;print_stats -p;write_dot rewriting_test/b02/original.dot\""
# os.system(command)


# command = "./abc/abc -c \"read_eqn test_data_beta_runner/raw_circuit.eqn; st;rw;print_stats -p;write_dot rewriting_test/b02/rw.dot\""
# os.system(command)

# command = "./abc/abc -c \"read_eqn test_data_beta_runner/raw_circuit.eqn; st;rs;print_stats -p;write_dot rewriting_test/b02/rs.dot\""
# os.system(command)

# command = "./abc/abc -c \"read_eqn test_data_beta_runner/raw_circuit.eqn; st;rf;print_stats -p;write_dot rewriting_test/b02/rf.dot\""
# os.system(command)
# print("----------------------------------------------------------------------------------------")


os.chdir('..')

command = "./abc/abc -c \"read_eqn test_data_beta_runner/raw_circuit.eqn; st;print_stats -p;read_lib asap7_clean.lib ; map ; topo; upsize; dnsize; stime;write_dot rewriting_test/b02/original.dot;write_verilog rewriting_test/b02/orignal.v\""
os.system(command)


command = "./abc/abc -c \"read_eqn test_data_beta_runner/raw_circuit.eqn; st;rw;print_stats -p;read_lib asap7_clean.lib ; map ; topo; upsize; dnsize; stime;write_dot rewriting_test/b02/rw.dot;write_verilog rewriting_test/b02/rw.v\""
os.system(command)

command = "./abc/abc -c \"read_eqn test_data_beta_runner/raw_circuit.eqn; st;rs;print_stats -p;read_lib asap7_clean.lib ; map ; topo; upsize; dnsize; stime;write_dot rewriting_test/b02/rs.dot;write_verilog rewriting_test/b02/rs.v\""
os.system(command)

command = "./abc/abc -c \"read_eqn test_data_beta_runner/raw_circuit.eqn; st;rf;print_stats -p;read_lib asap7_clean.lib ; map ; topo; upsize; dnsize; stime;write_dot rewriting_test/b02/rf.dot;write_verilog rewriting_test/b02/rf.v\""
os.system(command)
print("----------------------------------------------------------------------------------------")



# for optized circuit
print("\n\n------------------------------------Optimized circuit------------------------------------")
#command = "./abc/abc -c \"read_eqn test_data_beta_runner/optimized_circuit.eqn; balance; refactor; print_stats -p; read_lib asap7_clean.lib ; map ; stime;  strash ; andpos; write_aiger test_data_beta_runner/optimized_circuit.aig\""
#command = "./abc/abc -c \"read_eqn test_data_beta_runner/optimized_circuit.eqn; balance; refactor; print_stats; read_lib asap7_clean.lib ; map ; stime; strash ; write_aiger test_data_beta_runner/optimized_circuit.aig\""
#command = "./abc/abc -c \"read_eqn test_data_beta_runner/optimized_circuit.eqn; balance; refactor; print_stats -p; read_lib asap7_clean.lib ; map ; stime; collapse; write_blif test_data_beta_runner/optimized_circuit.blif\""
#command = "./abc/abc -c \"read_eqn test_data_beta_runner/optimized_circuit.eqn; st; dch -f; print_stats -p; read_lib asap7_clean.lib ; map ; topo; upsize; dnsize; stime\""
#os.system(command)
#print("----------------------------------------------------------------------------------------")
#write_dot rewriting_test/egg.dot
def run_command(i):
    command = f"./abc/abc -c \"read_eqn test_data_beta_runner/optimized_circuit{i}.eqn; st; print_stats -p;read_lib asap7_clean.lib ; map ; topo; upsize; dnsize; stime;write_dot rewriting_test/b02/egg{i}.dot;write_verilog rewriting_test/b02/egg{i}.v\""
    subprocess.run(command, shell=True)
    print("----------------------------------------------------------------------------------------")
# threads = []
# for i in range(30):
#     thread = threading.Thread(target=run_command, args=(i,))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()    
for i in range(1,2):
    run_command(i)
for i in range(2,3):
    run_command(i)
# for i in range(30):
#     run_command(i)