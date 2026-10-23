"""File 178: Agglomerative Clustering. Install: pip install scikit-learn matplotlib"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def main():
    data = load_iris()
    X = StandardScaler().fit_transform(data.data)
    labels = AgglomerativeClustering(n_clusters=3, linkage="ward").fit_predict(X)
    print("Cluster sizes:", {int(k): int((labels == k).sum()) for k in set(labels)})
    print("Silhouette score:", round(silhouette_score(X, labels), 3))
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=30)
    plt.title("Agglomerative Clustering of Iris Data")
    plt.xlabel("Standardized feature 1")
    plt.ylabel("Standardized feature 2")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
