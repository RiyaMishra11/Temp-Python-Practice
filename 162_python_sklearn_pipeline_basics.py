"""
File 162: Scikit-learn Pipeline Basics
Demonstrates preprocessing and model training in a single pipeline.
Install: pip install pandas scikit-learn
"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report


def main():
    # Small sample dataset; replace this with your own CSV if needed.
    df = pd.DataFrame({
        "age": [22, 35, 47, 29, 52, 41, 33, 26, 58, 38, 45, 31],
        "income": [25000, 52000, 68000, 39000, 82000, 61000, 48000, 32000, 90000, 57000, 72000, 42000],
        "city": ["Delhi", "Jaipur", "Delhi", "Noida", "Jaipur", "Noida", "Delhi", "Jaipur", "Noida", "Delhi", "Jaipur", "Noida"],
        "purchased": [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
    })

    X = df.drop(columns="purchased")
    y = df["purchased"]

    numeric_features = ["age", "income"]
    categorical_features = ["city"]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ])

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Accuracy:", round(accuracy_score(y_test, predictions), 3))
    print("\nClassification report:")
    print(classification_report(y_test, predictions, zero_division=0))


if __name__ == "__main__":
    main()
