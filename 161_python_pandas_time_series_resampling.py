"""File 161: Time-series resampling and rolling averages. Install: pip install pandas numpy matplotlib"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    rng = np.random.default_rng(42)
    dates = pd.date_range("2025-01-01", periods=180, freq="D")
    daily_sales = 500 + np.linspace(0, 120, len(dates)) + rng.normal(0, 35, len(dates))
    df = pd.DataFrame({"date": dates, "sales": daily_sales}).set_index("date")
    weekly = df["sales"].resample("W").sum()
    monthly = df["sales"].resample("MS").sum()
    df["rolling_7_day_avg"] = df["sales"].rolling(7, min_periods=1).mean()
    print("Time-Series Resampling Demo")
    print("\nWeekly sales totals (first 8 weeks):")
    print(weekly.head(8).round(2).to_string())
    print("\nMonthly sales totals:")
    print(monthly.round(2).to_string())
    df[["sales", "rolling_7_day_avg"]].plot(figsize=(10, 5), title="Daily Sales and 7-Day Rolling Average")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
