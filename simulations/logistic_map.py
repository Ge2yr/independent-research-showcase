"""
Simple logistic map simulation.

The logistic map is a classic example of how complex, chaotic behaviour can
arise from a simple non-linear dynamical equation. This script iterates
the logistic map and prints values, detecting when values exceed a threshold.
"""
def logistic_map(r, x0, n):
    """Iterate the logistic map r * x * (1 - x) starting from x0 for n steps."""
    x = x0
    values = []
    for _ in range(n):
        x = r * x * (1 - x)
        values.append(x)
    return values


def main():
    r = 3.7  # parameter value leading to chaotic behaviour
    x0 = 0.5  # initial condition
    iterations = 30
    values = logistic_map(r, x0, iterations)
    for i, v in enumerate(values):
        print(f"Step {i+1}: {v:.4f}")
        if v > 0.9 or v < 0.1:
            print("  Warning: value approaching boundary (0 or 1)")


if __name__ == '__main__':
    main()
