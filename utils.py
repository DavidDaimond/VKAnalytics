from time import sleep

from methods import friends_get
from config import VERSION, MASS_REQ_INTERVAL
from objects import Person


def get_user_friends(access_token, user_id, v=VERSION, import_all=True, **parameters):
    params = dict(access_token=access_token, user_id=user_id, v=v)
    params.update(parameters)

    data = friends_get(params)

    if import_all:
        count = data['response']['count']
        offset = params['offset'] if params.get('offset') else 0

        while offset + len(data['response']['items']) < count:
            offset = offset + len(data['response']['items'])
            params['offset'] = offset

            data['response']['items'] += friends_get(params)['response']['items']

            sleep(MASS_REQ_INTERVAL)

    return [Person(d) for d in data]
