"""212 — Histogram Gradient Boosting Regression"""
from sklearn.datasets import load_diabetes
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    model = make_pipeline(SimpleImputer(strategy="median"),
        HistGradientBoostingRegressor(max_iter=150, learning_rate=0.06, max_leaf_nodes=15,
                                      l2_regularization=1.0, random_state=42))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Histogram Gradient Boosting Regression")
    print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
    print(f"RMSE: {mean_squared_error(y_test, pred) ** 0.5:.2f}")
    print(f"R²: {r2_score(y_test, pred):.3f}")

if __name__ == "__main__":
    main()
