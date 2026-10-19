"""
File 165: ROC Curve and ROC-AUC Evaluation
Evaluates a binary classifier using predicted probabilities.
Install: pip install pandas scikit-learn matplotlib
"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import RocCurveDisplay, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main():
    X, y = make_classification(
        n_samples=500,
        n_features=8,
        n_informative=5,
        n_redundant=1,
        weights=[0.65, 0.35],
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    model.fit(X_train, y_train)

    predicted_labels = model.predict(X_test)
    predicted_probabilities = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, predicted_probabilities)
    print(f"ROC-AUC: {auc:.3f}")
    print("\nClassification report at the model's default threshold:")
    print(classification_report(y_test, predicted_labels, zero_division=0))

    RocCurveDisplay.from_predictions(y_test, predicted_probabilities)
    plt.title(f"ROC Curve (AUC = {auc:.3f})")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
