"""211 — AdaBoost Regression"""
from sklearn.datasets import load_diabetes
from sklearn.ensemble import AdaBoostRegressor
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    base_tree = DecisionTreeRegressor(max_depth=3, random_state=42)
    model = make_pipeline(SimpleImputer(strategy="median"),
        AdaBoostRegressor(estimator=base_tree, n_estimators=100, learning_rate=0.05, loss="square", random_state=42))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("AdaBoost Regression")
    print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
    print(f"RMSE: {mean_squared_error(y_test, pred) ** 0.5:.2f}")
    print(f"R²: {r2_score(y_test, pred):.3f}")

if __name__ == "__main__":
    main()
