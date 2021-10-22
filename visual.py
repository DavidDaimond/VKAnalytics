class VKVisual:
    """
    parent class for all other Visual classes. Visual classes uses for visualize data.
    All of Visual classes have get_data and show_data method, even if this methods not using
    """
    def __init__(self):
        self.data = None

    def get_data(self, *args):
        # get data from *args and put it into self.data for next operations
        self.data = list(*args)

    def show_data(self, **params):
        # show data from self.data with parameters **params
        print(**params)
        print(self.data)
