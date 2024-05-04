from features.read import read, read_balance
from classes import Data, Balance


def balance():
    global b
    data = read_balance()
    b = Balance(data)

    data = read()

    for string in data:
        s = Data(string)
        if s.category == '-':
            b.value -= int(s.value)
        elif s.category == '+':
            b.value += int(s.value)

    print("Текущий баланс: ", b.value)