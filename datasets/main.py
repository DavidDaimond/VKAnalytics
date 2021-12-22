import pickle
from os.path import join
from objects import Message


class VKDataset:
    """
    parent class for all VKDatasets
    """
    def __init__(self, **data):
        self.data = data

    def save(self, path, name='dataset'):
        with open(join(path, name) + '.pkl', 'wb') as file:
            pickle.dump(self, file)


class ConversationDataset(VKDataset):
    def __init__(self, messages_list):
        self.messages = [Message(**message) for message in messages_list]
        self.data = messages_list

    def text_only(self):
        return [x['text'] for x in self.data if x['text']]

    def __getitem__(self, item):
        return self.messages.__getitem__(item)

    def __setitem__(self, item, value):
        self.messages.__setitem__(item, value)

    def __str__(self):
        return '\n\n'.join([x.__str__() for x in self.messages][:10])
