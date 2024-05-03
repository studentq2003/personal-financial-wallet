from features.show import show
from features.order import order
from features.welcome import welcome
from features.read import read


def main():
    welcome()

    while True:
        cmd = input('\nВведите команду\n')

        if cmd == '--show':
            data = read()
            show(data)

        elif cmd == '--order':
            data = read()
            ordered_data = order(data)
            show(ordered_data)

        elif cmd == '--exit':
            break

    print('Работа программы завершена! Спасибо за использование!')


if __name__ == '__main__':
    main()
