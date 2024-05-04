from features.show import show
from components.welcome import welcome
from features.read import read
from components.help import help
from components.exit import exit
from components.order import order
from components.errortext import red
from components.bluetext import blue
from components.commands import commands
from features.add import add
from features.balance import balance
from features.rewrite_balance import rewrite_balance


def main():
    welcome()

    while True:
        cmd = input('\nВведите команду\n')

        if cmd == '--show':
            data = read()
            show(data)

        elif cmd == '--order':
            order()

        elif cmd == '--add':
            add()

        elif cmd == '--balance' or cmd == '-b':
            balance()

        elif cmd == '-rb' or cmd == '--rbalance':
            rewrite_balance()

        elif cmd == '--help' or cmd == '-h':
            help()

        elif cmd == '--commands':
            commands()

        elif cmd == '--exit' or cmd == '/q':
            exit()
            break

        else:
            print(red("Такой команды нет. Введите -h или --help для просмотра помощи"))
            print(blue('Также вы можете просмотреть доступные команды, введя --commands'))


if __name__ == '__main__':
    main()
