"""File 179: Gaussian Mixture Model Clustering. Install: pip install scikit-learn matplotlib"""
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def main():
    X, _ = make_blobs(n_samples=350, centers=3, cluster_std=1.4, random_state=42)
    X = StandardScaler().fit_transform(X)
    model = GaussianMixture(n_components=3, covariance_type="full", random_state=42)
    labels = model.fit_predict(X)
    print("Converged:", model.converged_)
    print("BIC:", round(model.bic(X), 2))
    print("AIC:", round(model.aic(X), 2))
    print("Silhouette score:", round(silhouette_score(X, labels), 3))
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=25)
    plt.title("Gaussian Mixture Model Clustering")
    plt.xlabel("Standardized feature 1")
    plt.ylabel("Standardized feature 2")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
