import pandas as pd
import os

#paths
RAW_PATH = "../data/raw/StudentsPerformance.csv"
CLEANED_PATH = "../data/processed/cleaned_student_data.csv"

#ensure processed folder exists
os.makedirs("../data/processed", exist_ok=True)

def clean_data():
    #load data
    df = pd.read_csv(RAW_PATH)

    #normalize column names (strip spaces & lowercase all columns)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    #drop rows with any missing data
    df.dropna(inplace=True)

    #ensure score columns are numeric (in case of weird entries)
    score_columns = ['math_score', 'reading_score', 'writing_score']
    for col in score_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    #drop rows where scores failed numeric conversion (just in case)
    df.dropna(subset=score_columns, inplace=True)

    #standardize categorical columns to lowercase for consistency
    text_columns = ['gender', 'race/ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
    for col in text_columns:
        df[col] = df[col].str.strip().str.lower()

    #save cleaned data
    df.to_csv(CLEANED_PATH, index=False)
    print(f"Cleaned data saved at {CLEANED_PATH}")

if __name__ == "__main__":
    clean_data()