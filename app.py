import json
from variables import Stats


def read_file():
    with open(path + filename, "r") as f:
        data = json.load(f)
        for i in data:
            out = Stats(i["type"], i["value"], i["date"])
            print(f'{out.type}\t{out.value}\t{out.date}')


path = './'
filename = 'money.json'
