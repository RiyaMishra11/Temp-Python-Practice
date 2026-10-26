"""190 - Compare tree and permutation feature importance.
Install: pip install pandas scikit-learn matplotlib
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

def main():
    data = load_breast_cancer(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=250, random_state=42)
    model.fit(X_train, y_train)
    perm = permutation_importance(model, X_test, y_test, n_repeats=10,
                                  random_state=42, scoring="accuracy")
    results = pd.DataFrame({
        "feature": X.columns,
        "tree_importance": model.feature_importances_,
        "permutation_importance": perm.importances_mean
    }).sort_values("permutation_importance", ascending=False)
    print(f"Test accuracy: {model.score(X_test, y_test):.3f}")
    print(results.head(15).round(4).to_string(index=False))
    results.head(12).sort_values("permutation_importance").plot(
        x="feature", y=["tree_importance", "permutation_importance"],
        kind="barh", figsize=(10, 7))
    plt.title("Feature Importance Methods")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
