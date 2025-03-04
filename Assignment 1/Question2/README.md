# Student Performance Visualization

## Overview

This project analyzes a student performance dataset to explore patterns between study time, absences, and final grades. 

The workflow is fully scripted to make sure all data cleaning, visualization, and reporting steps can be reproduced using the provided Python scripts.

---

## Prerequisites

- Python 3.x
- Required libraries:
    pandas
    matplotlib
    seaborn

Install them using:
pip install pandas matplotlib seaborn

---

## How to Run

1. Navigate to the `src` folder:
    cd src

2. Clean the data:
    python clean_data.py

3. Run the analysis and generate plots:
    python analysis.py

This creates:
- Cleaned data in `data/processed/`
- Plots in `analysis/plots/`
- Summary report in `analysis/results.md`