"""
203 — Regression Learning Curves
Training examples ki quantity badhne par model ki performance kaise change hoti hai.
"""

from sklearn.datasets import fetch_california_housing
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.model_selection import learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = fetch_california_housing()
    X, y = data.data, data.target

    model = make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        Ridge(alpha=1.0)
    )

    sizes, train_scores, valid_scores = learning_curve(
        model,
        X,
        y,
        train_sizes=np.linspace(0.1, 1.0, 8),
        cv=5,
        scoring="r2",
        n_jobs=-1,
        random_state=42
    )

    train_mean = train_scores.mean(axis=1)
    valid_mean = valid_scores.mean(axis=1)

    print("Training sizes:", sizes)
    print("Mean training R²:", np.round(train_mean, 3))
    print("Mean validation R²:", np.round(valid_mean, 3))

    plt.plot(sizes, train_mean, marker="o", label="Training R²")
    plt.plot(sizes, valid_mean, marker="o", label="Validation R²")
    plt.xlabel("Number of training examples")
    plt.ylabel("R² score")
    plt.title("Ridge Regression Learning Curve")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
