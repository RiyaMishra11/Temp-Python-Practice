"""
183 - Cluster Profiling
Summarize cluster sizes and feature averages after K-Means.

Install: pip install pandas scikit-learn
"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

def main():
    X, _ = make_blobs(n_samples=450, centers=3, n_features=4,
                      cluster_std=1.4, random_state=42)
    columns = ["feature_a", "feature_b", "feature_c", "feature_d"]
    df = pd.DataFrame(X, columns=columns)
    scaled = StandardScaler().fit_transform(df)
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["cluster"] = model.fit_predict(scaled)

    print("Cluster sizes:")
    print(df["cluster"].value_counts().sort_index())
    print("\nMean feature values by cluster (original units):")
    print(df.groupby("cluster")[columns].mean().round(2))
    print("\nMean and standard deviation by cluster:")
    print(df.groupby("cluster")[columns].agg(["mean", "std"]).round(2))

if __name__ == "__main__":
    main()
