"""215 — Multi-Output Regression"""
from sklearn.datasets import make_regression
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

def main():
    X, y = make_regression(n_samples=1200, n_features=12, n_informative=8,
                           n_targets=3, noise=15, random_state=42)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    model = make_pipeline(SimpleImputer(), StandardScaler(),
                          MultiOutputRegressor(Ridge(alpha=1.0)))
    model.fit(Xtr, ytr)
    p = model.predict(Xte)
    print("Multi-Output Regression")
    for i in range(y.shape[1]):
        rmse = mean_squared_error(yte[:, i], p[:, i]) ** 0.5
        print(f"Target {i+1}: RMSE={rmse:.2f}, R²={r2_score(yte[:,i],p[:,i]):.3f}")
    print("Sample predictions:\n", np.round(p[:5], 2))

if __name__ == "__main__":
    main()
