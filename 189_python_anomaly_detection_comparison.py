"""
189 - Anomaly Detection Model Comparison
Compare Isolation Forest, LOF, and One-Class SVM.
Install: pip install numpy pandas scikit-learn
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

def main():
    rng = np.random.default_rng(189)
    normal = rng.normal(0, 1, size=(300, 2))
    unusual = rng.uniform(4, 6, size=(15, 2))
    X = np.vstack([normal, unusual])
    X_scaled = StandardScaler().fit_transform(X)
    models = {
        "Isolation Forest": IsolationForest(contamination=0.05, random_state=42),
        "Local Outlier Factor": LocalOutlierFactor(n_neighbors=20, contamination=0.05),
        "One-Class SVM": OneClassSVM(nu=0.05, gamma="scale"),
    }
    rows = []
    for name, model in models.items():
        labels = model.fit_predict(X_scaled)
        rows.append({
            "model": name,
            "flagged_outliers": int((labels == -1).sum()),
            "flagged_percentage": round(float((labels == -1).mean() * 100), 2),
        })
    results = pd.DataFrame(rows)
    print("Anomaly detection comparison:")
    print(results.to_string(index=False))
    print("\nModels may flag different points; validate results against domain knowledge.")

if __name__ == "__main__":
    main()
