"""191 - Plot learning curves for Logistic Regression.
Install: pip install matplotlib scikit-learn
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    data = load_breast_cancer()
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000))
    sizes, train_scores, valid_scores = learning_curve(
        model, data.data, data.target,
        train_sizes=[0.1, 0.25, 0.4, 0.55, 0.7, 0.85, 1.0],
        cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
        scoring="accuracy", n_jobs=-1)
    train_mean, valid_mean = train_scores.mean(axis=1), valid_scores.mean(axis=1)
    for n, tr, va in zip(sizes, train_mean, valid_mean):
        print(f"samples={n:3d} | train accuracy={tr:.3f} | CV accuracy={va:.3f}")
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, train_mean, marker="o", label="Training score")
    plt.plot(sizes, valid_mean, marker="o", label="Cross-validation score")
    plt.xlabel("Training samples")
    plt.ylabel("Accuracy")
    plt.title("Learning Curve - Logistic Regression")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
