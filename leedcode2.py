import pandas as pd
import numpy as np 

try:
    df = pd.read_csv('bmw.csv')
    print(" Dataset Loaded Successfully.\n")
except FileNotFoundError:
    print(" Error: Please check the file path. Using a sample DataFrame for demonstration.")
    # Create a simple example DataFrame if the file isn't found
    data = {'model': ['320i', '530e', '320i', 'X5', 'M4'],
            'year': [2018, 2020, 2018, 2021, 2022],
            'price': [15000, 35000, 15000, np.nan, 70000],
            'mileage': [55000, 20000, 55000, 10000, '3,000'],
            'fuel_type': ['Petrol', 'Hybrid', 'Petrol', None, 'Petrol']}
    df = pd.DataFrame(data)

print("--- not a proper INfor  geting in the csv file  ---")
df.info()
print("\n")

initial_rows = len(df)
df.drop_duplicates(inplace=True)
duplicates_removed = initial_rows - len(df)
print(f" Removed {duplicates_removed} Duplicate Rows.")

print("\n--- Missing Value Check ---")
print(df.isnull().sum()) 

median_price = df['price'].median()
df['price'].fillna(median_price, inplace=True)
print(f" Filled missing 'price' values with median: {median_price}")

df.dropna(subset=['fuel_type'], inplace=True)
print(" Dropped rows with missing 'fuel_type'.")

if df['mileage'].dtype == 'object':
    df['mileage'] = (
        df['mileage']
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.strip()
        .replace('', np.nan) 
        .astype(float)
        .astype('Int64') 
    )
    print("⚙️ Cleaned and Converted 'mileage' to Integer.")
else:
    print("⚙️ 'mileage' column is already numeric.")

print("\n--- Final Cleaned Info ---")
df.info()
print("\n--- First 5 Cleaned Rows ---")
print(df.head())
