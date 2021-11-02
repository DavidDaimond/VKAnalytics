class APIResponseError(Exception):
    def __init__(self, code, msg):
        print(f'You get the error code {code}. Message: {msg}')


class ReachedLimitError(APIResponseError):
    def __init__(self):
        print('You reached limits of VK for this token\'s account! Try to request later or change the token!')


class NoDataError(Exception):
    def __init__(self):
        print('self.data is None! You must declare data using .get_data() method or declare directly!')


class NoMethodError(Exception):
    def __init__(self):
        print('self.method is None! You must declare method using .change_method() function or declare directly!')
