"""
File 163: Compare Feature Scaling Methods
Compares StandardScaler and MinMaxScaler on numeric columns.
Install: pip install pandas scikit-learn
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def main():
    data = pd.DataFrame({
        "age": [18, 25, 32, 45, 60],
        "annual_income": [18000, 32000, 45000, 90000, 150000],
        "visits_per_month": [1, 3, 4, 8, 12],
    })

    print("Original data:")
    print(data.to_string(index=False))

    standard_scaled = pd.DataFrame(
        StandardScaler().fit_transform(data),
        columns=data.columns
    )
    minmax_scaled = pd.DataFrame(
        MinMaxScaler().fit_transform(data),
        columns=data.columns
    )

    print("\nStandardScaler (approximately mean 0, standard deviation 1):")
    print(standard_scaled.round(3).to_string(index=False))

    print("\nMinMaxScaler (values between 0 and 1):")
    print(minmax_scaled.round(3).to_string(index=False))

    print("\nTip: fit the scaler on training data only, then transform test data.")
    print("This prevents information from the test set leaking into training.")


if __name__ == "__main__":
    main()
