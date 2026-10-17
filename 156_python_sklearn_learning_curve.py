"""File 156: Learning curve analysis. Requires: pip install pandas scikit-learn matplotlib"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import learning_curve, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def main():
    data = load_iris(as_frame=True)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    sizes, train_scores, valid_scores = learning_curve(
        model, data.data, data.target, cv=cv, scoring="accuracy",
        train_sizes=[0.2, 0.4, 0.6, 0.8, 1.0], n_jobs=-1
    )
    summary = pd.DataFrame({
        "training_samples": sizes,
        "train_accuracy_mean": train_scores.mean(axis=1),
        "validation_accuracy_mean": valid_scores.mean(axis=1)
    })
    print("Learning Curve — Logistic Regression")
    print(summary.round(3).to_string(index=False))
    plt.plot(sizes, train_scores.mean(axis=1), marker="o", label="Training accuracy")
    plt.plot(sizes, valid_scores.mean(axis=1), marker="o", label="Validation accuracy")
    plt.xlabel("Number of training samples")
    plt.ylabel("Accuracy")
    plt.title("Learning Curve")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
