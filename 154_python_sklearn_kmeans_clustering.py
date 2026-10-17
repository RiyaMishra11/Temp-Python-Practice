"""File 154: K-Means Clustering. Requires: pip install pandas scikit-learn"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def main():
    data = load_iris(as_frame=True)
    X_scaled = StandardScaler().fit_transform(data.data)
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    print("K-Means Clustering — Iris dataset")
    print(f"Silhouette score: {silhouette_score(X_scaled, labels):.3f}")
    result = data.data.copy()
    result["cluster"] = labels
    print("\nCluster sizes:\n", result["cluster"].value_counts().sort_index())
    print("\nCluster feature means:\n", result.groupby("cluster").mean().round(2))

if __name__ == "__main__":
    main()
