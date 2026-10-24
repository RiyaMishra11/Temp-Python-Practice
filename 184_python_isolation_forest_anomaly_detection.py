"""
184 - Anomaly Detection with Isolation Forest
Detect unusual points in a synthetic dataset.

Install: pip install numpy matplotlib scikit-learn
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

def main():
    rng = np.random.default_rng(42)
    normal = rng.normal(0, 1, size=(350, 2))
    unusual = rng.uniform(4, 6, size=(20, 2))
    X = np.vstack([normal, unusual])

    model = IsolationForest(contamination=0.05, random_state=42)
    predictions = model.fit_predict(X)  # 1=inlier, -1=anomaly
    scores = model.decision_function(X)
    anomalies = predictions == -1

    print(f"Total observations: {len(X)}")
    print(f"Detected anomalies: {anomalies.sum()}")
    print("\nFive most unusual observations:")
    for index in np.argsort(scores)[:5]:
        print(f"Index {index}: point={X[index].round(2)}, score={scores[index]:.4f}")

    plt.figure(figsize=(8, 6))
    plt.scatter(X[~anomalies, 0], X[~anomalies, 1], label="Inlier", s=25)
    plt.scatter(X[anomalies, 0], X[anomalies, 1], label="Detected anomaly", s=45)
    plt.title("Isolation Forest Anomaly Detection")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
