
import pandas as pd
import os

# Path to raw data folder
raw_path = "data/raw"

# Get all CSV files
csv_files = [file for file in os.listdir(raw_path) if file.endswith(".csv")]

print("=" * 80)
print("DATA INGESTION STARTED")
print("=" * 80)

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"FILE: {file}")
    print("=" * 80)

    file_path = os.path.join(raw_path, file)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

print("\nData ingestion completed successfully.")