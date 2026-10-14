"""141 - Anomaly Detection with IQR | pip install pandas"""
import pandas as pd

def flag_iqr_outliers(series, multiplier=1.5):
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - multiplier * iqr, q3 + multiplier * iqr
    return (series < lower) | (series > upper), lower, upper

def main():
    df = pd.DataFrame({
        "transaction_id": range(1001, 1013),
        "amount": [120, 135, 128, 142, 150, 138, 129, 145, 132, 141, 155, 950]
    })
    df["is_outlier"], lower, upper = flag_iqr_outliers(df["amount"])
    print(f"IQR lower bound: {lower:.2f}; upper bound: {upper:.2f}")
    print(df.to_string(index=False))
    print("\\nFlagged transactions:")
    print(df.loc[df["is_outlier"]].to_string(index=False))

if __name__ == "__main__":
    main()
