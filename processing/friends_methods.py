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
        if self.checktable is None:
            return None
        t = np.zeros((self.checktable.shape[0],))
        for x in fls:
            t = np.vstack((t, self.transform_one(x)))
        return t

