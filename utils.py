from time import sleep

from methods import friends_get
from config import VERSION, MASS_REQ_INTERVAL
from objects import User
from exceptions import APIResponseError


def get_user_friends(access_token, user_id, v=VERSION, import_all=True, interval=MASS_REQ_INTERVAL, **parameters):
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


def get_mutual_dict(access_token, fl, v=VERSION, interval=MASS_REQ_INTERVAL, **parameters):
    md = {}
    params = dict(access_token=access_token, v=v)
    params.update(parameters)
    for person in fl:
        md[person['id']] = get_user_friends(access_token=access_token, user_id=person, interval=interval,
                                            **parameters)

        sleep(interval)

    return md
