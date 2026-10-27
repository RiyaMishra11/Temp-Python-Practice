"""194 - Random Forest Regression. Install: pip install scikit-learn"""
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=150, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
    print(f"RMSE: {mean_squared_error(y_test, pred) ** 0.5:.2f}")
    print(f"R2: {r2_score(y_test, pred):.3f}")
    print("Top features:")
    for name, score in sorted(zip(data.feature_names, model.feature_importances_), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{name}: {score:.3f}")

if __name__ == "__main__":
    main()
