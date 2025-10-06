# Independent Research Showcase

Welcome to my personal research repository.  This project serves as a **sandbox** for developing and evaluating ideas at the intersection of machine learning, dynamical systems and cognitive science.  All examples here use **public datasets and standard algorithms**, ensuring no proprietary methods or data are exposed.

## Motivation

After completing my degree in Psychological Sciences at California State University San Marcos, I continued exploring how systems learn, adapt, and maintain identity over time.  This work sits at the boundary of applied machine learning and theoretical research I call **ROM‑R (Recursive Optimization with Memory and Reflection)**.  While the details of ROM‑R are proprietary, the public experiments in this repository illustrate the *types of questions* I investigate:

- When do iterative algorithms converge to a stable point?  
- How do residual errors evolve during training?  
- Can simple feedback loops produce complex or chaotic behaviour?  

These questions mirror issues in cognitive science—such as how minds stabilize self‑concepts—and inform the development of practical AI systems.

## Repository Structure

| Folder | Description |
|-------|------------|
| **`ml_benchmarks/`** | Supervised and unsupervised learning tasks on public datasets (digits classification, diabetes regression, iris clustering).  Each project includes a script, saved metrics (CSV/JSON), and plots. |
| **`residual_monitors/`** | Demonstrations of optimization dynamics and convergence (e.g. gradient descent on synthetic data) with logged loss values and visualizations. |
| **`simulations/`** | Explorations of simple dynamical systems (e.g. logistic map) to illustrate stability, bifurcation and chaos. |
| **`automation/`**, **`visualization/`** | Placeholders for future scripts to automate sweeps and enhance plotting; currently minimal. |
| **`docs/REFLECTIONS.md`** | In‑depth narrative explaining what each experiment shows and how it relates to the larger ROM‑R research questions without disclosing proprietary methods. |

### Quick Start

To run any of the benchmarks locally:

1. Create a new Python environment (e.g. via conda).  
2. Install dependencies (`pip install -r requirements.txt` or install scikit‑learn, pandas, matplotlib).
3. Navigate to the desired directory and execute the script with appropriate arguments (see docstrings in each script).  
4. Inspect the generated CSV/JSON logs and plots in the same folder.

Because each experiment uses public data, you can freely modify the scripts, reproduce the results, and extend the analyses.

## Reflections and ROM‑R Context

For high‑level commentary on what these experiments demonstrate and how they connect to my ROM‑R research, see [`docs/REFLECTIONS.md`](docs/REFLECTIONS.md).  This document explains the purpose, observations and takeaways of each benchmark and outlines how concepts like *fixed points*, *residual dynamics* and *self‑consistency* inform my ongoing theoretical work.

## Contact

I am currently seeking opportunities to collaborate on applied research projects that blend **machine learning, neuroscience, and systems theory**.  If you are a researcher or a team interested in these areas, feel free to reach out.  Note that I cannot share proprietary algorithms or detailed ROM‑R implementations, but I am always happy to discuss the high‑level ideas and the science behind them.
