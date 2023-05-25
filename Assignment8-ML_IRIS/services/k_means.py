import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import PyQt6

matplotlib.use("agg")


def k_means_cluster(x, df):
    km = KMeans(3)
    clusts = km.fit_predict(x)

    # Plot the clusters obtained using k means
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(
        km.cluster_centers_[:, 3],
        km.cluster_centers_[:, 0],
        km.cluster_centers_[:, 2],
        s=250,
        marker="o",
        c="red",
        label="centroids",
    )
    ax.scatter(
        df["petal width (cm)"],
        df["sepal length (cm)"],
        df["petal length (cm)"],
        c=clusts,
        s=20,
        cmap="winter",
    )

    ax.set_title("K-Means Clustering")
    ax.set_xlabel("Petal Width")
    ax.set_ylabel("Sepal Length")
    ax.set_zlabel("Petal Length")
    ax.legend()
    plt.savefig("Kmeans_plot.png")
