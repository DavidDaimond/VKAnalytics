import requests

from config import *
from exceptions import *
from objects.methods import *


class VKData:
    """
    Parent class for other VK objects. This class contain main structure of every Object classes.
    Methods parse_data and give_data must be declared even if they not using
    """
    def __init__(self, token):
        self.token = token

    def parse_data(self):
        """
        Method parse_data using for parse data (if it wasn't passed from __init__ or need more data).
        """
        pass

    def give_data(self):
        pass


class Person(VKData):

    def __init__(self, token, person_id, data=None):
        super(Person, self).__init__(token)
        self.id = person_id
        self.data = {} if data is None else data
        self.base_params = {
                   'v': VERSION,
                   'access_token': self.token
        }

    def parse_data(self, fields=None, user_data=True, friends=False, subs=False):
        """

        :param
        fields: string with fields, separated by commas
        friends: need to parse friends of user. By default, it only parse data about friends id
        :return:
        """

        params = self.base_params.copy()
        params['user_id'] = self.id

        if not (fields is None):
            params['fields'] = fields

        if user_data:
            response = users_get(params)

            self.data.update(response['response'][0])
            print('Data was successfully parsed')

        if friends:
            response = friends_get(params)

            self.data['friends'] = response['response']
            print('Friends was successfully parsed')

        if subs:
            response = users_get_subscriptions(params)

            self.data['subs'] = response['response']
            print('Subs was successfully parsed')

    def get_data(self):
        return self.data.copy()


# class Friend(Person):
#     def __init__(self, token, person_id, main_friend, data=None):
#         super(Friend, self).__init__(token, person_id, data)
#         self.friend = main_friend
#
#
# class FriendsList(VKData):
#
#     def __init__(self, token, id_list: list):
#         super(FriendsList, self).__init__(token)
#         self.id_list = list
