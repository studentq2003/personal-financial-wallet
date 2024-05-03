from classes import Data
from features.read import read


def show(data):
    # try:
    #     data = read()
    # except FileNotFoundError:
    #     print("File not found")

    print('\nСтатистика последних операций')

    k = 0
    for i in data:
        try:
            string = Data(i)
        except Exception as e:
            print(f'Error: {e}')

        if string.category == '-':
            category = 'Расход'
        else:
            category = 'Доход '
        print(f'[{k}]: '
              f'{category}\t'
              f'{string.value}\t'
              f'{string.date}\t'
              f'{string.time}\t'
              f'{string.description}')
        k += 1
        if k == 10:
            print('\nПоказаны 10 послених записей, показать все?[Y/n]?')
            inp = input()
            if inp.upper() != 'Y' and inp != '':
                break
