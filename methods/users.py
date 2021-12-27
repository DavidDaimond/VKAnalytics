from methods import vk_request


def get(params):
    return vk_request(method_name='users.get', params=params)


def get_subscriptions(params):
    return vk_request(method_name='users.getSubscriptions', params=params)


def get_followers(params):
    return vk_request(method_name='users.getFollowers', params=params)