"""File 173: Probability Calibration Curve. Install: pip install scikit-learn matplotlib"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibrationDisplay
from sklearn.metrics import brier_score_loss

def main():
    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_test)[:, 1]
    print(f"Brier score (lower is better): {brier_score_loss(y_test, probabilities):.4f}")
    CalibrationDisplay.from_predictions(y_test, probabilities, n_bins=10, strategy="uniform")
    plt.title("Probability Calibration Curve")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
