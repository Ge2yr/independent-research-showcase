"""
Matplotlib example: Plotting a sine wave.

This script demonstrates creating a simple line plot of a sine wave using
matplotlib. Use this as a template for other visualizations.
"""
import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
