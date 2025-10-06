"""Iris KMeans clustering example with PCA for visualization.

This script demonstrates unsupervised learning on the famous Iris dataset.
It loads the Iris dataset from scikit-learn, standardizes the features,
reduces dimensionality to two principal components for visualization,
applies KMeans clustering to group samples into three clusters, and then
saves the cluster assignments and evaluation metrics to CSV files.

It also generates a scatter plot of the first two principal components,
colored by predicted cluster labels with cluster centers annotated.

Outputs:
    - iris_kmeans_results.csv : DataFrame with true labels, predicted cluster,
      and principal component coordinates.
    - iris_kmeans_metrics.csv : CSV with silhouette score and adjusted rand index.
    - iris_kmeans_clusters.png : Plot of clusters in PCA space.

Usage: python iris_kmeans.py

This script was generated with the assistance of AI coding tools and
is provided as a public demonstration of clustering and visualization skills.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score
import matplotlib.pyplot as plt


def main():
    # Load iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names

    # Standardize features
    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)

    # Reduce dimensionality to two principal components for visualization
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_std)

    # Fit KMeans with 3 clusters
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_std)

    # Compute evaluation metrics
    sil_score = silhouette_score(X_std, clusters)
    ari_score = adjusted_rand_score(y, clusters)

    # Save results to CSV
    results_df = pd.DataFrame(
        {
            "pc1": X_pca[:, 0],
            "pc2": X_pca[:, 1],
            "true_label": [target_names[i] for i in y],
            "cluster": clusters,
        }
    )
    results_csv_path = "iris_kmeans_results.csv"
    results_df.to_csv(results_csv_path, index=False)

    # Save metrics to CSV
    metrics_df = pd.DataFrame(
        {"silhouette_score": [sil_score], "adjusted_rand_index": [ari_score]}
    )
    metrics_csv_path = "iris_kmeans_metrics.csv"
    metrics_df.to_csv(metrics_csv_path, index=False)

    # Plot clusters
    plt.figure()
    scatter = plt.scatter(
        X_pca[:, 0], X_pca[:, 1], c=clusters, s=50, cmap="viridis", alpha=0.7
    )
    centers = kmeans.cluster_centers_
    centers_pca = pca.transform(centers)
    plt.scatter(
        centers_pca[:, 0],
        centers_pca[:, 1],
        c="red",
        s=100,
        marker="X",
        label="Cluster centers",
    )
    plt.title("KMeans Clustering of Iris Dataset (PCA-reduced)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.3)
    plot_path = "iris_kmeans_clusters.png"
    plt.savefig(plot_path)
    plt.close()

    # Print summary to console
    print("KMeans clustering on Iris dataset")
    print(f"Silhouette score: {sil_score:.3f}")
    print(f"Adjusted Rand index: {ari_score:.3f}")
    print(f"Results saved to {results_csv_path} and {metrics_csv_path}")
    print(f"Plot saved to {plot_path}")


if __name__ == "__main__":
    main()
