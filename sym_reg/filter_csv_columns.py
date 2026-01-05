#!/usr/bin/env python3
"""
Filter CSV file to keep only specified columns.
Usage: python filter_csv_columns.py <input_csv> [output_csv]
If output_csv is not specified, the input file will be overwritten.
"""

import sys
import pandas as pd

# Columns to keep
COLUMNS_TO_KEEP = [
    '+',
    '!',
    '*',
    '&',
    'ASTSize',
    'ASTDepth',
    'SUM_LIB',
    'SUM_NODE',
    'AVE_LIB',
    'lev',
    'power',
    'area',
    'delay'
]

def filter_csv(input_file, output_file=None):
    """Read CSV and keep only specified columns."""
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Check which columns exist in the dataframe
        existing_columns = [col for col in COLUMNS_TO_KEEP if col in df.columns]
        missing_columns = [col for col in COLUMNS_TO_KEEP if col not in df.columns]
        
        if missing_columns:
            print(f"Warning: The following columns are not found in the CSV: {missing_columns}")
        
        if not existing_columns:
            print("Error: None of the specified columns were found in the CSV file.")
            return False
        
        # Keep only the specified columns
        df_filtered = df[existing_columns]
        
        # Determine output file
        if output_file is None:
            output_file = input_file
        
        # Save the filtered dataframe
        df_filtered.to_csv(output_file, index=False)
        
        print(f"Successfully filtered CSV file.")
        print(f"Input: {input_file}")
        print(f"Output: {output_file}")
        print(f"Original columns: {len(df.columns)}")
        print(f"Kept columns: {len(existing_columns)}")
        print(f"Rows: {len(df_filtered)}")
        
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python filter_csv_columns.py <input_csv> [output_csv]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = filter_csv(input_file, output_file)
    sys.exit(0 if success else 1)

