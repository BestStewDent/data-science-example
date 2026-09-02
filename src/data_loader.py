from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "sample"


def load_customers() -> pd.DataFrame:
    """Load synthetic customer profiles for demo purposes."""
    return pd.read_csv(DATA_DIR / "customers.csv", parse_dates=["signup_date"])


def load_orders() -> pd.DataFrame:
    """Load synthetic customer orders for demo purposes."""
    return pd.read_csv(DATA_DIR / "orders.csv", parse_dates=["order_date"])


def load_demo_data() -> pd.DataFrame:
    """Merge customers and orders into a single demo dataset."""
    customers = load_customers()
    orders = load_orders()
    return customers.merge(orders, on="customer_id", how="left")


if __name__ == "__main__":
    data = load_demo_data()
    print(data.head())
    print(f"Rows: {len(data)}")
    print(f"Unique customers: {data['customer_id'].nunique()}")
