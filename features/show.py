from classes import Data
from components.showmemore import showmemore


def show(data):
    print('\nСтатистика последних операций')

    k = 0
    print('{:<5} {:<10} {:<10} {:<20} {:<20} {:<30}'.format(
        '№', 'Категория', 'Сумма', 'Дата', 'Время', 'Описание'
    ))
    for i in data:
        try:
            string = Data(i)
        except Exception as e:
            print(f'Error: {e}')

        if string.category == '-':
            category = 'Расход'
        else:
            category = 'Доход '
        print(f'{k + 1:<5}'
              f'{category:<10}'
              f'{string.value:<10}'
              f'{string.date:<20}'
              f'{string.time:<20}'
              f'{string.description:<30}')
        k += 1
        if k == 10 and len(data) > 10:
            if showmemore() is False:
                break
