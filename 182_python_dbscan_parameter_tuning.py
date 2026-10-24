"""
182 - DBSCAN Parameter Tuning
Compare DBSCAN results across eps settings.

Install: pip install numpy scikit-learn matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def main():
    X, _ = make_moons(n_samples=500, noise=0.07, random_state=42)
    X = StandardScaler().fit_transform(X)
    eps_values = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
    results = []
    for eps in eps_values:
        labels = DBSCAN(eps=eps, min_samples=5).fit_predict(X)
        clusters = set(labels) - {-1}
        noise = np.mean(labels == -1)
        mask = labels != -1
        score = None
        if len(clusters) >= 2 and len(set(labels[mask])) >= 2:
            score = silhouette_score(X[mask], labels[mask])
        results.append((eps, labels))
        score_text = f"{score:.3f}" if score is not None else "N/A"
        print(f"eps={eps:.2f} | clusters={len(clusters)} | noise={noise:.1%} | silhouette={score_text}")
    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    for ax, (eps, labels) in zip(axes.flat, results):
        ax.scatter(X[:, 0], X[:, 1], c=labels, cmap="tab10", s=15)
        ax.set_title(f"eps={eps:.2f}")
        ax.set_xticks([])
        ax.set_yticks([])
    fig.suptitle("DBSCAN Results Across eps Values")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
