"""File 152: Gaussian Naive Bayes classification. Requires: pip install scikit-learn"""
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def main():
    data = load_wine(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = GaussianNB()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Gaussian Naive Bayes — Wine dataset")
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print("\nConfusion matrix:\n", confusion_matrix(y_test, pred))
    print("\nClassification report:\n",
          classification_report(y_test, pred, target_names=data.target_names))
    sample = X_test.iloc[[0]]
    print("Example predicted class:", data.target_names[model.predict(sample)[0]])

if __name__ == "__main__":
    main()
