import requests

from config import *


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

    def parse_data(self, fields=None):
        """

        :param fields: string with fields, separated by commas
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

    def get_data(self):
        return self.data.copy()
