"""201 - Regression Residual Diagnostics. Install: pip install matplotlib scikit-learn"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    data = load_diabetes()
    Xtr, Xte, ytr, yte = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
    model.fit(Xtr, ytr); pred = model.predict(Xte)
    residuals = yte - pred
    print(f"Test RMSE: {mean_squared_error(yte, pred)**0.5:.2f}")
    print(f"Mean residual: {residuals.mean():.2f}")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].scatter(pred, residuals, alpha=0.7)
    axes[0].axhline(0, linestyle="--")
    axes[0].set(title="Residuals vs Predicted", xlabel="Predicted value", ylabel="Residual")
    axes[1].scatter(yte, pred, alpha=0.7)
    low, high = min(yte.min(), pred.min()), max(yte.max(), pred.max())
    axes[1].plot([low, high], [low, high], linestyle="--")
    axes[1].set(title="Actual vs Predicted", xlabel="Actual value", ylabel="Predicted value")
    plt.tight_layout(); plt.show()

if __name__ == "__main__":
    main()
