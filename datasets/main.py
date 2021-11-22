class VKDataset:
    """
    parent class for all VKDatasets
    """
    def __init__(self):
        self.data = None

    def get_data(self, *args):
        # get data from *args and put it into self.data for next operations
        self.data = list(*args)

    def process_data(self, **params):
        pass


class UsersDataset(VKDataset):
    """
    class for parsing person data and structure it into datasets
    """
