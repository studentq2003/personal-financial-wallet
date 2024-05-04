from classes import Balance
from features.read import read_balance
from features.write import write_balance
from features.balance import balance
from components.balance_updater import balance_update
from utils.integer_exceptor import integer_exceptor


def rewrite_balance():
    current_balance = balance()

    print("Введите новую сумму для обновления баланса\n"
          f"Текущий баланс: {current_balance}")

    inp = integer_exceptor("Введите корректный баланс. Он должен быть целочисленным и не содержать другие символы")

    new_balance = {"balance": inp}
    bl = Balance(new_balance)
    tmp = bl.value

    v = balance_update(bl)

    delta = tmp - v
    u = tmp + delta

    data = read_balance()
    data.append([{"balance": u}])

    write_balance(data[-1])
