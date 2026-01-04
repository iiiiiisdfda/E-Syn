#!/bin/bash
# Compile LaTeX document to PDF using pdftex

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "Error: pdflatex is not installed"
    echo "Please install a LaTeX distribution (e.g., TeX Live)"
    exit 1
fi

# Check if report.tex exists
if [ ! -f "report.tex" ]; then
    echo "Error: report.tex not found"
    exit 1
fi

# Check if PDF exists and if .tex is newer than PDF
NEED_COMPILE=true
if [ -f "report.pdf" ]; then
    if [ "report.tex" -nt "report.pdf" ]; then
        echo "report.tex is newer than report.pdf, compiling..."
        NEED_COMPILE=true
    else
        # Check if force flag is provided
        if [ "$1" = "--force" ] || [ "$1" = "-f" ]; then
            echo "Force recompiling..."
            NEED_COMPILE=true
        else
            echo "report.pdf is up to date. Use --force to recompile anyway."
            exit 0
        fi
    fi
else
    echo "report.pdf not found, compiling..."
    NEED_COMPILE=true
fi

# Compile the document (run twice for proper references)
if [ "$NEED_COMPILE" = true ]; then
    echo "Compiling report.tex..."
    pdflatex -interaction=nonstopmode report.tex > /dev/null 2>&1
    pdflatex -interaction=nonstopmode report.tex
    
    # Check if compilation was successful
    if [ -f "report.pdf" ]; then
        echo "✓ Successfully compiled report.pdf"
        echo "Cleaning up auxiliary files..."
        rm -f report.aux report.out report.bbl report.blg
        # Keep report.log for debugging
    else
        echo "✗ Compilation failed. Check report.log for errors."
        exit 1
    fi
fi

