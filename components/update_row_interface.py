from datetime import datetime
from classes import Data

from features.show import show
from features.read import read

from utils.date_time_exceptor import check_date

from components.colors import default, purple, error


def input_value():
    print(default(
        "\nВведите новую сумму операции"
    ))
    while True:
        try:
            value = int(input())
            if value >= 0:
                return value
            else:
                print(error(
                    "Введите корректную сумму операции"
                ))
        except Exception:
            print(error(
                "Введите корректную сумму операции"
            ))
            pass


def input_date():
    print(default(
        "\nВведите новую дату операции"
    ))
    while True:
        try:
            cur_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Введите дату операции в формате {cur_date}")
            while True:
                try:
                    inp_date = input()
                    inp_date = datetime.strptime(inp_date, '%d-%m-%Y')
                    date = inp_date.strftime("%d-%m-%Y")
                    if not check_date(date):
                        continue
                    return date
                except Exception as e:
                    print(error(f"Введите корректную дату вида {cur_date}"))
        except Exception:
            pass


def input_description():
    print(default(
        "\nВведите новое описание операции"
    ))
    while True:
        try:
            return input()
        except Exception:
            pass


def update_row_interface():
    global target_id
    print(purple("\nИзменение записи\n"))
    print(default("Введите id операции для изменения\n"))

    x = True
    k = 0
    while x == True:
        try:
            if k > 0:
                print(error("Введите корректный ID. Чтобы найти ID операций, введите --show"))
            k += 1
            target_id = input()
            data = read()
            if target_id == '--show':
                show(data)
            for i in data:
                string = Data(i)
                if string.id == int(target_id):
                    x = False
                    break
                else:
                    continue
        except Exception:
            print(error("Нельзя использовать буквы и символы, доступны только цифры"))

    print(default("Выберите поле для изменить"))
    while True:
        print("\t[1] - изменить сумму\n"
              "\t[2] - изменить дату\n"
              "\t[3] - изменить описание"
              )
        try:
            field = int(input())
            if field == 1:
                field = 'value'
                value = input_value()
                return int(target_id), field, value
            elif field == 2:
                field = 'date'
                value = input_date()
                return int(target_id), field, value
            elif field == 3:
                field = 'description'
                value = input_description()
                return int(target_id), field, value
            else:
                print(error(
                    "Выберите корректную опцию"
                ))
        except Exception:
            pass
