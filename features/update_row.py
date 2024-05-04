from features.read import read
from classes import Data


def update_row():
    data = read()

    return data

    # for i in data:
    #     string = Data(i)


print(update_row())
