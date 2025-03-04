# Scripts - Data Cleaning & Visualization

## Overview

This folder contains scripts for:

- Cleaning the student performance data.
- Generating visualizations and a summary report.

---

## Files

File                Description
clean_data.py       Cleans the raw data and saves the cleaned version.
analysis.py         Creates plots and generates the results summary.

---

## Prerequisites

- Python 3.x
- Libraries: pandas, seaborn, matplotlib

Install them using:
pip install pandas seaborn matplotlib

---

## Script Execution Order

1. Clean Data:
    python clean_data.py
- Input: data/raw/student_performance.csv
- Output: data/processed/cleaned_student_data.csv

2. Run Analysis:
    python analysis.py
- Input: data/processed/cleaned_student_data.csv
- Output: Plots & analysis/results.md