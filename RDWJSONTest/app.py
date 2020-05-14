# TODO meerdere dictionaries tegelijk
# TODO Meer zoektermen (bouwjaar, dag en maand negeren, en hoe ik dat doe, via google of reygan maandag af)
# TODO zoektermen combineren (e.g. "volkswagen, 1999" of "bromfiets, cilinders: 1")
# TODO GUI

import json
import requests
import sys

exit = False

def search():
    print("Op wat wilt u zoeken?\nmerk | kenteken | exit")
    entry = input(">")
    if entry == "merk":
        print("Coming Soon.")

    elif entry == "kenteken":
        kenteken = input("kenteken:")
        api = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken="
        data = "".join([api, kenteken])
        kdata = requests.get(data).json()
        print(kdata)

    elif entry == "exit":
        exit = True
        sys.exit(0)

    else:
        print("Error.")

while exit is False:
    search()







