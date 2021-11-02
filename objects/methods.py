from objects.main import *


def get_friendslist(person, prepared=False):
    if not prepared:
        person.parse_friends()

    if type(person.data['friends']['items'][0]) is int:
        fl = [Person(person.token, friend) for friend in person.data['friends']['items']]
    else:
        fl = [Person(person.token, friend['id'], friend) for friend in person.data['friends']['items']]

    return fl
