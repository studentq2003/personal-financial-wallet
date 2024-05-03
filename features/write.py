import json
from variables import path, filename


def write(data):
    with open(path + filename, 'w') as f:
        json.dump(data, f)