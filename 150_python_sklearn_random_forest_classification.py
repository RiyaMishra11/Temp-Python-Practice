"""File 150: Random Forest Classification. Requires: pip install scikit-learn pandas"""
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

def main():
    data = load_breast_cancer(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Random Forest Classification")
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print("\nConfusion matrix:\n", confusion_matrix(y_test, pred))
    print("\nClassification report:\n",
          classification_report(y_test, pred, target_names=data.target_names))
    importance = pd.Series(model.feature_importances_, index=X.columns)
    print("\nTop 10 features:\n", importance.sort_values(ascending=False).head(10))

if __name__ == "__main__":
    main()
