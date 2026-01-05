#!/usr/bin/env python3
"""
Read MAPE values from CSV file and generate a bar chart.
"""

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

def plot_mape(csv_file, output_file=None):
    """
    Read MAPE values from CSV and create a bar chart.
    
    Args:
        csv_file: Path to the CSV file
        output_file: Output image file path (optional)
    """
    # Read CSV file
    df = pd.read_csv(csv_file, index_col=0)
    
    # Extract MAPE column
    if 'MAPE' not in df.columns:
        raise ValueError(f"MAPE column not found in {csv_file}. Available columns: {df.columns.tolist()}")
    
    mape_data = df['MAPE'].dropna()
    
    if len(mape_data) == 0:
        raise ValueError("No MAPE data found in the CSV file")
    
    # Sort by MAPE value (ascending - lower is better)
    mape_sorted = mape_data.sort_values(ascending=True)
    
    # Define colors (matching the style from model_comparison.py)
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # blue, orange, green, red, purple
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create horizontal bar chart
    bars = plt.barh(mape_sorted.index, mape_sorted.values,
                    color=[colors[i % len(colors)] for i in range(len(mape_sorted))])
    
    # Add value labels on bars
    for i, (model, value) in enumerate(mape_sorted.items()):
        plt.text(value, i, f' {value:.2f}%', va='center', fontsize=10)
    
    # Set labels and title
    plt.xlabel('MAPE (%)', fontsize=12)
    plt.title('Model Comparison: MAPE (Lower is Better)', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    
    # Adjust layout
    plt.tight_layout()
    
    # Determine output filename
    if output_file is None:
        base_name = os.path.splitext(os.path.basename(csv_file))[0]
        output_file = f'{base_name}_mape.png'
    
    # Save figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"MAPE plot saved to '{output_file}'")
    
    # Display summary
    print("\nMAPE Summary:")
    print("=" * 50)
    for model, value in mape_sorted.items():
        print(f"{model:20s}: {value:.2f}%")
    print("=" * 50)
    print(f"\nBest model (lowest MAPE): {mape_sorted.index[0]} ({mape_sorted.iloc[0]:.2f}%)")
    
    return output_file

def main():
    parser = argparse.ArgumentParser(description='Plot MAPE values from CSV file')
    parser.add_argument('csv_file', type=str, help='Path to CSV file containing MAPE data')
    parser.add_argument('-o', '--output', type=str, default=None, 
                       help='Output image file path (default: <csv_basename>_mape.png)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.csv_file):
        print(f"Error: File '{args.csv_file}' not found")
        return 1
    
    try:
        plot_mape(args.csv_file, args.output)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())


