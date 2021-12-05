from objects.main import *
from config import *

from time import sleep


def get_mutualsdict(fl, interval=MASS_REQ_INTERVAL):
    md = {}
    for person in fl:
        person.parse_friends()
        md[person.id] = person.data['friends']['items']
        sleep(interval)
    return md

