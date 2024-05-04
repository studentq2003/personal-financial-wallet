import json
from variables import path, datafile, balancefile


def read():
    with open(path + datafile, "r") as f:
        return json.load(f)


def read_balance():
    with open(path + balancefile, "r") as f:
        return json.load(f)
