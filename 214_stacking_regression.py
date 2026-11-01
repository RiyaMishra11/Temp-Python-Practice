"""214 — Stacking Regression"""
from sklearn.datasets import load_diabetes
from sklearn.ensemble import StackingRegressor, RandomForestRegressor, ExtraTreesRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def main():
    d = load_diabetes()
    Xtr, Xte, ytr, yte = train_test_split(d.data, d.target, test_size=0.2, random_state=42)
    estimators = [
        ("ridge", make_pipeline(SimpleImputer(), StandardScaler(), Ridge(alpha=10))),
        ("tree", make_pipeline(SimpleImputer(), DecisionTreeRegressor(max_depth=4, random_state=42))),
        ("forest", make_pipeline(SimpleImputer(), RandomForestRegressor(n_estimators=120, random_state=42, n_jobs=-1))),
        ("extra", make_pipeline(SimpleImputer(), ExtraTreesRegressor(n_estimators=120, random_state=42, n_jobs=-1)))
    ]
    model = StackingRegressor(estimators=estimators, final_estimator=Ridge(), cv=5, n_jobs=-1)
    model.fit(Xtr, ytr)
    p = model.predict(Xte)
    print("Stacking Regression")
    print(f"MAE: {mean_absolute_error(yte,p):.2f}")
    print(f"RMSE: {mean_squared_error(yte,p)**0.5:.2f}")
    print(f"R²: {r2_score(yte,p):.3f}")

if __name__ == "__main__":
    main()
