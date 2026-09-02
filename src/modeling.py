from typing import Dict

import pandas as pd

try:
    from src.feature_engineering import add_summary_features
    from src.data_loader import load_demo_data
except ModuleNotFoundError:  # pragma: no cover - direct script execution fallback
    from feature_engineering import add_summary_features
    from data_loader import load_demo_data


def build_demo_scorecard() -> Dict[str, float]:
    """Return a few toy metrics for a presentation summary."""
    df = load_demo_data()
    customer_summary = add_summary_features(df)

    return {
        "average_revenue": round(float(customer_summary["total_revenue"].mean()), 2),
        "total_customers": int(customer_summary["customer_id"].nunique()),
        "high_value_customers": int((customer_summary["segment"] == "high_value").sum()),
        "average_order_value": round(float(customer_summary["avg_order_value"].mean()), 2),
    }


def main() -> None:
    scorecard = build_demo_scorecard()
    for k, v in scorecard.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
