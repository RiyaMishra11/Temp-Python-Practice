"""File 169: Permutation Feature Importance. Install: pip install pandas scikit-learn"""
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def main():
    dataset = load_breast_cancer(as_frame=True)
    X, y = dataset.data, dataset.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
    model.fit(X_train, y_train)
    print(f"Test accuracy: {accuracy_score(y_test, model.predict(X_test)):.4f}")
    result = permutation_importance(
        model, X_test, y_test, n_repeats=10, random_state=42,
        scoring="accuracy", n_jobs=-1)
    importance = pd.DataFrame({
        "feature": X.columns,
        "mean_importance": result.importances_mean,
        "std_importance": result.importances_std
    }).sort_values("mean_importance", ascending=False)
    print("\nTop 10 features by permutation importance:")
    print(importance.head(10).round(4).to_string(index=False))

if __name__ == "__main__":
    main()
