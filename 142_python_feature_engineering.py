"""142 - Feature Engineering | pip install pandas scikit-learn"""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def main():
    df = pd.DataFrame({
        "age": [22, 35, None, 28, 41, 31],
        "monthly_spend": [1200, 2500, 1800, 900, 3200, 2100],
        "visits": [2, 5, 3, 1, 7, 4],
        "membership": ["Basic", "Premium", "Basic", "Basic", "Premium", "Standard"],
        "signup_date": ["2026-01-10", "2025-11-03", "2026-03-12",
                        "2026-02-01", "2025-08-19", "2026-01-28"],
    })
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    df["signup_month"] = df["signup_date"].dt.month
    df["spend_per_visit"] = df["monthly_spend"] / df["visits"]

    numeric = ["age", "monthly_spend", "visits", "signup_month", "spend_per_visit"]
    categorical = ["membership"]
    transformer = ColumnTransformer([
        ("numeric", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]), numeric),
        ("categorical", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]), categorical),
    ])
    matrix = transformer.fit_transform(df[numeric + categorical])
    print("Engineered feature preview:")
    print(df[numeric + categorical].to_string(index=False))
    print(f"\\nTransformed feature matrix shape: {matrix.shape}")
    print("Feature names:", transformer.get_feature_names_out().tolist())

if __name__ == "__main__":
    main()
