import requests

from config import *
from exceptions import *

from time import sleep


def error_handler(req_func):
    def req_with_handler(**kwargs):
        response = req_func(**kwargs)

        if 'response' not in response:
            if response['error']['error_code'] == 29:
                raise ReachedLimitError()
            else:
                raise APIResponseError(response['error']['error_code'], response['error']['error_msg'])

        return response
    return req_with_handler


@error_handler
def vk_request(method_name, params):
    api_url = 'http://api.vk.com/method/'
    req = requests.get(api_url + method_name,
                       params=params)

    response = req.json()

    return response


def users_get(params):
    return vk_request(method_name='users.get', params=params)


def friends_get(params):
    return vk_request(method_name='friends.get', params=params)