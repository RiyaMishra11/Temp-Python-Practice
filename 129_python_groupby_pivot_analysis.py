"""
129 - GroupBy and Pivot Analysis
Learn: groupby, aggregation, sorting, pivot tables, and top-N analysis.

Install dependency:
    pip install pandas

Run:
    python 129_python_groupby_pivot_analysis.py
"""
import pandas as pd


def analyze_orders(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    required = {"region", "category", "sales", "profit"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    data = df.copy()
    data["sales"] = pd.to_numeric(data["sales"], errors="coerce")
    data["profit"] = pd.to_numeric(data["profit"], errors="coerce")
    data = data.dropna(subset=["region", "category", "sales", "profit"])

    by_region = (
        data.groupby("region", as_index=False)
        .agg(total_sales=("sales", "sum"), total_profit=("profit", "sum"),
             order_count=("sales", "size"))
        .sort_values("total_sales", ascending=False)
    )
    by_category = (
        data.groupby("category", as_index=False)
        .agg(total_sales=("sales", "sum"), average_profit=("profit", "mean"))
        .sort_values("total_sales", ascending=False)
    )
    pivot = pd.pivot_table(
        data, index="region", columns="category", values="sales",
        aggfunc="sum", fill_value=0, margins=True
    )
    top_orders = data.nlargest(5, "sales").reset_index(drop=True)

    return {
        "by_region": by_region,
        "by_category": by_category,
        "sales_pivot": pivot,
        "top_orders": top_orders,
    }


def main() -> None:
    orders = pd.DataFrame([
        {"region": "North", "category": "Office", "sales": 1200, "profit": 250},
        {"region": "South", "category": "Tech", "sales": 3500, "profit": 700},
        {"region": "North", "category": "Tech", "sales": 2400, "profit": 420},
        {"region": "West", "category": "Office", "sales": 900, "profit": 110},
        {"region": "South", "category": "Office", "sales": 1500, "profit": 200},
        {"region": "West", "category": "Tech", "sales": 2800, "profit": 560},
    ])
    for title, result in analyze_orders(orders).items():
        print(f"\\n=== {title.replace('_', ' ').upper()} ===")
        print(result.to_string(index=False))


if __name__ == "__main__":
    main()
