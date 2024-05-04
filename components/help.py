from components.colors import default


def help():
    print('\n'
          'Добро пожаловать в краткое руководство по программе '
          '"Личный финансовый кошелёк"\n'
          'Более подробное описание функционала находится в pdf файле в репозитории\n'
          'Доступные команды:\n'
          )
    print(default('\t--show'))
    print(
        '\t\t>>\t[показать последние 10 операций]\n'
        '\t\tВам будет предложено показать полный список.\n'
        '\t\tДля вывода полного списка нажмите Enter, либо введите "Y" или "y"\n'
        '\t\tЧтобы не выводить полный список операций, введите "n"\n'
        '\n'
    )
    print(default('\t-b\t\t--balance'))
    print(
        '\t\t>>\tВывести текущий баланс\n'
        '\n'
    )

    print(default('\t-rb\t\t--rbalance'))
    print(
        '\t\t>>\tИзменить баланс\n'
        '\n'
    )

    print(default('\t-s\t\t--search'))
    print(
        '\t\t>>\tПоиск записи по полю\n'
        '\n'
    )

    print(default('\t-u\t\t--update'))
    print(
        '\t\t>>\tОбновление поля записи\n'
        '\n'
    )

    print(default('\t--add'))
    print(
        '\t\t>>\tДобавлаение записи\n'
        '\n'
    )
    print(default('\t-mb\t\t--mkbackup'))
    print(
        '\t\t>>\tЗаписать пользовательский бекап\n'
        '\n'
    )

    print(default('\t-r\t\t--restore'))
    print(
        '\t\t>>\tВосстановить пользовательский бекап\n'
        '\n'
    )

    print(default('\t--exit\t\t/q'))
    print(
        '\t\t>>\tЗавершить работу программы\n'
        '\n'
    )