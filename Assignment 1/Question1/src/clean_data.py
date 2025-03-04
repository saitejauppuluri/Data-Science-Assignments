import pandas as pd
import os

#paths
RAW_DATA_PATH = "../data/raw/frailty_data.csv"
CLEANED_DATA_PATH = "../data/processed/cleaned_frailty_data.csv"

#make sure processed folder exists
os.makedirs("../data/processed", exist_ok=True)

def clean_data():
    #read raw data
    df = pd.read_csv(RAW_DATA_PATH)

    #clean column names (just to be safe)
    df.columns = ['Height', 'Weight', 'Age', 'Grip_Strength', 'Frailty']

    #no complex cleaning needed in this case, but this is where we could:
    #-handle missing values (drop rows, fill with averages, etc.)
    #-check data types (make sure numbers are numbers)

    #save cleaned data
    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Cleaned data saved at {CLEANED_DATA_PATH}")

if __name__ == "__main__":
    clean_data()