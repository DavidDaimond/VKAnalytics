"""
Good news, everyone!

I forgot the news
"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

# from sklearn.cluster import KMeans


class MutualOHE:

    def __init__(self):
        self.checktable = None

    def fit(self, fitdata: list):
        """
        fitdata: list of values which will be used to check and transform.
        """
        self.checktable = fitdata

    def transform_one(self, fl):
        if not (self.checktable is None):
            if not len(fl):
                return np.zeros((self.checktable.shape[0],))
            data = np.array([[friend] for friend in fl])
            return np.sum((data == self.checktable).astype(int), 0)

    def transform(self, fls):
        if not (self.checktable is None):
            t = np.zeros((self.checktable.shape[0],))
            for x in fls:
                t = np.vstack((t, self.transform_one(x)))
            return t


def mutuals_clustering_pca(md, clusterizator, return_clusters=True, **kwargs):
    m_ohe = MutualOHE()
    persons_list = np.array(list(md.keys()))

    m_ohe.fit(persons_list)
    transformed_data = m_ohe.transform(list(md.values()))

    pca = PCA(n_components=2)
    points = pca.fit_transform(transformed_data)

    # ax = plt.axes()
    # ax.set(facecolor="black")

    clusterizator.fit_predict(points)

    for i in range(len(set(clusterizator.labels_))):
        plt.scatter(points[:, 0][clusterizator.labels_ == i], points[:, 1][clusterizator.labels_ == i], 7)

    if return_clusters:
        clusters = []
        for i in range(len(set(clusterizator.labels_))):
            clusters.append(
                list(
                    zip(persons_list[clusterizator.labels_[1:] == i], [clusterizator.labels_ == i])
                )
            )
