from features.show import show
from components.welcome import welcome
from components.help import help
from components.exit import exit
from components.order import order
from components.colors import default
from components.commands import commands
from features.add import add
from features.balance import balance
from features.rewrite_balance import rewrite_balance
from utils.zero_balance import zero_balance
from features.search import search
from components.search_input import search_input
from components.error_cmd import error_cmd
from utils.make_backup import make_backup
from utils.validate_json import validate_json
from variables import schema
from features.read import read
from utils.restore_backup import restore_backup


def main():
    welcome()
    zero_balance()

    # onload валидация основного файла money.json, если ошибки - восстановление из бекапа
    data = read()
    if validate_json(data, schema) is False:
        restore_backup()

    # листенер команд
    while True:
        cmd = input('\nВведите команду\n')

        if cmd == '--show':
            data = order()

            print(default(f'Текущий баланс: {balance()}\n'))
            show(data)

        elif cmd == '--add':
            add()

        elif cmd == '--balance' or cmd == '-b':
            print(default(f"Текущий баланс: {balance()}\n"))

        elif cmd == '-rb' or cmd == '--rbalance':
            rewrite_balance()

        elif cmd == '--search' or cmd == '-s':
            field, value = search_input()
            search(field, value)

        elif cmd == '--help' or cmd == '-h':
            help()

        elif cmd == '--commands':
            commands()

        elif cmd == '--exit' or cmd == '/q':
            exit()
            break

        elif cmd == '-mb' or cmd == 'mkdump':
            make_backup()

        else:
            error_cmd()


if __name__ == '__main__':
    main()
