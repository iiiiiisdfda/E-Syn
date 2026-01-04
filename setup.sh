#!/bin/bash

# Environment Setup Script for E-Syn Project
# This script sets up the development environment by:
# 1. Building ABC tool
# 2. Installing Python dependencies
# 3. Building all Rust projects

set -e  # Exit on error

# Get the project root directory (where this script is located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR"

echo "=========================================="
echo "E-Syn Environment Setup"
echo "=========================================="
echo "Project root: $PROJECT_ROOT"
echo ""

# Step 1: Build ABC
echo "Step 1: Building ABC..."
echo "----------------------------------------"
cd "$PROJECT_ROOT/abc"
if [ -f "Makefile" ]; then
    make clean 2>/dev/null || true
    make
    echo "✓ ABC built successfully"
else
    echo "✗ Error: Makefile not found in abc directory"
    exit 1
fi
echo ""

# Step 2: Install Python dependencies
echo "Step 2: Installing Python dependencies..."
echo "----------------------------------------"

# Check if conda is available
if command -v conda &> /dev/null; then
    echo "Installing packages from packages.txt using conda..."
    if [ -f "$PROJECT_ROOT/packages.txt" ]; then
        # Note: packages.txt contains conda package specifications
        # You may need to adjust this based on your conda environment
        echo "Note: Please install packages from packages.txt manually using conda"
        echo "Example: conda install --file packages.txt"
    else
        echo "⚠ Warning: packages.txt not found"
    fi
else
    echo "⚠ Warning: conda not found, skipping conda packages"
fi

# Install requirements from requirements_str367.txt
if [ -f "$PROJECT_ROOT/requirements_str367.txt" ]; then
    echo "Installing Python packages from requirements_str367.txt..."
    
    # First, upgrade sympy to resolve conflict with torch before installing other packages
    echo "Upgrading sympy to resolve dependency conflict with torch..."
    pip install --upgrade "sympy>=1.13.3" 2>&1 | grep -v "WARNING" || true
    
    # Then install requirements (this may show warnings but should work)
    echo "Installing packages from requirements_str367.txt..."
    pip install -r "$PROJECT_ROOT/requirements_str367.txt" 2>&1 | grep -v "WARNING: pip's dependency resolver" || true
    
    # Ensure sympy is at the correct version after installation
    echo "Verifying sympy version..."
    pip install --upgrade --force-reinstall "sympy>=1.13.3" 2>&1 | grep -v "WARNING" || true
    
    echo "✓ Python dependencies installed"
else
    echo "✗ Error: requirements_str367.txt not found"
    exit 1
fi
echo ""

# Step 3: Build Rust projects
echo "Step 3: Building Rust projects..."
echo "----------------------------------------"

# List of Rust projects to build
RUST_PROJECTS=(
    "s-converter"
    "sym_reg/analyzer"
    "alpha_utils/circuitparser"
    "e-rewriter"
    "alpha_utils/infix2lisp"
    "alpha_utils/lisp2infix"
)

# Check if cargo is available
if ! command -v cargo &> /dev/null; then
    echo "✗ Error: cargo not found. Please install Rust toolchain first."
    echo "Visit: https://www.rust-lang.org/tools/install"
    exit 1
fi

# Build each Rust project
for project in "${RUST_PROJECTS[@]}"; do
    project_path="$PROJECT_ROOT/$project"
    if [ -f "$project_path/Cargo.toml" ]; then
        echo "Building $project..."
        cd "$project_path"
        cargo build --release
        if [ $? -eq 0 ]; then
            echo "✓ $project built successfully"
        else
            echo "✗ Error: Failed to build $project"
            exit 1
        fi
    else
        echo "⚠ Warning: Cargo.toml not found in $project, skipping..."
    fi
done

