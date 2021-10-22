class APIResponseError(Exception):
    def __init__(self, code, msg):
        print(f'You get the error code {code}. Message: {msg}')


class ReachedLimitError(APIResponseError):
    def __init__(self):
        print('You reached limits of VK for this token\'s account! Try to request later or change the token!')
