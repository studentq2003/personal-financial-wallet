import json
from variables import path, filename


def read():
    with open(path + filename, "r") as f:
        return json.load(f)
