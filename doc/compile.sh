#!/bin/bash
# Compile LaTeX document to PDF using pdftex

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "Error: pdflatex is not installed"
    echo "Please install a LaTeX distribution (e.g., TeX Live)"
    exit 1
fi

# Compile the document (run twice for proper references)
echo "Compiling report.tex..."
pdflatex -interaction=nonstopmode report.tex
pdflatex -interaction=nonstopmode report.tex

# Check if compilation was successful
if [ -f "report.pdf" ]; then
    echo "✓ Successfully compiled report.pdf"
    echo "Cleaning up auxiliary files..."
    rm -f report.aux report.log report.out report.bbl report.blg
else
    echo "✗ Compilation failed. Check report.log for errors."
    exit 1
fi

