from time import sleep
from collections import Counter

from methods import friends_get, messages_get_history
from config import API_VERSION, MASS_REQ_INTERVAL, GET_HISTORY_MAX_COUNT
from objects import VKObject, User
from exceptions import APIResponseError


def is_vk_object(obj):
    return issubclass(type(obj), VKObject)


def load_all_dialog(params, interval=MASS_REQ_INTERVAL):
    data = messages_get_history(params)['response']
    params = Counter(params)
    params['count'] = GET_HISTORY_MAX_COUNT
    params['offset'] += len(data['items'])

    while len(data['items']) < data['count']:
        sleep(interval)
        resp = messages_get_history(params)['response']
        data['items'] += resp['items']
        params['offset'] += GET_HISTORY_MAX_COUNT
    return data


def get_user_friends(access_token, user_id, v=API_VERSION, import_all=True, interval=MASS_REQ_INTERVAL, **parameters):
    if type(user_id) == User:
        user_id = user_id['id']
    params = dict(access_token=access_token, user_id=user_id, v=v)
    params.update(parameters)
    try:
        data = friends_get(params)
    except APIResponseError as ex:
        return []

    if import_all:
        count = data['response']['count']
        offset = params['offset'] if params.get('offset') else 0

        while offset + len(data['response']['items']) < count:
            offset = offset + len(data['response']['items'])
            params['offset'] = offset

            data['response']['items'] += friends_get(params)['response']['items']

            sleep(interval)

    return [User(**d) for d in data['response']['items']]


def get_mutual_dict(access_token, fl, v=API_VERSION, interval=MASS_REQ_INTERVAL, **parameters):
    md = {}
    params = dict(access_token=access_token, v=v)
    params.update(parameters)
    for person in fl:
        md[person['id']] = get_user_friends(access_token=access_token, user_id=person, interval=interval,
                                            **parameters)
        sleep(interval)

    return md

