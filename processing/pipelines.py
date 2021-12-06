from config import MASS_REQ_INTERVAL

from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

from .friends_methods import MutualOHE
from objects import Person
from utils import get_user_friends, get_mutual_dict

from matplotlib import pyplot as plt

import numpy as np


class FriendsMutualPipeline:
    """
    This class take Person as input and then, using some transformations, give you data about user's friends.
    BE CAREFUL WHEN USE THIS CLASS, cause it creates much request, which can be more, than VK limits allow!!!
    """
    def __init__(self):
        self.mutual_ohe = MutualOHE()
        self.pca = PCA(n_components=2)
        self.fl = None
        self.md = None
        self.map = None

    def fit(self, person, access_token, interval=MASS_REQ_INTERVAL):
        self.fl = get_user_friends(access_token=access_token,
                                   user_id=person['id'],
                                   interval=interval,
                                   fields=['id']
                                   )

        self.md = get_mutual_dict(access_token=access_token,
                                  fl=self.fl,
                                  interval=interval,
                                  fields=['id']
                                  )

        persons_list = np.array(list(self.md.keys()))
        self.mutual_ohe.fit(persons_list)

    def predict(self):
        transformed_data = self.mutual_ohe.transform([[person['id'] for person in self[friend]] for friend in self.md])
        self.map = self.pca.fit_transform(transformed_data)

    def fit_predict(self, person, access_token, interval=MASS_REQ_INTERVAL):
        self.fit(person=person, access_token=access_token, interval=interval)
        self.predict(self)

    def show_data(self):
        plt.scatter(self.map[:, 0], self.map[:, 1])
