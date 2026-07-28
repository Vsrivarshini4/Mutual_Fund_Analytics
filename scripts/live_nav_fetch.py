import requests
import pandas as pd

# Scheme names and AMFI codes
schemes = {
    "HDFC_Top_100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

# Download NAV data for each scheme
for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    print(f"Downloading {scheme_name}...")

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(f"../data/raw/{scheme_name}.csv", index=False)

print("All NAV files downloaded successfully!")