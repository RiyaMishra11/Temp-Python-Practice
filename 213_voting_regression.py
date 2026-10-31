"""213 — Voting Regression"""
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    ridge = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), Ridge(alpha=10.0))
    tree = make_pipeline(SimpleImputer(strategy="median"), DecisionTreeRegressor(max_depth=4, random_state=42))
    forest = make_pipeline(SimpleImputer(strategy="median"),
        RandomForestRegressor(n_estimators=150, max_depth=6, random_state=42, n_jobs=-1))
    model = VotingRegressor(estimators=[("ridge", ridge), ("tree", tree), ("forest", forest)])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Voting Regression")
    print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
    print(f"RMSE: {mean_squared_error(y_test, pred) ** 0.5:.2f}")
    print(f"R²: {r2_score(y_test, pred):.3f}")

if __name__ == "__main__":
    main()
