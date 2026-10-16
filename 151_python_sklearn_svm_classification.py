"""File 151: Support Vector Machine classification. Requires: pip install scikit-learn"""
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def main():
    data = load_iris(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    # Scale features inside a pipeline to avoid data leakage.
    model = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1.0))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("SVM Classification — Iris dataset")
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print(classification_report(y_test, pred, target_names=data.target_names))
    sample = X_test.iloc[[0]]
    print("Example predicted class:", data.target_names[model.predict(sample)[0]])

if __name__ == "__main__":
    main()
