from classes import Data
from components.showmemore import showmemore


def show(data):
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
            if showmemore() is False:
                break
