#!/bin/bash
cd ..
current_dir=$(pwd)

input_dir="converted_circuit_strash/EPFL/"  
output_dir="test_data_beta_runner/" 
log_dir="log_mem/"  

mkdir -p "$log_dir"  

current_dir=$(pwd)  

for file in "$current_dir/$input_dir"/*.eqn; do
    filename=$(basename "$file" .eqn)  
    log_file="$log_dir/$filename.txt"  
    cp "$file" "$output_dir/raw_circuit.eqn"
    cd "$current_dir"
    python run_beta.py > "$log_file" 2>&1
    echo "Completed: $filename"  
    cd "$current_dir"
done