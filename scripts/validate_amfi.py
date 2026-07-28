import pandas as pd

# Load datasets
fund_master = pd.read_csv("../data/raw/01_fund_master.csv")
nav_history = pd.read_csv("../data/raw/02_nav_history.csv")

# Check whether all AMFI codes in fund_master exist in nav_history
missing_codes = fund_master[
    ~fund_master["amfi_code"].isin(nav_history["amfi_code"])
]

print("Missing AMFI Codes:")
print(missing_codes)

print("\nTotal Missing Codes:", len(missing_codes))