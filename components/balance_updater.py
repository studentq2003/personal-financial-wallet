from classes import Data
from features.read import read


def balance_update(b):
    data = read()

    # print(data, b.value)
    for string in data:
        s = Data(string)
        if s.category == '-':
            b.value -= int(s.value)
        elif s.category == '+':
            b.value += int(s.value)
    return b.value
