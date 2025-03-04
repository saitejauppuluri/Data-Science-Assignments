# Frailty Data Analysis Workflow

## Overview

This project analyzes the relationship between grip strength and frailty among participants. It follows a structured reproducible workflow, ensuring all steps — from raw data preparation to analysis — are clear, separated, and repeatable.

The project is organized into three main stages:
1. Data Collection - Raw data and metadata.
2. Data Processing - Data cleaning and preparation.
3. Data Analysis - Visualization and statistical analysis.

## Folder Structure

Question1/
├── data/
│   ├── raw/                  # Raw data and metadata
│   ├── processed/            # Cleaned data
├── src/                      # All scripts for data preparation, cleaning, and analysis
├── analysis/                 # Final plots and summary report
└── README.md                 # Project-level documentation (this file)

## How to Run the Full Workflow

### Prerequisites

- Python 3.x
- Required libraries:
    pandas
    matplotlib
    seaborn

Install using:
pip install pandas matplotlib seaborn

### Steps to Reproduce

1. Navigate to the src folder:
    cd src

2. Generate Raw Data (if not already present):
    python convert_to_csv.py
This script creates frailty_data.csv from the provided table.

3. Clean the Data:
    python clean_data.py
This creates cleaned_frailty_data.csv in data/processed.

4. Run Analysis:
    python analysis.py
This creates:
- Scatter plots in analysis/plots/
- A summary report in analysis/results.md

## Outputs

File/Folder                                  Description
data/raw/frailty_data.csv                    Original raw data in CSV format
data/processed/cleaned_frailty_data.csv      Cleaned data after processing
analysis/plots/                              Folder containing generated plots
analysis/results.md                          Summary report with key findings

## Key Concept: Reproducibility

This project is designed to follow a reproducible workflow, meaning anyone can clone the project and re-run all steps to obtain the same results. Data, processing, and analysis are kept separate, and all transformations are handled through scripts to ensure transparency and consistency.