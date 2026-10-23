"""File 181: Compare Clustering Metrics. Install: pip install scikit-learn"""
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

def main():
    X, _ = make_blobs(n_samples=400, centers=4, cluster_std=1.3, random_state=42)
    X = StandardScaler().fit_transform(X)
    labels = KMeans(n_clusters=4, n_init=10, random_state=42).fit_predict(X)
    print("Silhouette score (higher is generally better):", round(silhouette_score(X, labels), 4))
    print("Davies-Bouldin index (lower is generally better):", round(davies_bouldin_score(X, labels), 4))
    print("Calinski-Harabasz score (higher is generally better):", round(calinski_harabasz_score(X, labels), 4))
    print("Use multiple metrics and domain knowledge when judging clusters.")

if __name__ == "__main__":
    main()
