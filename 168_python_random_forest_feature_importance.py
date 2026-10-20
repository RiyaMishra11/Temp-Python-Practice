"""File 168: Random Forest Feature Importance. Install: pip install pandas scikit-learn"""
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    dataset = load_breast_cancer(as_frame=True)
    X, y = dataset.data, dataset.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=300, random_state=42,
                                   class_weight="balanced")
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.4f}")
    importance = pd.Series(model.feature_importances_, index=X.columns,
                           name="importance").sort_values(ascending=False)
    print("\nTop 10 features:")
    print(importance.head(10).round(4).to_string())
    print("\nImpurity-based importance can be biased; compare with permutation importance.")

if __name__ == "__main__":
    main()
