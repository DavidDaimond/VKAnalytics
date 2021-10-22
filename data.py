import requests


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

    def __init__(self, token, person_id):
        super(Person, self).__init__(token)
        self.id = person_id
        self.data = {}

    def parse_data(self, fields=None):
        """

        :param fields: string with fields, separated by commas
        :return:
        """
        pass
