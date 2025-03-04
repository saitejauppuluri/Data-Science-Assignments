# Scripts - Data Preparation, Cleaning, and Analysis

## Overview

This folder contains all Python scripts used to:

- Convert the provided table into structured raw data.
- Clean and process the data into a usable format.
- Perform analysis, generate visualizations, and produce a summary report.

## File Descriptions

File                  Purpose
convert_to_csv.py     Converts the assignment table into frailty_data.csv and saves it in data/raw/. Run this first if the raw file is missing.
clean_data.py         Reads frailty_data.csv, performs basic cleaning, and saves cleaned_frailty_data.csv into data/processed/.
analysis.py           Loads cleaned_frailty_data.csv, generates visualizations (violin plot, scatter plot with trendline), calculates average grip strength (frail vs non-frail), and saves results in analysis/.

## Prerequisites

- Python 3.x
- Required libraries:
    pandas
    matplotlib
    seaborn

Install using:
pip install pandas matplotlib seaborn

## Script Execution Order

Run the scripts in the following order to fully reproduce the workflow:

1. Convert Table to CSV (if missing)
    python convert_to_csv.py
- Output: data/raw/frailty_data.csv

2. Clean Data
    python clean_data.py
- Input: data/raw/frailty_data.csv
- Output: data/processed/cleaned_frailty_data.csv

3. Run Analysis
    python analysis.py
- Input: data/processed/cleaned_frailty_data.csv
- Outputs:
    - Plots in analysis/plots/
    - Summary report in analysis/results.md

## Script Dependencies Summary

Script              Input                              Output
convert_to_csv.py   None                               data/raw/frailty_data.csv
clean_data.py       data/raw/frailty_data.csv          data/processed/cleaned_frailty_data.csv
analysis.py         data/processed/cleaned_frailty_data.csv    Plots & analysis/results.md

## Notes

- If frailty_data.csv already exists, you can skip convert_to_csv.py.
- All outputs (cleaned data, plots, summary report) are automatically saved in the appropriate folders (data/processed/ and analysis/).