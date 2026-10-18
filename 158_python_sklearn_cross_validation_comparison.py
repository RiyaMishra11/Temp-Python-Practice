"""File 158: Compare models with cross-validation. Install: pip install pandas scikit-learn"""
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def main():
    data = load_iris(as_frame=True)
    X, y = data.data, data.target
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    models = {
        "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
        "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=150, random_state=42),
        "SVM": make_pipeline(StandardScaler(), SVC())
    }
    rows = []
    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy", n_jobs=-1)
        rows.append({"model": name, "mean_accuracy": scores.mean(), "std_accuracy": scores.std()})
    print("Model Comparison — 5-fold Cross-Validation")
    print(pd.DataFrame(rows).sort_values("mean_accuracy", ascending=False).round(3).to_string(index=False))

if __name__ == "__main__":
    main()
