"""File 175: DBSCAN Clustering. Install: pip install scikit-learn matplotlib"""
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def main():
    X, _ = make_moons(n_samples=400, noise=0.07, random_state=42)
    X_scaled = StandardScaler().fit_transform(X)
    labels = DBSCAN(eps=0.25, min_samples=5).fit_predict(X_scaled)
    clusters = set(labels) - {-1}
    noise_count = int((labels == -1).sum())
    print("Clusters found:", len(clusters))
    print("Noise points:", noise_count)
    mask = labels != -1
    if len(set(labels[mask])) > 1:
        print("Silhouette score (excluding noise):", round(silhouette_score(X_scaled[mask], labels[mask]), 3))
    plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, s=25)
    plt.title("DBSCAN Clustering (-1 indicates noise)")
    plt.xlabel("Scaled feature 1")
    plt.ylabel("Scaled feature 2")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
