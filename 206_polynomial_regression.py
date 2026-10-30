"""206 — Polynomial Regression: model nonlinear relationships."""
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42)
    model = make_pipeline(SimpleImputer(strategy="median"),
        PolynomialFeatures(degree=2, include_bias=False),
        StandardScaler(), LinearRegression())
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Polynomial Regression (degree=2)")
    print(f"R²: {r2_score(y_test, pred):.3f}")
    print(f"RMSE: {mean_squared_error(y_test, pred) ** 0.5:.2f}")

if __name__ == "__main__":
    main()
