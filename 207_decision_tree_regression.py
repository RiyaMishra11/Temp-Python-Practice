"""207 — Decision Tree Regression: predict continuous values with a tree."""
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42)
    model = make_pipeline(SimpleImputer(strategy="median"),
        DecisionTreeRegressor(max_depth=4, min_samples_leaf=5, random_state=42))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Decision Tree Regression")
    print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
    print(f"RMSE: {mean_squared_error(y_test, pred) ** 0.5:.2f}")
    print(f"R²: {r2_score(y_test, pred):.3f}")
    tree = model.named_steps["decisiontreeregressor"]
    plt.figure(figsize=(16, 8))
    plot_tree(tree, feature_names=data.feature_names, filled=True, rounded=True)
    plt.title("Decision Tree Regressor")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
