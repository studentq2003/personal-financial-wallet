from features.read import read, read_balance
from classes import Data, Balance
from components.balance_updater import balance_update


def balance():
    global b
    data = read_balance()
    for i in data:
        b = Balance(i)

    v = balance_update(b)

    return v
