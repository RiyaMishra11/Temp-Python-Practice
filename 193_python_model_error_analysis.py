"""193 - Examine false positives and false negatives.
Install: pip install pandas scikit-learn
"""
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

def main():
    data = load_breast_cancer(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification report:")
    print(classification_report(y_test, predictions, target_names=data.target_names))
    errors = X_test.copy()
    errors["actual"] = y_test
    errors["predicted"] = predictions
    errors = errors[errors["actual"] != errors["predicted"]].copy()
    labels = dict(enumerate(data.target_names))
    errors["actual_label"] = errors["actual"].map(labels)
    errors["predicted_label"] = errors["predicted"].map(labels)
    print(f"\nMisclassified samples: {len(errors)}")
    cols = ["actual_label", "predicted_label", "mean radius",
            "mean texture", "mean perimeter"]
    print(errors[cols].head(15).round(3).to_string())

if __name__ == "__main__":
    main()
