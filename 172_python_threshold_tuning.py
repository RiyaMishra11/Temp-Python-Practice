"""File 172: Classification Threshold Tuning. Install: pip install scikit-learn"""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score

def main():
    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_test)[:, 1]
    print("Threshold | Precision | Recall | F1")
    print("-" * 42)
    for threshold in [0.3, 0.4, 0.5, 0.6, 0.7]:
        predictions = (probabilities >= threshold).astype(int)
        print(f"{threshold:9.2f} | {precision_score(y_test, predictions, zero_division=0):9.3f} | "
              f"{recall_score(y_test, predictions, zero_division=0):6.3f} | "
              f"{f1_score(y_test, predictions, zero_division=0):.3f}")
    print("\nChoose a threshold based on the cost of false positives and false negatives.")

if __name__ == "__main__":
    main()
