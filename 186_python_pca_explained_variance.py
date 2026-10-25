"""
186 - PCA Explained Variance
Fit PCA and inspect how much variance each component explains.
Install: pip install scikit-learn matplotlib
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def main():
    data = load_wine()
    X = StandardScaler().fit_transform(data.data)
    pca = PCA().fit(X)
    individual = pca.explained_variance_ratio_
    cumulative = individual.cumsum()
    for i, (single, total) in enumerate(zip(individual, cumulative), start=1):
        print(f"PC{i}: explained={single:.2%}, cumulative={total:.2%}")
    components = range(1, len(individual) + 1)
    plt.figure(figsize=(8, 5))
    plt.bar(components, individual, label="Individual variance")
    plt.plot(components, cumulative, marker="o", label="Cumulative variance")
    plt.xlabel("Principal component")
    plt.ylabel("Explained variance ratio")
    plt.title("PCA Explained Variance - Wine Dataset")
    plt.xticks(list(components))
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
