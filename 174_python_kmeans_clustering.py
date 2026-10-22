"""File 174: K-Means Clustering. Install: pip install scikit-learn matplotlib"""
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def main():
    X, _ = make_blobs(n_samples=400, centers=4, cluster_std=1.2, random_state=42)
    X_scaled = StandardScaler().fit_transform(X)
    model = KMeans(n_clusters=4, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    print("Inertia:", round(model.inertia_, 3))
    print("Silhouette score:", round(silhouette_score(X_scaled, labels), 3))
    plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, s=25)
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], marker="X", s=180)
    plt.title("K-Means Clustering")
    plt.xlabel("Scaled feature 1")
    plt.ylabel("Scaled feature 2")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
