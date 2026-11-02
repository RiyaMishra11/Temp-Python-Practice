"""221 — Poisson Regression: model a non-negative count-like target."""
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import PoissonRegressor
from sklearn.metrics import mean_poisson_deviance, mean_absolute_error
import numpy as np

def main():
    d = load_diabetes()
    Xtr, Xte, ytr, yte = train_test_split(d.data, d.target, test_size=0.2, random_state=42)
    # Convert the positive demonstration target to integer count-like values.
    ytr = np.maximum(1, np.rint(ytr)).astype(int)
    yte = np.maximum(1, np.rint(yte)).astype(int)
    model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(),
                          PoissonRegressor(alpha=1.0, max_iter=1000))
    model.fit(Xtr, ytr)
    p = np.maximum(model.predict(Xte), 1e-9)
    print("Poisson Regression")
    print(f"MAE: {mean_absolute_error(yte,p):.2f}")
    print(f"Mean Poisson Deviance: {mean_poisson_deviance(yte,p):.3f}")

if __name__ == "__main__":
    main()
