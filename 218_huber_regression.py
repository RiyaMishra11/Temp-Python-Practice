"""218 — Huber Regression: robust linear regression."""
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import HuberRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def main():
    d = load_diabetes()
    Xtr, Xte, ytr, yte = train_test_split(d.data, d.target, test_size=0.2, random_state=42)
    model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(),
                          HuberRegressor(epsilon=1.35, max_iter=1000))
    model.fit(Xtr, ytr)
    p = model.predict(Xte)
    print("Huber Regression")
    print(f"MAE: {mean_absolute_error(yte,p):.2f}")
    print(f"RMSE: {mean_squared_error(yte,p)**0.5:.2f}")
    print(f"R²: {r2_score(yte,p):.3f}")

if __name__ == "__main__":
    main()
