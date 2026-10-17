"""File 157: Probability calibration evaluation. Requires: pip install scikit-learn matplotlib"""
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.calibration import calibration_curve
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    X, y = make_classification(
        n_samples=1200, n_features=12, n_informative=7, n_redundant=2,
        weights=[0.6, 0.4], random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_test)[:, 1]
    print("Probability Calibration — Logistic Regression")
    print(f"Brier score (lower is better): {brier_score_loss(y_test, probabilities):.4f}")
    observed, predicted = calibration_curve(y_test, probabilities, n_bins=10)
    plt.plot(predicted, observed, marker="o", label="Model")
    plt.plot([0, 1], [0, 1], linestyle="--", label="Perfect calibration")
    plt.xlabel("Mean predicted probability")
    plt.ylabel("Observed positive fraction")
    plt.title("Calibration Curve")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
