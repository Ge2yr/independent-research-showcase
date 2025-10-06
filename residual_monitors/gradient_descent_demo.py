"""
This script performs a simple linear regression using gradient descent
on synthetic data and logs the loss over iterations. It demonstrates
basic optimization and residual monitoring skills.

Outputs:
    - gradient_descent_losses.csv: CSV containing epochs and loss values
    - gradient_descent_loss.png: Line plot of loss vs epoch
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    np.random.seed(0)
    # Generate synthetic linear data with noise
    X = np.random.rand(100)
    true_slope = 2.5
    true_intercept = 1.0
    noise = 0.1 * np.random.randn(100)
    y = true_intercept + true_slope * X + noise

    # Initialize parameters
    b0 = 0.0
    b1 = 0.0
    learning_rate = 0.2
    epochs = 50

    losses = []

    # Gradient descent loop
    for epoch in range(epochs):
        y_pred = b0 + b1 * X
        error = y_pred - y
        loss = np.mean(error ** 2)
        losses.append({"epoch": epoch, "loss": loss})

        # Compute gradients
        grad_b0 = 2 * np.mean(error)
        grad_b1 = 2 * np.mean(error * X)

        # Update parameters
        b0 -= learning_rate * grad_b0
        b1 -= learning_rate * grad_b1

    # Save the loss log to CSV
    df = pd.DataFrame(losses)
    df.to_csv("gradient_descent_losses.csv", index=False)

    # Plot the loss curve
    plt.figure()
    plt.plot(df["epoch"], df["loss"], marker="o")
    plt.xlabel("Epoch")
    plt.ylabel("MSE Loss")
    plt.title("Gradient Descent on Synthetic Linear Data")
    plt.grid(True)
    plt.savefig("gradient_descent_loss.png")
    plt.close()


if __name__ == "__main__":
    main()
