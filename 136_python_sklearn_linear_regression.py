"""136 - Scikit-learn Linear Regression | pip install pandas scikit-learn"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    data = pd.DataFrame({
        "study_hours": [1,2,3,4,5,6,7,8,9,10,11,12],
        "practice_tests": [1,1,2,2,3,3,4,4,5,5,6,6],
        "score": [35,40,45,49,55,59,64,68,74,79,84,90],
    })
    X, y = data[["study_hours", "practice_tests"]], data["score"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")
    print(f"R²: {r2_score(y_test, predictions):.3f}")
    print("\\nActual vs predicted:")
    for actual, predicted in zip(y_test.tolist(), predictions.tolist()):
        print(f"Actual={actual:5.1f} | Predicted={predicted:5.1f}")
    new_case = pd.DataFrame({"study_hours": [8], "practice_tests": [4]})
    print("Predicted score:", round(model.predict(new_case)[0], 1))

if __name__ == "__main__":
    main()
