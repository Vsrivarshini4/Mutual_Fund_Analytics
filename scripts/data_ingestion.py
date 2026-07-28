import pandas as pd
import os

folder_path = "data/raw"

files = os.listdir(folder_path)

for file in files:
    if file.endswith(".csv"):
        print("=" * 50)
        print("Dataset:", file)

        df = pd.read_csv(os.path.join(folder_path, file))

        print("Shape:", df.shape)
        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nData Types:")
        print(df.dtypes)

        print("=" * 50)

    import pandas as pd
import os

folder_path = "data/raw"

files = os.listdir(folder_path)

for file in files:
    if file.endswith(".csv"):
        print("=" * 50)
        print("Dataset:", file)

        df = pd.read_csv(os.path.join(folder_path, file))

        print("Missing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("=" * 50)

import os

processed_folder = "data/processed"

if not os.path.exists(processed_folder):
    os.makedirs(processed_folder)

print("Processed folder created successfully")


import pandas as pd

# Load the first dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# Display first 5 rows
print("First 5 Rows:")
print(fund_master.head())

# Display dataset shape
print("\nShape:")
print(fund_master.shape)

# Display column names
print("\nColumns:")
print(fund_master.columns)

# Display data types
print("\nData Types:")
print(fund_master.dtypes)


# Check missing values
print("Missing Values:")
print(fund_master.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(fund_master.duplicated().sum())

# Basic information about the dataset
print("\nDataset Info:")
fund_master.info()

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(fund_master.describe())