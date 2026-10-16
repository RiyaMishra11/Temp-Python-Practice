"""File 153: Principal Component Analysis (PCA). Requires: pip install scikit-learn pandas"""
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def main():
    data = load_wine(as_frame=True)
    X = data.data
    # Standardize features before PCA because their scales differ.
    X_scaled = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2, random_state=42)
    components = pca.fit_transform(X_scaled)
    result = pd.DataFrame(components, columns=["PC1", "PC2"])
    result["wine_class"] = data.target.to_numpy()
    print("PCA — Wine dataset")
    print(f"Original feature count: {X.shape[1]}")
    print("Reduced feature count:", 2)
    for i, ratio in enumerate(pca.explained_variance_ratio_, start=1):
        print(f"PC{i} explained variance: {ratio:.3%}")
    print(f"Total variance retained: {pca.explained_variance_ratio_.sum():.3%}")
    print("\nFirst five transformed rows:\n", result.head().to_string(index=False))

if __name__ == "__main__":
    main()
