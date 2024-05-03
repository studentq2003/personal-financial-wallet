from features.show import show
from features.order import order_date, order_value
from features.welcome import welcome
from features.read import read
from features.help import help
from components.sortby import sort_by
from components.exit import exit


def main():
    global ordered_data
    welcome()

    while True:
        cmd = input('\nВведите команду\n')

        if cmd == '--show':
            data = read()
            show(data)

        elif cmd == '--order':
            data = read()
            print('\nПо какому полю сортировать?'
                  '\n[1] По дате и времени'
                  '\n[2] По сумме')
            inp = input('\n')
            if inp == '1':
                state = sort_by()
                ordered_data = order_date(data, state)
            elif inp == '2':
                state = sort_by()
                ordered_data = order_value(data, state)
            else:
                print('\nНекорректный ввод, введите номер пункта')
            show(ordered_data)

        elif cmd == '--help' or cmd == '-h' or cmd == '--commands':
            help()

        elif cmd == '--exit':
            exit()
            break


if __name__ == '__main__':
    main()
