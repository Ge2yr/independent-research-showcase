"""
This script demonstrates a simple machine learning benchmark using
the digits dataset from scikit‑learn. It trains logistic regression
models with different regularization strengths (C values) and logs
train and test accuracy to a CSV file. A plot of test accuracy
versus C is also saved. This example is safe to share publicly
because it uses open datasets and contains no proprietary code.

Usage:
    python digits_classification.py

Outputs:
    - digits_results.csv: CSV containing C values and train/test accuracy
    - digits_accuracy.png: Line plot of test accuracy vs C

Note: This script uses matplotlib for visualization and does not
specify colors explicitly, adhering to the visualization guidelines.
"""

import pandas as pd
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def main() -> None:
    # Load the digits dataset (similar to MNIST but smaller).
    digits = load_digits()
    X = digits.data
    y = digits.target

    # Split into train and test sets.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Define a few regularization strengths to simulate hyperparameter tuning.
    C_values = [0.1, 1.0, 10.0]
    results = []

    # Train a logistic regression model for each C value.
    for C in C_values:
        # Create and train the model.
        model = LogisticRegression(max_iter=1000, C=C, solver="liblinear")
        model.fit(X_train, y_train)

        # Compute training and test accuracy.
        train_pred = model.predict(X_train)
        test_pred = model.predict(X_test)
        train_acc = accuracy_score(y_train, train_pred)
        test_acc = accuracy_score(y_test, test_pred)

        # Save the results.
        results.append({"C": C, "train_accuracy": train_acc, "test_accuracy": test_acc})

    # Convert results to a DataFrame and save to CSV.
    df = pd.DataFrame(results)
    df.to_csv("digits_results.csv", index=False)

    # Create a line plot of test accuracy vs C.
    plt.figure()
    plt.plot(df["C"], df["test_accuracy"], marker="o")
    plt.xlabel("C (Regularization Strength)")
    plt.ylabel("Test Accuracy")
    plt.title("Logistic Regression on Digits Dataset")
    plt.grid(True)
    plt.savefig("digits_accuracy.png")
    plt.close()


if __name__ == "__main__":
    main()
