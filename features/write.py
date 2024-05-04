import json
from variables import path, datafile, balancefile


def write(data):
    with open(path + datafile, 'w') as f:
        json.dump(data, f)


def write_balance(data):
    with open(path + balancefile, 'w') as f:
        json.dump(data, f)
