"""Diabetes regression example using scikit-learn linear regression.

This script demonstrates a simple supervised regression task on the Diabetes dataset
from scikit-learn. It loads the dataset, splits it into training and test sets,
fits a linear regression model, evaluates it using common metrics, and saves
the predictions and metrics to CSV files.

It also generates a scatter plot comparing the true target values to the model
predictions to visualize how well the model captures the relationship.

Outputs:
    - diabetes_regression_results.csv : CSV with columns for true target and
      predicted target on the test set.
    - diabetes_regression_metrics.csv : CSV with metrics (MSE, MAE, R2).
    - diabetes_regression_plot.png : Plot of true vs predicted values.

Usage: python diabetes_regression.py

This script was generated with the assistance of AI coding tools and is provided
as a public demonstration of regression modeling and evaluation skills.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt


def main():
    # Load the diabetes dataset
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Compute evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Save predictions to CSV
    results_df = pd.DataFrame(
        {"y_true": y_test, "y_pred": y_pred}
    )
    results_csv_path = "diabetes_regression_results.csv"
    results_df.to_csv(results_csv_path, index=False)

    # Save metrics to CSV
    metrics_df = pd.DataFrame(
        {"mse": [mse], "mae": [mae], "r2": [r2]}
    )
    metrics_csv_path = "diabetes_regression_metrics.csv"
    metrics_df.to_csv(metrics_csv_path, index=False)

    # Plot true vs predicted values
    plt.figure()
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("True Target")
    plt.ylabel("Predicted Target")
    plt.title("Linear Regression on Diabetes Dataset")
    plt.grid(True, linestyle="--", alpha=0.3)
    plot_path = "diabetes_regression_plot.png"
    plt.savefig(plot_path)
    plt.close()

    # Print summary to console
    print("Linear Regression on Diabetes dataset")
    print(f"Mean squared error: {mse:.2f}")
    print(f"Mean absolute error: {mae:.2f}")
    print(f"R^2 score: {r2:.3f}")
    print(f"Results saved to {results_csv_path} and {metrics_csv_path}")
    print(f"Plot saved to {plot_path}")


if __name__ == "__main__":
    main()