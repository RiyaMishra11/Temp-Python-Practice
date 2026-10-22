"""File 176: PCA Dimensionality Reduction. Install: pip install scikit-learn matplotlib"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def main():
    dataset = load_iris()
    X_scaled = StandardScaler().fit_transform(dataset.data)
    transformed = PCA(n_components=2).fit_transform(X_scaled)
    pca = PCA(n_components=2).fit(X_scaled)
    print("Explained variance ratio:", pca.explained_variance_ratio_.round(4))
    print("Total variance retained:", round(pca.explained_variance_ratio_.sum(), 4))
    for class_id, class_name in enumerate(dataset.target_names):
        mask = dataset.target == class_id
        plt.scatter(transformed[mask, 0], transformed[mask, 1], label=class_name, s=30)
    plt.xlabel("Principal component 1")
    plt.ylabel("Principal component 2")
    plt.title("Iris Dataset Reduced to Two Dimensions")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
