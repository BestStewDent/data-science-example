import pandas as pd

try:
    from src.data_loader import load_demo_data
except ModuleNotFoundError:  # pragma: no cover - direct script execution fallback
    from data_loader import load_demo_data


def add_summary_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create simple business-oriented features used in the demo notebook."""
    summary = (
        df.groupby("customer_id")
        .agg(
            total_revenue=("amount", "sum"),
            avg_order_value=("amount", "mean"),
            order_count=("order_id", "count"),
            segment=("segment", "first"),
            region=("region", "first"),
        )
        .reset_index()
    )

    summary["revenue_band"] = pd.cut(
        summary["total_revenue"],
        bins=[0, 200, 400, 1000],
        labels=["low", "medium", "high"],
        right=False,
    )
    return summary


def main() -> None:
    df = load_demo_data()
    enriched = add_summary_features(df)
    print(enriched.head())
    print(f"Average revenue: {enriched['total_revenue'].mean():.2f}")


if __name__ == "__main__":
    main()
