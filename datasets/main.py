class VKDataset:
    """
    parent class for all VKDatasets
    """
    def __init__(self):
        self.data = None

    def create(self, *args):
        pass

    def process_data(self, **params):
        pass


class UsersDataset(VKDataset):
    """
    class for parsing person data and structure it into datasets
    """
