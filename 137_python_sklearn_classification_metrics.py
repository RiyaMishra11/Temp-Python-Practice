"""137 - Classification Metrics | pip install scikit-learn"""
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    dataset = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.25, random_state=42,
        stratify=dataset.target)
    model = make_pipeline(StandardScaler(),
                          LogisticRegression(max_iter=2000, random_state=42))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"Accuracy:  {accuracy_score(y_test, pred):.3f}")
    print(f"Precision: {precision_score(y_test, pred):.3f}")
    print(f"Recall:    {recall_score(y_test, pred):.3f}")
    print(f"F1 score:  {f1_score(y_test, pred):.3f}")
    print("\\nConfusion matrix:\\n", confusion_matrix(y_test, pred))
    print("\\nDetailed report:\\n",
          classification_report(y_test, pred, target_names=dataset.target_names))

if __name__ == "__main__":
    main()
