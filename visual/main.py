from objects.main import Person
from exceptions import NoMethodError, NoDataError


class VKVisual:
    """
    parent class for all other Visual classes. Visual classes uses for visualize data.
    All of Visual classes have get_data and show_data method, even if this methods not using
    self.method - the way, which data will be prepared to visualise
    """
    def __init__(self):
        self.data = None
        self.method = None

    def get_data(self, *args):
        # get data from *args and put it into self.data for next operations
        self.data = list(*args)

    def show_data(self, **params):
        # show data from self.data with parameters **params
        print(**params)
        print(self.data)

    def change_method(self, method):
        self.method = method


class FriendsField(VKVisual):
    def __init__(self, **kwargs):
        """
        :param kwargs:
        """
        super(FriendsField, self).__init__()

        if len(kwargs.keys()):
            self.data = kwargs.get('data')
            self.method = kwargs.get('method')

    def show_data(self, **kwargs):
        if self.data is None:
            raise NoDataError()
        if self.method is None:
            raise NoMethodError()

        self.method(self.data, **kwargs)
