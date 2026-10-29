"""
205 — Regression Hyperparameter Tuning
GridSearchCV ke through Ridge Regression ka best alpha select karna.
"""

from sklearn.datasets import fetch_california_housing
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, KFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np


def main():
    data = fetch_california_housing()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("model", Ridge())
    ])

    param_grid = {"model__alpha": [0.01, 0.1, 1.0, 10.0, 100.0]}
    cv = KFold(n_splits=5, shuffle=True, random_state=42)

    search = GridSearchCV(
        pipeline,
        param_grid=param_grid,
        scoring="r2",
        cv=cv,
        n_jobs=-1
    )
    search.fit(X_train, y_train)

    predictions = search.predict(X_test)
    print("Best parameters:", search.best_params_)
    print(f"Best cross-validation R²: {search.best_score_:.3f}")
    print(f"Test R²: {r2_score(y_test, predictions):.3f}")
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    print(f"Test RMSE: {rmse:.3f}")


if __name__ == "__main__":
    main()
