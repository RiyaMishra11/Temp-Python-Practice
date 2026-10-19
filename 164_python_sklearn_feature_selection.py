"""
File 164: Feature Selection with SelectKBest
Ranks numeric features using ANOVA F-scores for a classification task.
Install: pip install pandas scikit-learn
"""

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def main():
    df = pd.DataFrame({
        "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 5, 6, 1, 7, 4, 8, 3],
        "attendance": [45, 50, 55, 62, 70, 75, 80, 92, 52, 68, 78, 40, 88, 65, 95, 58],
        "social_media_hours": [8, 7, 6, 5, 4, 3, 2, 1, 7, 5, 3, 9, 2, 6, 1, 8],
        "previous_score": [40, 45, 50, 55, 65, 70, 75, 90, 48, 60, 72, 35, 85, 58, 94, 52],
        "passed": [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    })

    X = df.drop(columns="passed")
    y = df["passed"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    selector = SelectKBest(score_func=f_classif, k=2)
    selector.fit(X_train, y_train)

    scores = pd.DataFrame({
        "feature": X.columns,
        "f_score": selector.scores_,
        "selected": selector.get_support(),
    }).sort_values("f_score", ascending=False)

    print("Feature scores (higher can indicate more class separation):")
    print(scores.round(3).to_string(index=False))

    # Keep feature selection inside the pipeline so it is fit only on training data.
    model = make_pipeline(
        SelectKBest(score_func=f_classif, k=2),
        StandardScaler(),
        LogisticRegression(max_iter=1000),
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("\nTest accuracy using the selected two features:",
          round(accuracy_score(y_test, predictions), 3))


if __name__ == "__main__":
    main()
