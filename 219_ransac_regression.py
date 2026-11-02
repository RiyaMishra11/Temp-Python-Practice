"""219 — RANSAC Regression: robust fitting with possible outliers."""
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, RANSACRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def main():
    d = load_diabetes()
    Xtr, Xte, ytr, yte = train_test_split(d.data, d.target, test_size=0.2, random_state=42)
    model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(),
        RANSACRegressor(estimator=LinearRegression(), min_samples=0.5,
                        max_trials=100, random_state=42))
    model.fit(Xtr, ytr)
    p = model.predict(Xte)
    r = model.named_steps["ransacregressor"]
    print("RANSAC Regression")
    print("Training inliers:", int(np.sum(r.inlier_mask_)))
    print("Training outliers:", int(np.sum(~r.inlier_mask_)))
    print(f"MAE: {mean_absolute_error(yte,p):.2f}")
    print(f"RMSE: {mean_squared_error(yte,p)**0.5:.2f}")
    print(f"R²: {r2_score(yte,p):.3f}")

if __name__ == "__main__":
    main()
