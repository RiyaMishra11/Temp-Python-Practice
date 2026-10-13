"""138 - K-Means Clustering | pip install pandas scikit-learn"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def main():
    customers = pd.DataFrame({
        "annual_spend": [120,150,180,210,240,900,950,1000,1050,1100,350,400],
        "visits_per_year": [2,3,3,4,4,12,13,14,15,16,5,6],
    })
    scaled = StandardScaler().fit_transform(customers)
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    customers["cluster"] = model.fit_predict(scaled)
    print("CUSTOMER SEGMENTS")
    print(customers.sort_values("cluster").to_string(index=False))
    print("\\nCLUSTER SUMMARY")
    print(customers.groupby("cluster").agg(
        customer_count=("cluster", "size"),
        avg_annual_spend=("annual_spend", "mean"),
        avg_visits=("visits_per_year", "mean")).round(2).to_string())
    print(f"\\nSilhouette score: {silhouette_score(scaled, customers['cluster']):.3f}")

if __name__ == "__main__":
    main()
