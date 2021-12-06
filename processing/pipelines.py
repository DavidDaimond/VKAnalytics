from config import MASS_REQ_INTERVAL

from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

from .friends_methods import MutualOHE
from objects import Person
from utils import get_user_friends, get_mutual_dict

import numpy as np


class FriendsMutualPipeline:
    """
    This class take Person as input and then, using some transformations, give you data about user's friends.
    BE CAREFUL WHEN USE THIS CLASS, cause it creates much request, which can be more, than VK limits allow!!!
    """
    def __init__(self, person: Person):
        self.person = person
        self.mutual_ohe = MutualOHE()
        self.pca = PCA(n_components=2)
        self.fl = None
        self.md = None
        self.map = None

    def process(self, access_token, interval=MASS_REQ_INTERVAL):
        self.fl = get_user_friends(access_token=access_token,
                                   user_id=self.person['data']['id'],
                                   interval=interval
                                   )

        self.md = get_mutual_dict(access_token=access_token,
                                  fl=self.fl,
                                  interval=interval
                                  )

    def show_data(self):
        pass
