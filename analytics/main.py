class VKAnalytic:
    """
    parent class for all other Analytics classes.
    Analytics classes uses for analyzing data and then show it as graphs, plots and others
    It is something between Visual and Data classes. Analytics can parse/process data, show data and more
    But unlike Visual classes, which more oriented to show data, this class-family more commonly used for
    creating datasets, collecting and analysing data
    """
    def __init__(self):
        self.data = None

    def get_data(self, *args):
        # get data from *args and put it into self.data for next operations
        self.data = list(*args)

    def process_data(self, **params):
        pass

    def show_data(self, **params):
        # show data from self.data with parameters **params
        print(**params)
        print(self.data)

