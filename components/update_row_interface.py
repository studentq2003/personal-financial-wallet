from datetime import date

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
            pass


def input_date():
    print(default(
        "\nВведите новую дату операции"
    ))
    while True:
        try:
            return input()
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

    while True:
        try:
            target_id = int(input())
        except Exception:
            pass
        if target_id > 0:
            break
        else:
            print(error("Введите корректный ID. Чтобы найти ID операций, введите --show"))

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
                return target_id, field, value
            elif field == 2:
                field = 'date'
                value = input_date()
                return target_id, field, value
            elif field == 3:
                field = 'description'
                value = input_description()
                return target_id, field, value
            else:
                print(error(
                    "Выберите корректную опцию"
                ))
        except Exception:
            pass
