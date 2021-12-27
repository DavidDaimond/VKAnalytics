from methods import vk_request


def get_history(params):
    return vk_request(method_name='messages.getHistory', params=params)