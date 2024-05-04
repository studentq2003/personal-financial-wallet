from features.read import read_balance
from components.balance_updater import balance_update
from features.write import write_balance
from classes import Balance


def zero_balance():
    global bl
    data = read_balance()
    for i in data:
        bl = Balance(i)
    if int(bl.value) == -1:
        bl.value = balance_update(bl)

    data.append([{"balance": bl.value}])

    write_balance(data[-1])
