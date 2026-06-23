import requests
import pandas as pd

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, amfi_code in funds.items():

    print("=" * 60)
    print(f"Fetching {fund_name}")
    print("=" * 60)

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_name = f"data/raw/{fund_name}_NAV.csv"

    nav_df.to_csv(file_name, index=False)

    print(f"Saved: {file_name}")

print("\nAll NAV files downloaded successfully.")