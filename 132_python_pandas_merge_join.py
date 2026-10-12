"""132 - Pandas Merge and Join | Install: pip install pandas"""
import pandas as pd

def main():
    customers = pd.DataFrame({
        "customer_id": [101, 102, 103, 104],
        "customer_name": ["Riya", "Aman", "Neha", "Kabir"],
        "city": ["Jaipur", "Delhi", "Pune", "Jaipur"],
    })
    orders = pd.DataFrame({
        "order_id": [5001, 5002, 5003, 5004, 5005],
        "customer_id": [101, 102, 101, 105, 104],
        "amount": [1200, 800, 450, 600, 1500],
    })

    merged = orders.merge(customers, on="customer_id", how="left",
                          validate="many_to_one", indicator=True)
    print("ORDERS WITH CUSTOMER DETAILS")
    print(merged.to_string(index=False))

    print("\\nORDERS WITH UNKNOWN CUSTOMER IDS")
    unmatched = merged.loc[merged["_merge"] == "left_only", ["order_id", "customer_id"]]
    print(unmatched.to_string(index=False) if not unmatched.empty else "None")

    summary = (merged.loc[merged["_merge"] == "both"]
               .groupby(["customer_id", "customer_name"], as_index=False)
               .agg(order_count=("order_id", "nunique"), total_amount=("amount", "sum"))
               .sort_values("total_amount", ascending=False))
    print("\\nCUSTOMER SUMMARY")
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
