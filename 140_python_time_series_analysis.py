"""140 - Time Series Analysis | pip install pandas"""
import pandas as pd

def main():
    dates = pd.date_range("2026-01-01", periods=180, freq="D")
    df = pd.DataFrame({
        "date": dates,
        "sales": [800 + (i * 7) % 350 + (i // 30) * 40 for i in range(180)]
    }).set_index("date")
    monthly = df["sales"].resample("MS").sum().to_frame("monthly_sales")
    monthly["rolling_3_month_avg"] = monthly["monthly_sales"].rolling(3).mean()
    monthly["mom_change_pct"] = monthly["monthly_sales"].pct_change() * 100
    print("MONTHLY SALES ANALYSIS")
    print(monthly.round(2).to_string())
    print("\\nHighest-sales month:", monthly["monthly_sales"].idxmax().strftime("%Y-%m"))

if __name__ == "__main__":
    main()
