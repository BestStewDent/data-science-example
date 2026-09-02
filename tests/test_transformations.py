import pandas as pd

from src.data_loader import load_demo_data
from src.feature_engineering import add_summary_features


def test_demo_data_contains_expected_columns():
    df = load_demo_data()
    expected = {"customer_id", "segment", "signup_date", "region", "order_id", "order_date", "product_category", "amount", "is_repeat_purchase"}
    assert expected.issubset(set(df.columns))


def test_customer_summary_has_valid_ranges():
    df = load_demo_data()
    summary = add_summary_features(df)

    assert len(summary) == df["customer_id"].nunique()
    assert summary["total_revenue"].ge(0).all()
    assert summary["avg_order_value"].ge(0).all()
    assert set(summary["revenue_band"].dropna().unique()) <= {"low", "medium", "high"}


def test_repeat_purchase_flag_is_boolean_like():
    df = load_demo_data()
    assert df["is_repeat_purchase"].isin([True, False]).all()
