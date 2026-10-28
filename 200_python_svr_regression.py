"""200 - Support Vector Regression. Install: pip install scikit-learn"""
from sklearn.datasets import load_diabetes
from sklearn.svm import SVR
from sklearn.compose import TransformedTargetRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    data = load_diabetes()
    Xtr, Xte, ytr, yte = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    model = TransformedTargetRegressor(
        regressor=make_pipeline(StandardScaler(), SVR(kernel="rbf", C=10, epsilon=0.1)),
        transformer=StandardScaler())
    model.fit(Xtr, ytr); pred = model.predict(Xte)
    print("Support Vector Regression")
    print(f"MAE: {mean_absolute_error(yte, pred):.2f}")
    print(f"RMSE: {mean_squared_error(yte, pred)**0.5:.2f}")
    print(f"R2: {r2_score(yte, pred):.3f}")

if __name__ == "__main__":
    main()
