# TODO meerdere dictionaries tegelijk
# TODO Meer zoektermen
# TODO zoektermen combineren (e.g. "volkswagen, 1999" of "bromfiets, cilinders: 1")
# TODO GUI

import json
import requests
import sys

# haal data op
response = requests.get("https://opendata.rdw.nl/resource/m9d7-ebf2.json")
data = response.json()

exit = False

### Het lukte nog niet om uit elke dictionary info te halen maar ik wou er zelf achterkomen. Het duurde uberhaupt al lang
### om search() werkend te krijgen dus als ik het morgen nog niet weet ga ik het wel vragen omdat het anders wel zonde
### van de tijd is.

def search():
    print("merk | kenteken | exit")
    entry = input(">")
    if entry == "merk":
        for x in data:
            print(data[0]['merk'])

    elif entry == "kenteken":
        for x in data:
            print(data[0]['kenteken'])
    elif entry == "exit":
        exit = True
        sys.exit(0)

    else:
        print("Error.")

while exit is False:
    search()







