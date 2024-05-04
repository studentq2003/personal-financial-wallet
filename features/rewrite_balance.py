from classes import Balance
from features.read import read_balance
from features.write import write_balance


def rewrite_balance():
    global rb
    try:
        data = read_balance()
        for i in data:
            rb = Balance(i)
    except Exception as e:
        print(e)

    print("Введите новую сумму для обновления баланса\n"
          f"Текущий баланс: {rb.value}")

    while True:
        try:
            b.value = int(input())
        except Exception as e:
            print("Некорректный ввод: ", e)
        break

    new_b = {"balance": rb.value}

    write_balance(new_b)
