"""File 177: Hierarchical Clustering Dendrogram. Install: pip install scikit-learn scipy matplotlib"""
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

def main():
    X, _ = make_blobs(n_samples=80, centers=3, cluster_std=1.1, random_state=42)
    X_scaled = StandardScaler().fit_transform(X)
    linked = linkage(X_scaled, method="ward")
    plt.figure(figsize=(10, 5))
    dendrogram(linked, truncate_mode="lastp", p=20, leaf_rotation=45)
    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Cluster or sample")
    plt.ylabel("Ward distance")
    plt.tight_layout()
    plt.show()
    print("Dendrogram plotted. Larger merge heights indicate more distant groups.")

if __name__ == "__main__":
    main()
