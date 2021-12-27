from methods import vk_request


def get(params):
    return vk_request(method_name='friends.get', params=params)