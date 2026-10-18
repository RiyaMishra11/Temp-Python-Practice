"""File 160: Outlier detection using IQR and z-scores. Install: pip install pandas numpy"""
import numpy as np
import pandas as pd

def main():
    rng = np.random.default_rng(42)
    values = np.concatenate([rng.normal(50, 8, 100), [5, 7, 95, 110]])
    df = pd.DataFrame({"value": values})
    q1, q3 = df["value"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["iqr_outlier"] = (df["value"] < lower) | (df["value"] > upper)
    mean, std = df["value"].mean(), df["value"].std(ddof=0)
    df["z_score"] = (df["value"] - mean) / std
    df["zscore_outlier"] = df["z_score"].abs() > 3
    print("Outlier Detection Demo")
    print(f"IQR bounds: {lower:.2f} to {upper:.2f}")
    print("IQR outlier count:", int(df["iqr_outlier"].sum()))
    print("Z-score outlier count:", int(df["zscore_outlier"].sum()))
    print("\nFlagged rows (IQR method):")
    print(df.loc[df["iqr_outlier"]].round(2).to_string(index=False))

if __name__ == "__main__":
    main()
