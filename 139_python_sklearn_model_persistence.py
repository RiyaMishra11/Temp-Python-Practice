"""139 - Save and Load a Scikit-learn Model | pip install pandas scikit-learn joblib
Only load model files from sources you trust."""
from pathlib import Path
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    training = pd.DataFrame({
        "ad_spend": [100,150,200,250,300,350,400],
        "sales": [1000,1300,1700,2000,2400,2700,3100],
    })
    model = LinearRegression().fit(training[["ad_spend"]], training["sales"])
    model_path = Path("sales_prediction_model.joblib")
    joblib.dump(model, model_path)

    loaded_model = joblib.load(model_path)
    new_data = pd.DataFrame({"ad_spend": [225,450]})
    predictions = loaded_model.predict(new_data)
    print(f"Model saved to: {model_path.resolve()}")
    for spend, prediction in zip(new_data["ad_spend"], predictions):
        print(f"Ad spend={spend} -> predicted sales={prediction:.2f}")

if __name__ == "__main__":
    main()
