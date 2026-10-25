"""
187 - Silhouette Analysis
Compare K-Means cluster counts with silhouette scores.
Install: pip install matplotlib scikit-learn
"""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def main():
    X, _ = make_blobs(n_samples=500, centers=4, cluster_std=1.15, random_state=42)
    X = StandardScaler().fit_transform(X)
    candidates = list(range(2, 9))
    scores = []
    for k in candidates:
        labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(X)
        score = silhouette_score(X, labels)
        scores.append(score)
        print(f"k={k}: silhouette score={score:.3f}")
    best_k = candidates[scores.index(max(scores))]
    print(f"Best candidate by silhouette score: k={best_k}")
    plt.figure(figsize=(8, 5))
    plt.plot(candidates, scores, marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Silhouette score")
    plt.title("Silhouette Analysis for K-Means")
    plt.xticks(candidates)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
