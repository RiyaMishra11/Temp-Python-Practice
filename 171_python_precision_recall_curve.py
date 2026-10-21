"""File 171: Precision-Recall Curve. Install: pip install scikit-learn matplotlib"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import PrecisionRecallDisplay, average_precision_score

def main():
    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_test)[:, 1]
    score = average_precision_score(y_test, probabilities)
    print(f"Average precision: {score:.4f}")
    PrecisionRecallDisplay.from_predictions(y_test, probabilities)
    plt.title(f"Precision-Recall Curve (AP = {score:.3f})")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
