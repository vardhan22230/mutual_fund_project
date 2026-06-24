
import pandas as pd
from sqlalchemy import create_engine

print("Creating SQLite database...")

engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets

nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

txn_df = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

perf_df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

# Load into SQLite

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("\nAll tables loaded successfully.")


print("\nVerifying row counts...")

print("fact_nav rows:", len(nav_df))
print("fact_transactions rows:", len(txn_df))
print("fact_performance rows:", len(perf_df))