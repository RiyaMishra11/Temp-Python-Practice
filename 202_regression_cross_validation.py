"""
202 — Regression Cross-Validation
Regression models ko multiple folds par evaluate karke reliable performance estimate lena.
"""

from sklearn.datasets import fetch_california_housing
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np


def main():
    # California Housing dataset; first run par internet download ho sakta hai.
    data = fetch_california_housing()
    X, y = data.data, data.target

    model = make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        LinearRegression()
    )

    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    r2_scores = cross_val_score(model, X, y, cv=cv, scoring="r2")
    rmse_scores = -cross_val_score(
        model, X, y, cv=cv, scoring="neg_root_mean_squared_error"
    )

    print("R² scores per fold:", np.round(r2_scores, 3))
    print(f"Mean R²: {r2_scores.mean():.3f} ± {r2_scores.std():.3f}")
    print("RMSE scores per fold:", np.round(rmse_scores, 3))
    print(f"Mean RMSE: {rmse_scores.mean():.3f}")


if __name__ == "__main__":
    main()
