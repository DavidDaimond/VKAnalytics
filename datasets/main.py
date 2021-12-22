import pickle
from os.path import join


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
    pass
