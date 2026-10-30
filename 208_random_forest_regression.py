"""208 — Random Forest Regression: combine multiple decision trees."""
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42)
    model = make_pipeline(SimpleImputer(strategy="median"),
        RandomForestRegressor(n_estimators=200, max_depth=6,
            min_samples_leaf=3, random_state=42, n_jobs=-1))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Random Forest Regression")
    print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
    print(f"RMSE: {mean_squared_error(y_test, pred) ** 0.5:.2f}")
    print(f"R²: {r2_score(y_test, pred):.3f}")
    forest = model.named_steps["randomforestregressor"]
    order = np.argsort(forest.feature_importances_)
    plt.barh(np.array(data.feature_names)[order], forest.feature_importances_[order])
    plt.xlabel("Feature importance")
    plt.title("Random Forest Feature Importance")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
