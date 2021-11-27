class VKObject:
    """
    Parent class for other VK objects. This class contain main structure of every Object classes.
    Objects is class-family, which encapsulate behavior of VK data structures
    """
    def __init__(self, **data):
        self.data = data

    def add_data(self, data):
        self.data = self.data | data

    def __getitem__(self, item):
        if not (type(item) is str):
            raise TypeError(f'The key is always must be string, not {type(item)}')

        return self.data.__getitem__(item)

    def __setitem__(self, item, value):
        if not (type(item) is str):
            raise TypeError(f'The key is always must be string, not {type(item)}')

        self.data.__setitem__(item, value)


class Person(VKObject):
    def __init__(self, **data):
        super(Person, self).__init__(**data)

    def add_friends(self, friends: list):
        """

        :param friends: list of friends in VKAPI-style. It
        :return:
        """
        self.data['friends'] += friends


class Post(VKObject):
    def __init__(self, **data):
        super(Post, self).__init__(**data)

