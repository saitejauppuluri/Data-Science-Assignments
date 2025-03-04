import pandas as pd

#output path for raw data
OUTPUT_PATH = "../data/raw/frailty_data.csv"

#create DataFrame from provided table
data = {
    'Height': [65.8, 71.5, 69.4, 68.2, 67.8, 68.7, 69.8, 70.1, 67.9, 66.8],
    'Weight': [112, 136, 153, 142, 144, 123, 141, 136, 112, 120],
    'Age': [30, 19, 45, 22, 29, 50, 51, 23, 17, 39],
    'Grip_Strength': [30, 31, 29, 28, 24, 26, 22, 20, 19, 31],
    'Frailty': ['N', 'N', 'N', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N']
}

df = pd.DataFrame(data)

#ensure output folder exists
import os
os.makedirs("../data/raw", exist_ok=True)

#save to CSV
df.to_csv(OUTPUT_PATH, index=False)
print(f"Data successfully saved to {OUTPUT_PATH}")