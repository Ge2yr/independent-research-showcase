# Independent Research Skills Showcase

## Overview
This repository highlights practical machine learning and data analysis skills developed through independent research and experimentation. While my proprietary ROM‑R framework and company research remain confidential, all examples here use public datasets and open‑source tools.  You’ll find applied examples across classification, regression, clustering, chaotic simulations, optimization monitoring, and automation.

## Repository Structure

### `ml_benchmarks/`
Examples of supervised and unsupervised learning using **scikit‑learn** and **PyTorch**.  Each script logs results to CSV files and produces plots for easy interpretation.

- **`digits_classification.py`** — Trains logistic regression on the sklearn digits dataset; logs train/test accuracy to `digits_results.csv` and saves `digits_accuracy.png`.
- **`diabetes_regression.py`** — Runs a linear regression on the diabetes dataset; outputs predictions (`diabetes_regression_results.csv`), evaluation metrics (`diabetes_regression_metrics.csv`), and a scatter plot (`diabetes_regression_plot.png`).
- **`iris_kmeans.py`** — Performs K‑Means clustering on the Iris dataset with PCA for visualization; reports silhouette and adjusted Rand index; saves cluster assignments (`iris_kmeans_results.csv`), metrics (`iris_kmeans_metrics.csv`), and a cluster plot (`iris_kmeans_clusters.png`).
- **Digit benchmark files** (from earlier exercises) are also included: `digits_classification.py`, `digits_results.csv`, `digits_accuracy.png`.

### `simulations/`
Toy simulations illustrating recursive systems and chaotic dynamics.

- **`logistic_map.py`** — Generates a time series of the logistic map, saving values to `logistic_map.csv` and plotting the trajectory in `logistic_map.png`.  This demonstrates how simple nonlinear systems can exhibit complex behaviour.

### `residual_monitors/`
Small utilities for monitoring optimization and detecting instability during training.

- **`gradient_descent_demo.py`** — Implements a basic gradient descent loop for linear regression; logs loss at each iteration (`gradient_descent_losses.csv`) and plots the loss curve (`gradient_descent_loss.png`).  Shows how to instrument an optimization process.
- **`monitor.py`** — Generic hooks for checking gradient norms or other simple training diagnostics.

### `automation/` and `visualization/`
Placeholders for experiment orchestration scripts and custom visualization utilities.  These can be expanded to automate sweeps or create standardized plots for reports.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ge2yr/independent-research-showcase.git
   cd independent-research-showcase
   ```
2. **Create and activate a Python environment** (example using conda):
   ```bash
   conda create -n irs python=3.11 -y
   conda activate irs
   pip install -r requirements.txt
   ```
3. **Run an example**:
   ```bash
   # Digit classification
   python ml_benchmarks/digits_classification.py

   # Diabetes regression
   python ml_benchmarks/diabetes_regression.py

   # Iris clustering
   python ml_benchmarks/iris_kmeans.py

   # Logistic map simulation
   python simulations/logistic_map.py
   ```
   Outputs will appear in the corresponding folders as `.csv` logs and `.png` plots.  Inspect the CSVs for numeric results and open the images for visual summaries.

## Contributing & Notes

- All code and data here are non‑proprietary.  Proprietary algorithms and ROM‑R research remain under NDA and are not shared.
- Feel free to fork or clone this repository for learning purposes.  If you suggest improvements or have ideas for additional public experiments, open an issue or submit a pull request.

---

*This repository serves as a public portfolio of applied ML and research skills while keeping confidential work protected.*
