from objects.main import *
from config import *

from time import sleep


def get_friendslist(person, prepared=False):
    if not prepared:
        person.parse_friends()

    if type(person.data['friends']['items'][0]) is int:
        fl = [Person(person.token, friend) for friend in person.data['friends']['items']]
    else:
        fl = [Person(person.token, friend['id'], friend) for friend in person.data['friends']['items']]

    return fl


def get_mutualsdict(fl, interval=MASS_REQ_INTERVAL):
    md = {}
    for person in fl:
        person.parse_friends()
        md[person.id] = person.data['friends']['items']
        sleep(interval)
    return md

