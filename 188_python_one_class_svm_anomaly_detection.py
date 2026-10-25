"""
188 - One-Class SVM Anomaly Detection
Train on a mostly normal dataset and flag unusual points.
Install: pip install numpy matplotlib scikit-learn
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

def main():
    rng = np.random.default_rng(188)
    normal = rng.normal(loc=0, scale=1, size=(300, 2))
    unusual = rng.uniform(low=4, high=6, size=(15, 2))
    X = np.vstack([normal, unusual])
    X_scaled = StandardScaler().fit_transform(X)
    model = OneClassSVM(kernel="rbf", nu=0.05, gamma="scale")
    predictions = model.fit_predict(X_scaled)  # 1=inlier, -1=outlier
    outliers = predictions == -1
    print(f"Observations: {len(X)}")
    print(f"Flagged as outliers: {outliers.sum()}")
    plt.figure(figsize=(8, 6))
    plt.scatter(X[~outliers, 0], X[~outliers, 1], label="Inlier", s=25)
    plt.scatter(X[outliers, 0], X[outliers, 1], label="Outlier", s=45)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("One-Class SVM Anomaly Detection")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
