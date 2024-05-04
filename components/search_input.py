from datetime import datetime


def search_input():
    print("Введите номер категории, по которой искать операцию")
    while True:
        print("\t[1] - Доходы\n"
              "\t[2] - Расход\n"
              "\t[3] - Сумма\n"
              "\t[4] - Дата\n"
              "\t[5] - Описание\n")
        field = int(input('\n'))
        if field == 1:
            return 'type', '+'
        elif field == 2:
            return 'type', '-'
        elif field == 3:
            print("Введите сумму")
            value = int(input('\n'))
            return 'value', value
        elif field == 4:
            print(f"Введите дату в формате {datetime.now().date()}")
            value = input('\n')
            return 'date', value
        elif field == 5:
            print("Введите описание")
            value = input('\n')
            return 'description', value
        print("Категория выбрана неправильно. Введите номер от 1 до 5")
