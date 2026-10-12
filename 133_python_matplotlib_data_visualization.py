"""133 - Matplotlib Data Visualization | Install: pip install pandas matplotlib"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = pd.DataFrame({
        "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "sales": [12000, 14500, 13800, 17100, 18600, 21000],
        "expenses": [8000, 9200, 8900, 10300, 11100, 12500],
    })
    data["profit"] = data["sales"] - data["expenses"]
    fig, axes = plt.subplots(2, 1, figsize=(9, 8), constrained_layout=True)

    axes[0].bar(data["month"], data["sales"], label="Sales")
    axes[0].set_title("Monthly Sales")
    axes[0].set_xlabel("Month")
    axes[0].set_ylabel("Amount")
    axes[0].grid(axis="y", alpha=0.25)

    axes[1].plot(data["month"], data["profit"], marker="o", label="Profit")
    axes[1].set_title("Monthly Profit Trend")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Amount")
    axes[1].grid(True, alpha=0.25)

    output = Path("monthly_sales_dashboard.png")
    fig.savefig(output, dpi=150, bbox_inches="tight")
    print(f"Chart saved to: {output.resolve()}")
    plt.show()

if __name__ == "__main__":
    main()
