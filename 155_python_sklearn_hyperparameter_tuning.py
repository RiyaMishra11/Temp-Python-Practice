"""File 155: GridSearchCV hyperparameter tuning. Requires: pip install scikit-learn"""
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

def main():
    data = load_iris(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
    )
    pipeline = make_pipeline(StandardScaler(), SVC())
    params = {"svc__C": [0.1, 1, 10], "svc__kernel": ["linear", "rbf"],
              "svc__gamma": ["scale", "auto"]}
    search = GridSearchCV(pipeline, params, cv=5, scoring="accuracy", n_jobs=-1)
    search.fit(X_train, y_train)
    pred = search.predict(X_test)
    print("GridSearchCV — SVM")
    print("Best parameters:", search.best_params_)
    print(f"Best CV accuracy: {search.best_score_:.3f}")
    print(f"Test accuracy: {accuracy_score(y_test, pred):.3f}")
    print(classification_report(y_test, pred, target_names=data.target_names))

if __name__ == "__main__":
    main()
