from datetime import datetime
from utils.date_time_exceptor import check_date
from components.colors import error, default


def search_input():
    print(
        default(
            "Введите номер категории, по которой искать операцию"
        ))
    while True:
        print("\t[1] - Доходы\n"
              "\t[2] - Расход\n"
              "\t[3] - Сумма\n"
              "\t[4] - Дата\n"
              "\t[5] - Описание\n"
              "\t[6] - ID"
              )
        print(default(
            "\t[0] - Выйти в главное меню\n"
        ))

        field = int(input('\n'))

        if field == 1:
            return 'type', '+'

        elif field == 2:
            return 'type', '-'

        elif field == 3:
            print(default("Введите сумму"))
            try:
                value = int(input('\n'))
                if 0 < value < 10000000000:
                    return 'value', value
                else:
                    print(error(
                        "Сумма введена некорректно"
                    ))
            except Exception:
                print(error(
                    "Сумма введена некорректно"
                ))

        elif field == 4:
            print(
                default(
                    f"Введите дату в формате {datetime.now().date()}"
                ))
            value = input('\n')
            try:
                if check_date(value):
                    return 'date', value
                else:
                    print(error(
                        "Дата введена неправильно"
                    ))
            except Exception:
                print(error(
                    "Дата введена неправильно"
                ))

        elif field == 5:
            print(default(
                "Введите описание"
            ))
            value = input('\n')
            return 'description', value

        elif field == 6:
            print(default(
                "Введите ID операции"
            ))
            try:
                value = int(input('\n'))
                if value > 0:
                    return 'id', value
                else:
                    print(error(
                        "ID введен некорректно"
                    ))
            except Exception:
                print(error(
                    "ID введен некорректно"
                ))

        elif field == 0:
            break

        print("Категория выбрана неправильно. Введите номер от 1 до 5")
