"""217 — Regression Model Comparison"""
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

def main():
    d = load_diabetes()
    Xtr, Xte, ytr, yte = train_test_split(d.data, d.target, test_size=0.2, random_state=42)
    models = {
        "Linear Regression": make_pipeline(SimpleImputer(), StandardScaler(), LinearRegression()),
        "Ridge": make_pipeline(SimpleImputer(), StandardScaler(), Ridge()),
        "Decision Tree": make_pipeline(SimpleImputer(), DecisionTreeRegressor(max_depth=4, random_state=42)),
        "Random Forest": make_pipeline(SimpleImputer(), RandomForestRegressor(n_estimators=150, random_state=42, n_jobs=-1)),
        "Gradient Boosting": make_pipeline(SimpleImputer(), GradientBoostingRegressor(n_estimators=100, random_state=42)),
        "SVR": make_pipeline(SimpleImputer(), StandardScaler(), SVR(C=10))
    }
    print(f"{'Model':<22} {'MAE':>9} {'RMSE':>9} {'R²':>8}")
    print("-" * 52)
    for name, model in models.items():
        model.fit(Xtr, ytr)
        p = model.predict(Xte)
        print(f"{name:<22} {mean_absolute_error(yte,p):>9.2f} "
              f"{mean_squared_error(yte,p)**0.5:>9.2f} {r2_score(yte,p):>8.3f}")

if __name__ == "__main__":
    main()
