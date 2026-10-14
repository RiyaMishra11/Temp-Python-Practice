"""143 - Model Cross-Validation | pip install scikit-learn"""
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    dataset = load_diabetes()
    X, y = dataset.data, dataset.target
    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    models = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": make_pipeline(StandardScaler(), Ridge(alpha=1.0)),
    }
    print("5-FOLD CROSS-VALIDATION (R²)")
    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=cv, scoring="r2")
        print(f"{name}: scores={scores.round(3).tolist()}")
        print(f"  Mean R²={scores.mean():.3f}; Std={scores.std():.3f}")

if __name__ == "__main__":
    main()
