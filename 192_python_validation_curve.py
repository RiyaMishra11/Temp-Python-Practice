"""192 - Explore Logistic Regression regularization with a validation curve.
Install: pip install matplotlib scikit-learn
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import validation_curve, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    data = load_breast_cancer()
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000))
    c_values = np.logspace(-3, 3, 7)
    train_scores, valid_scores = validation_curve(
        model, data.data, data.target,
        param_name="logisticregression__C", param_range=c_values,
        cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
        scoring="accuracy", n_jobs=-1)
    train_mean, valid_mean = train_scores.mean(axis=1), valid_scores.mean(axis=1)
    for c, tr, va in zip(c_values, train_mean, valid_mean):
        print(f"C={c:.4g} | train accuracy={tr:.3f} | CV accuracy={va:.3f}")
    plt.figure(figsize=(8, 5))
    plt.semilogx(c_values, train_mean, marker="o", label="Training score")
    plt.semilogx(c_values, valid_mean, marker="o", label="CV score")
    plt.xlabel("Regularization parameter C (log scale)")
    plt.ylabel("Accuracy")
    plt.title("Validation Curve - Logistic Regression")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
