"""
File 148: Gradient Boosting Regression
Requirements: pip install pandas scikit-learn
"""
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    data = load_diabetes(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = GradientBoostingRegressor(
        n_estimators=150, learning_rate=0.05, max_depth=2, random_state=42
    )
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, pred) ** 0.5
    print("Gradient Boosting Regression — Diabetes dataset")
    print(f"MAE:  {mean_absolute_error(y_test, pred):.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²:   {r2_score(y_test, pred):.3f}")
    importance = pd.Series(model.feature_importances_, index=X.columns)
    print("\nFeature importance:")
    print(importance.sort_values(ascending=False).to_string())

if __name__ == "__main__":
    main()
