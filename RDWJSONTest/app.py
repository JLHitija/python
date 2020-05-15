# TODO meerdere dictionaries tegelijk
# TODO Meer zoektermen (bouwjaar, dag en maand negeren, en hoe ik dat doe, via google of reygan maandag af)
# TODO zoektermen combineren (e.g. "volkswagen, 1999" of "bromfiets, cilinders: 1")
# TODO GUI

import json
import requests
import sys
import pprint

exit = False
pp = pprint.PrettyPrinter(indent=4)

def search():
    print("Op wat wilt u zoeken?\nmodel | kenteken | bouwjaar | exit")
    entry = input(">")
    if entry == "model":
        merk = input("model(TYPE IN CAPS):")
        api = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?handelsbenaming="
        data = "".join([api, merk])
        data2 = requests.get(data).json()
        pp.pprint(data2)

    elif entry == "kenteken":
        kenteken = input("kenteken(TYPE IN CAPS:")
        api = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken="
        data = "".join([api, kenteken])
        data2 = requests.get(data).json()
        pp.pprint(data2)

    elif entry == "bouwjaar":
        jaar = input("bouwjaar:")
        api = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?datum_eerste_toelating="
        #hier een loop
        datum = jaar + "alle data in het jaar waar het om gaat. Dit moet waarschijnlijk ook" \
                       "in een loop."
        data = "".join([api, datum])


    elif entry == "exit":
        exit = True
        sys.exit(0)

    else:
        print("Error. Try again.")

while exit is False:
    search()







