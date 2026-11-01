"""216 — Quantile Regression"""
from sklearn.datasets import make_regression
from sklearn.linear_model import QuantileRegressor
from sklearn.metrics import mean_pinball_loss
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

def main():
    X, y = make_regression(n_samples=1000, n_features=5, noise=25, random_state=42)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    for q in (0.1, 0.5, 0.9):
        model = make_pipeline(StandardScaler(),
            QuantileRegressor(quantile=q, alpha=0.01, solver="highs"))
        model.fit(Xtr, ytr)
        p = model.predict(Xte)
        print(f"Quantile {q:.1f}: mean prediction={np.mean(p):.2f}, "
              f"pinball loss={mean_pinball_loss(yte,p,alpha=q):.2f}")

if __name__ == "__main__":
    main()
