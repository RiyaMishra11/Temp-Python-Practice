"""198 - Polynomial Regression. Install: pip install numpy matplotlib scikit-learn"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def main():
    rng = np.random.default_rng(42)
    X = np.sort(rng.uniform(-3, 3, 180)).reshape(-1, 1)
    y = 0.5 * X[:, 0]**2 + np.sin(2 * X[:, 0]) + rng.normal(0, 0.7, len(X))
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)
    grid = np.linspace(-3, 3, 300).reshape(-1, 1)
    plt.figure(figsize=(9, 6))
    plt.scatter(Xte[:, 0], yte, s=22, label="Test data")
    for degree in [1, 2, 5, 10]:
        model = make_pipeline(PolynomialFeatures(degree, include_bias=False), StandardScaler(), LinearRegression())
        model.fit(Xtr, ytr)
        pred = model.predict(Xte)
        print(f"degree={degree:2d} | RMSE={mean_squared_error(yte, pred)**0.5:.3f} | R2={r2_score(yte, pred):.3f}")
        plt.plot(grid[:, 0], model.predict(grid), label=f"Degree {degree}")
    plt.title("Polynomial Regression Degrees")
    plt.xlabel("X"); plt.ylabel("y"); plt.legend(); plt.tight_layout(); plt.show()

if __name__ == "__main__":
    main()
