"""File 167: Hyperparameter Tuning with GridSearchCV. Install: pip install scikit-learn"""
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def main():
    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=5000))
    ])
    params = {"model__C": [0.01, 0.1, 1.0, 10.0],
              "model__solver": ["liblinear", "lbfgs"]}
    search = GridSearchCV(pipeline, params, cv=5, scoring="accuracy", n_jobs=-1)
    search.fit(X_train, y_train)
    predictions = search.predict(X_test)
    print("Best parameters:", search.best_params_)
    print(f"Best mean CV accuracy: {search.best_score_:.4f}")
    print(f"Held-out test accuracy: {accuracy_score(y_test, predictions):.4f}")

if __name__ == "__main__":
    main()
