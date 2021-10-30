import requests

from config import *
from exceptions import *


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

    def parse_data(self, fields=None, friends=False):
        """

        :param
        fields: string with fields, separated by commas
        friends: need to parse friends of user. By default, it only parse data about friends id
        :return:
        """

        params = {
                   'v': VERSION,
                   'access_token': self.token,
                   'user_id': self.id,
        }

        if not (fields is None):
            params['fields'] = fields

        req = requests.get("http://api.vk.com/method/users.get",
                           params=params)

        response = req.json()

        if 'response' not in response:
            if response['error']['error_code'] == 29:
                raise ReachedLimitError()
            else:
                raise APIResponseError(response['error']['error_code'], response['error']['error_msg'])

        self.data.update(response['response'][0])
        print('Data was successfully updated')

        if friends:
            self.parse_friends()

    def parse_friends(self, fields=None):

        params = {
                   'v': VERSION,
                   'access_token': self.token,
                   'user_id': self.id,
        }

        if not (fields is None):
            params['fields'] = fields

        req = requests.get("http://api.vk.com/method/friends.get",
                           params=params)

        response = req.json()

        if 'response' not in response:
            if response['error']['error_code'] == 29:
                raise ReachedLimitError()
            else:
                raise APIResponseError(response['error']['error_code'], response['error']['error_msg'])

        self.data['friends'] = response['response']
        print('Friends was successfully parsed')

    def get_data(self):
        return self.data.copy()
