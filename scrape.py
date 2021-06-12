from os import stat
import requests
from bs4 import BeautifulSoup
import re
import time
import datetime
import sys


OUT_FILE = 'data.csv'

def dprint(*args,**nargs):
    print(*args,**nargs)
    nargs['file'] = None
    print(*args,**nargs)


def get_freie_plaetze():
    try:
        url = 'https://192.webclimber.de/de/trafficlight?callback=WebclimberTrafficlight.insertTrafficlight&key=nDhc9HyCw6XZzNe4QDpaSFg0QxmkfW43&hid=192&container=trafficlightContainer&type=2&area='

        req = requests.get(url)

        # print(r.status_code)

        bs_parse = BeautifulSoup(req.text, features="html.parser")

        status_text = bs_parse.find_all(class_='status_text')[0].contents[0]

        # freie Pl\u00e4tze 18
        plaetze = re.match('freie Pl\\\\u00e4tze (\\d*)', status_text).groups()[0]

        return int(plaetze)

    except Exception as e:
        dprint(str(e), file=sys.stderr)
        return None


dprint(f'Scraping at {str(datetime.datetime.now())}:', file=sys.stderr)

p = get_freie_plaetze()
if p is not None:
    o = f'{time.time()},{p}'
    # print(o)
    with open(OUT_FILE, 'a') as f:
        dprint(o, file=f)

