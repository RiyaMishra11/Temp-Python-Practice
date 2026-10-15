"""
File 146: Decision Tree Classification
Requirements: pip install pandas scikit-learn
"""
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

def main():
    data = load_iris(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Decision Tree Classification — Iris dataset")
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print(classification_report(y_test, pred, target_names=data.target_names))
    print("Readable tree rules:")
    print(export_text(model, feature_names=list(X.columns)))
    sample = X_test.iloc[[0]]
    print("Example prediction:", data.target_names[model.predict(sample)[0]])

if __name__ == "__main__":
    main()
