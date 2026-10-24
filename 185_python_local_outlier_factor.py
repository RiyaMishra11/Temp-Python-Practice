"""
185 - Local Outlier Factor (LOF)
Find observations unusual relative to their local neighborhood.

Install: pip install numpy matplotlib scikit-learn
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

def main():
    rng = np.random.default_rng(7)
    main_group = rng.normal(0, 0.8, size=(300, 2))
    small_group = rng.normal(3.2, 0.25, size=(18, 2))
    isolated = rng.uniform(-4, 4, size=(12, 2))
    X = np.vstack([main_group, small_group, isolated])

    model = LocalOutlierFactor(n_neighbors=20, contamination=0.04)
    predictions = model.fit_predict(X)  # 1=inlier, -1=outlier
    lof_scores = -model.negative_outlier_factor_
    outliers = predictions == -1

    print(f"Observations: {len(X)}")
    print(f"LOF outliers detected: {outliers.sum()}")
    print("\nTop 10 observations by LOF score:")
    for index in np.argsort(lof_scores)[-10:][::-1]:
        print(f"Index {index}: point={X[index].round(2)}, LOF={lof_scores[index]:.3f}")

    plt.figure(figsize=(8, 6))
    plt.scatter(X[~outliers, 0], X[~outliers, 1], label="Inlier", s=25)
    plt.scatter(X[outliers, 0], X[outliers, 1], label="Outlier", s=45)
    plt.title("Local Outlier Factor")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
