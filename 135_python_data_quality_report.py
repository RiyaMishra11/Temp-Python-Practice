"""135 - Automated Data Quality Report | Install: pip install pandas"""
from pathlib import Path
import pandas as pd

def build_quality_report(df):
    rows = []
    total = len(df)
    for column in df.columns:
        missing = int(df[column].isna().sum())
        rows.append({
            "column": column,
            "dtype": str(df[column].dtype),
            "missing_count": missing,
            "missing_percent": round(missing / total * 100, 2) if total else 0.0,
            "unique_values": int(df[column].nunique(dropna=True)),
        })
    return pd.DataFrame(rows)

def main():
    data = pd.DataFrame({
        "customer_id": [1, 2, 2, 4, None],
        "customer_name": ["Riya", "Aman", "Aman", None, "Kabir"],
        "age": [22, 25, 25, -3, 30],
        "purchase_amount": [500, 1200, 1200, 700, None],
    })
    report = build_quality_report(data)
    duplicate_rows = int(data.duplicated().sum())
    invalid_ages = int((pd.to_numeric(data["age"], errors="coerce") < 0).sum())
    missing_ids = int(data["customer_id"].isna().sum())

    print("COLUMN-LEVEL DATA QUALITY")
    print(report.to_string(index=False))
    print("\\nDATASET CHECKS")
    print(f"Total rows: {len(data)}")
    print(f"Duplicate rows: {duplicate_rows}")
    print(f"Negative ages: {invalid_ages}")
    print(f"Missing customer IDs: {missing_ids}")

    path = Path("data_quality_report.csv")
    report.to_csv(path, index=False)
    print(f"\\nQuality report saved to: {path.resolve()}")

if __name__ == "__main__":
    main()
