"""
128 - Pandas Data Cleaning
Learn: missing values, duplicate rows, type conversion, string cleanup, and validation.

Install dependency:
    pip install pandas

Run:
    python 128_python_pandas_data_cleaning.py
"""
import pandas as pd


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of a sales DataFrame."""
    cleaned = df.copy()

    # Normalize column names and text fields.
    cleaned.columns = (
        cleaned.columns.astype(str).str.strip().str.lower().str.replace(" ", "_")
    )
    for column in ("customer", "product"):
        if column in cleaned.columns:
            cleaned[column] = cleaned[column].astype("string").str.strip().str.title()

    # Convert numeric columns safely; invalid values become missing.
    for column in ("quantity", "unit_price"):
        if column in cleaned.columns:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    if "order_date" in cleaned.columns:
        cleaned["order_date"] = pd.to_datetime(
            cleaned["order_date"], errors="coerce"
        )

    # Remove exact duplicates and rows missing essential fields.
    cleaned = cleaned.drop_duplicates()
    required = [c for c in ("customer", "product", "quantity", "unit_price") if c in cleaned]
    if required:
        cleaned = cleaned.dropna(subset=required)

    # Business-rule validation.
    if "quantity" in cleaned.columns:
        cleaned = cleaned[cleaned["quantity"] > 0]
    if "unit_price" in cleaned.columns:
        cleaned = cleaned[cleaned["unit_price"] >= 0]

    if {"quantity", "unit_price"}.issubset(cleaned.columns):
        cleaned["revenue"] = cleaned["quantity"] * cleaned["unit_price"]

    return cleaned.reset_index(drop=True)


def main() -> None:
    sample = pd.DataFrame(
        [
            {"Customer": " riya ", "Product": " notebook", "Quantity": "2", "Unit Price": "50", "Order Date": "2026-10-01"},
            {"Customer": "AMAN", "Product": "pen ", "Quantity": "3", "Unit Price": "10", "Order Date": "2026-10-02"},
            {"Customer": " riya ", "Product": " notebook", "Quantity": "2", "Unit Price": "50", "Order Date": "2026-10-01"},
            {"Customer": "Neha", "Product": "bag", "Quantity": "-1", "Unit Price": "500", "Order Date": "bad-date"},
            {"Customer": None, "Product": "pencil", "Quantity": "4", "Unit Price": "5", "Order Date": "2026-10-03"},
        ]
    )
    cleaned = clean_sales_data(sample)
    print("CLEANED DATA")
    print(cleaned.to_string(index=False))
    print("\\nSUMMARY")
    print(f"Rows before cleaning: {len(sample)}")
    print(f"Rows after cleaning:  {len(cleaned)}")
    if "revenue" in cleaned:
        print(f"Total revenue:        {cleaned['revenue'].sum():.2f}")


if __name__ == "__main__":
    main()
