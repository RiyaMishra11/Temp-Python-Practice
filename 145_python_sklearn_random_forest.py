"""145 - Random Forest Regression; install: pip install pandas scikit-learn"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    data = pd.DataFrame({
        "ad_spend": [100,120,150,180,200,220,250,280,300,330,350,400,420,450,480,500,530,550,580,600],
        "website_visits": [900,950,1100,1200,1300,1450,1550,1700,1800,1950,2050,2250,2300,2450,2600,2700,2850,2950,3100,3250],
        "sales": [950,1020,1150,1280,1390,1460,1630,1770,1850,2020,2110,2350,2390,2510,2700,2780,2910,3040,3180,3320],
    })
    X = data[["ad_spend", "website_visits"]]
    y = data["sales"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)
    model = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")
    print(f"R²: {r2_score(y_test, predictions):.3f}")
    importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    print("\\nFEATURE IMPORTANCE")
    print(importance.to_string())

if __name__ == "__main__":
    main()
