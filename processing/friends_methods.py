"""
Good news, everyone!

I forgot the news
"""
import numpy as np
from time import sleep

from .filters import can_access_closed
from config import API_VERSION, MASS_REQ_INTERVAL
from objects import User
from methods.friends import get as get_friends
from utils import get_user_friends


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


class FriendsPath:
    def __init__(self, access_key):
        self.access_key = access_key
        self.get_friends = lambda user_id: get_user_friends(self.access_key, user_id,
                                                            v=API_VERSION,
                                                            fields='can_access_closed')

    def get_path(self, user1, user2, depth=10):
        if type(user1) in [int, str]:
            user1 = User(id=user1)
        if type(user2) in [int, str]:
            user2 = User(id=user2)

        friends_graph = {}
        friend_filter = lambda user: can_access_closed(user) and not (user['id'] in friends_graph.keys())

        i = 1
        _friends = self.get_friends(user1['id'])
        last_result = {user1['id']: _friends}

        lr_user_list = []
        for lr_fl in last_result.values():
            lr_user_list += lr_fl

        user_ids = [str(user['id']) for user in lr_user_list if friend_filter(user)]

        friends_graph.update(last_result)

        while i <= depth or user2['id'] in last_result.values():
            i += 1
            last_result = {}
            for user_id in user_ids:
                _friends = self.get_friends(user_id)
                last_result.update({user_id: _friends})

                sleep(MASS_REQ_INTERVAL)

            lr_user_list = []
            for lr_fl in last_result.values():
                lr_user_list += lr_fl

            user_ids = [str(user['id']) for user in lr_user_list if friend_filter(user)]
            friends_graph.update(last_result)

        return friends_graph, user2['id'] in last_result.values()
