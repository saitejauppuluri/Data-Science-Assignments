# Used Car Price Analysis

This project processes and analyzes a dataset of used car listings. The dataset is cleaned, transformed, and explored using pandas in Python. The goal is to fulfill five tasks (a–e), each explained and demonstrated in a notebook.

---

## Folder Structure

- data/ → Contains the original CSV (`train.csv`)
- notebooks/ → Contains the notebook where all tasks are solved step-by-step
- output/ → Final results like grouped summary CSV
- requirements.txt → Python libraries used

---

## Task Breakdown

### (a) Handle Missing Values  
- Dropped New_Price column due to 86%+ missing values.  
- Imputed Mileage, Engine, Power, and Seats using mode, since these features often use standard values (e.g., 1199 CC, 5 seats).

### (b) Remove Units  
- Stripped units like "kmpl", "CC", and "bhp" from the columns and converted them to numeric format.

### (c) One-Hot Encode  
- Applied one-hot encoding to Fuel_Type and Transmission.

### (d) Add a New Feature  
- Added a new feature Car_Age = 2025 - Year.

### (e) Perform DataFrame Operations  
- Selected and filtered relevant data.
- Renamed Kilometers_Driven to KMs_Driven.  
- Sorted by price.  
- Grouped by Location to find average price and total count.  
- Saved results to output/summary_by_location.csv.

---

## How to Run

1. Make sure train.csv is placed inside the data/ folder.
2. Open and run notebooks/used_car_analysis.ipynb.
3. The final output will be saved in output/summary_by_location.csv.