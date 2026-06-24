
import pandas as pd
import os

print("=" * 80)
print("DAY 2 - DATA CLEANING")
print("=" * 80)

raw_path = "data/raw"
processed_path = "data/processed"

# Create processed folder if not exists
os.makedirs(processed_path, exist_ok=True)

print("Folders verified successfully.")

# Load NAV History dataset
nav_df = pd.read_csv("data/raw/02_nav_history.csv")

print("\nData Types:")
print(nav_df.dtypes)

print("\nMissing Values:")
print(nav_df.isnull().sum())

print("\nDuplicate Rows:")
print(nav_df.duplicated().sum())

print("\nInvalid NAV Values:")
print((nav_df["nav"] <= 0).sum())

print("\nCleaning nav_history dataset...")

# Convert date column to datetime
nav_df["date"] = pd.to_datetime(nav_df["date"])

# Sort records
nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)

# Forward fill NAV values within each fund
nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()

# Save cleaned dataset
nav_df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("\nNAV History cleaned successfully.")
print("Saved: data/processed/02_nav_history_cleaned.csv")



print("\n" + "=" * 80)
print("Cleaning investor_transactions.csv")
print("=" * 80)

txn_df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("\nData Types:")
print(txn_df.dtypes)

print("\nMissing Values:")
print(txn_df.isnull().sum())

print("\nDuplicate Rows:")
print(txn_df.duplicated().sum())

print("\nTransaction Types:")
print(txn_df["transaction_type"].unique())

print("\nKYC Status Values:")
print(txn_df["kyc_status"].unique())

print("\nInvalid Amounts:")
print((txn_df["amount_inr"] <= 0).sum())

print("\nCleaning investor_transactions dataset...")

# Convert transaction_date to datetime
txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

# Standardize transaction types
txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .str.strip()
    .str.title()
)

# Standardize KYC status
txn_df["kyc_status"] = (
    txn_df["kyc_status"]
    .str.strip()
    .str.title()
)

# Keep only valid amounts
txn_df = txn_df[txn_df["amount_inr"] > 0]

# Save cleaned dataset
txn_df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("\nInvestor Transactions cleaned successfully.")
print("Saved: data/processed/08_investor_transactions_cleaned.csv")

print("\n" + "=" * 80)
print("Cleaning scheme_performance.csv")
print("=" * 80)

perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nData Types:")
print(perf_df.dtypes)

print("\nMissing Values:")
print(perf_df.isnull().sum())

print("\nDuplicate Rows:")
print(perf_df.duplicated().sum())

# Check expense ratio range
invalid_expense = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1) |
    (perf_df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:")
print(len(invalid_expense))

# Validate return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    print(f"\nChecking {col}")
    print(pd.to_numeric(perf_df[col], errors="coerce").isnull().sum())


print("\nCleaning scheme_performance dataset...")

# Remove duplicates (safety check)
perf_df = perf_df.drop_duplicates()

# Save cleaned dataset
perf_df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nScheme Performance cleaned successfully.")
print("Saved: data/processed/07_scheme_performance_cleaned.csv")