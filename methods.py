import requests

from config import *
from exceptions import *


def bad_response_handler(req_func):
    def req_with_handler(**kwargs):
        response = req_func(**kwargs)
        if 'response' not in response:
            if response['error']['error_code'] == 29:
                raise ReachedLimitError()
            else:
                raise APIResponseError(response['error']['error_code'], response['error']['error_msg'])

        return response
    return req_with_handler


@bad_response_handler
def vk_request(method_name, params):
    api_url = 'http://api.vk.com/method/'
    req = requests.get(api_url + method_name,
                       params=params)

    response = req.json()

    return response


# The name of functions is similar to VK API methods, but translated from CamelCase to snake_case


def users_get(params):
    return vk_request(method_name='users.get', params=params)


def friends_get(params):
    return vk_request(method_name='friends.get', params=params)


def users_get_subscriptions(params):
    return vk_request(method_name='users.getSubscriptions', params=params)


def users_get_followers(params):
    return vk_request(method_name='users.getFollowers', params=params)


def messages_get_history(params):
    return vk_request(method_name='messages.getHistory', params=params)