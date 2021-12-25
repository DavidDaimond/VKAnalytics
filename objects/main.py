def parse_attachments(attlist):
    _attlist = list(attlist)
    for attachment in _attlist:
        attachment_type = attachment['type']
        if attachment_type in OBJECT_NAMES.keys():
            attachment[attachment_type] = OBJECT_NAMES[attachment_type](**attachment[attachment_type])
    return _attlist


class VKObject:
    """
    Parent class for other VK objects. This class contain main structure of every Object classes.
    Objects is class-family, which encapsulate behavior of VK data structures
    """
    def __init__(self, **data):
        self.data = data

    def add_data(self, data):
        self.data.update(data)

    def __getitem__(self, item):
        if not (type(item) is str):
            raise TypeError(f'The key is always must be string, not {type(item)}')

        return self.data.__getitem__(item)

    def __setitem__(self, item, value):
        if not (type(item) is str):
            raise TypeError(f'The key is always must be string, not {type(item)}')

        self.data.__setitem__(item, value)


class User(VKObject):
    def __init__(self, **data):
        super(User, self).__init__(**data)

    def add_friends(self, friends: list):
        """

        :param friends: list of friends in VKAPI-style. It
        :return:
        """
        self.data['friends'] += friends


class Post(VKObject):
    def __init__(self, **data):
        super(Post, self).__init__(**data)

    def __str__(self):
        return self['text'] if self['text'] else ''


class Message(VKObject):
    def __init__(self, **data):
        super(Message, self).__init__(**data)
        self.attachments = self.data.get('attachments')

    def convert_attachments(self):
        if self.data['attachments']:
            self.attachments = parse_attachments(self.data['attachments'])

    def __str__(self):
        if self['text']:
            return str(self['text'])
        elif self['attachments']:
            repr_obj = OBJECT_NAMES.get(self['attachments'][0]['type'])

            return str(repr_obj)


class Conversation(VKObject):
    def __init__(self, **data):
        super(Conversation, self).__init__(**data)
        self.data['id'] = self.data['peer']['id']


OBJECT_NAMES = {
    'user': User,
    'wall': Post,
    'post': Post,
    'message': Message
}
