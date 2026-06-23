
import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("UNIQUE FUND HOUSES")
print("=" * 60)
print(df["fund_house"].unique())

print("\n" + "=" * 60)
print("CATEGORIES")
print("=" * 60)
print(df["category"].unique())

print("\n" + "=" * 60)
print("SUB CATEGORIES")
print("=" * 60)
print(df["sub_category"].unique())

print("\n" + "=" * 60)
print("RISK CATEGORIES")
print("=" * 60)
print(df["risk_category"].unique())

print("\n" + "=" * 60)
print("TOTAL UNIQUE AMFI CODES")
print("=" * 60)
print(df["amfi_code"].nunique())