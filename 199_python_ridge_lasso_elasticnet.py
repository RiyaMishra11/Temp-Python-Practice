"""199 - Compare Ridge, Lasso, and Elastic Net. Install: pip install scikit-learn pandas"""
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    data = load_diabetes()
    Xtr, Xte, ytr, yte = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    models = {"Ridge": Ridge(alpha=1.0), "Lasso": Lasso(alpha=0.1, max_iter=10000),
              "Elastic Net": ElasticNet(alpha=0.1, l1_ratio=0.5, max_iter=10000)}
    rows = []
    for name, estimator in models.items():
        model = make_pipeline(StandardScaler(), estimator)
        model.fit(Xtr, ytr); pred = model.predict(Xte)
        rows.append({"model": name, "MAE": mean_absolute_error(yte, pred),
                     "RMSE": mean_squared_error(yte, pred)**0.5, "R2": r2_score(yte, pred)})
    print(pd.DataFrame(rows).sort_values("RMSE").round(3).to_string(index=False))

if __name__ == "__main__":
    main()
