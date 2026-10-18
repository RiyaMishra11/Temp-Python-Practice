"""File 159: Imbalanced classification using class weights. Install: pip install scikit-learn"""
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, average_precision_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    X, y = make_classification(n_samples=2000, n_features=15, n_informative=7,
        n_redundant=3, weights=[0.93, 0.07], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    model = make_pipeline(StandardScaler(),
        LogisticRegression(class_weight="balanced", max_iter=2000, random_state=42))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]
    print("Imbalanced Classification — class_weight='balanced'")
    print("Confusion matrix (rows=actual, columns=predicted):")
    print(confusion_matrix(y_test, pred))
    print("\nClassification report:")
    print(classification_report(y_test, pred, zero_division=0))
    print(f"Average precision (positive class): {average_precision_score(y_test, prob):.3f}")

if __name__ == "__main__":
    main()
