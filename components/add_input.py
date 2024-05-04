from datetime import datetime
from utils.date_time_exceptor import check_date, check_time
from components.category_selector import category_selector
from utils.integer_exceptor import integer_exceptor
from components.colors import error, default
from utils.id_generator import id_generator
from classes import Data
from features.read import read


def add_input():
    print("Добавление строки\n"
          "Для добавления строки введите данные\n"
          )

    category = category_selector()

    print(default("Введите сумму операции\n"))

    value = integer_exceptor(
        error(
            "Введите корректную сумму операции"
        ))

    print('Выберите дату и время операции\n'
          'Установить текущую дату и время? [Y/n]?')
    date_and_time = input()
    if date_and_time != '' and date_and_time.upper() != 'Y':
        cur_date = datetime.now().strftime("%d-%m-%Y")
        cur_time = datetime.now().strftime("%H:%M")

        print(f"Введите дату операции в формате {cur_date}")
        while True:
            try:
                inp_date = input()
                inp_date = datetime.strptime(inp_date, '%d-%m-%Y')
                date = inp_date.strftime("%d-%m-%Y")
                if not check_date(date):
                    continue
                break
            except Exception as e:
                print(error(f"Введите корректную дату вида {cur_date}"))

        print(error(f"Введите время в формате {cur_time}"))
        while True:
            try:
                time = input()
                if not check_time(date, time):
                    continue
                break
            except Exception as e:
                print(error(f"Введите корректное время вида {cur_time}, error: {e}"))

    else:
        date = datetime.now().strftime("%d-%m-%Y")
        time = datetime.now().strftime("%H:%M")

    print(default(
        "Введите описание операции до 30 символов, либо оставьте поле пустым:"
    ))

    while True:
        description = input()
        if len(description) > 30:
            print(error("Введите описание не более 30 символов"))
        else:
            break

    data = read()
    while True:
        id = id_generator()

        for i in data:
            string = Data(i)
            if string.id == id:
                continue
        break

    return {
        "id": id,
        "type": category,
        "value": value,
        "date": date,
        "time": time,
        "description": description
    }
