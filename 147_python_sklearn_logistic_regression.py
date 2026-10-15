"""
File 147: Logistic Regression Classification
Requirements: pip install pandas scikit-learn
"""
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    data = load_breast_cancer(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    # Pipeline ensures scaling is learned from training data only.
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, random_state=42))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]
    print("Logistic Regression — Breast Cancer Wisconsin dataset")
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print(f"ROC-AUC:  {roc_auc_score(y_test, prob):.3f}")
    print("Confusion matrix (rows=actual, columns=predicted):")
    print(confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, target_names=data.target_names))

if __name__ == "__main__":
    main()
