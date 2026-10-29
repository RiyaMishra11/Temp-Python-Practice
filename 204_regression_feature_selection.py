"""
204 — Regression Feature Selection
SelectKBest se regression ke liye useful features choose karna.
"""

from sklearn.datasets import fetch_california_housing
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np


def main():
    data = fetch_california_housing()
    X, y = data.data, data.target
    feature_names = np.array(data.feature_names)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Selection and imputation are fitted on training data only to avoid leakage.
    selector = SelectKBest(score_func=f_regression, k=4)
    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("selector", selector),
        ("regressor", LinearRegression())
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    chosen = feature_names[model.named_steps["selector"].get_support()]
    print("Selected features:", list(chosen))
    print(f"Test R²: {r2_score(y_test, predictions):.3f}")
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    print(f"Test RMSE: {rmse:.3f}")


if __name__ == "__main__":
    main()
