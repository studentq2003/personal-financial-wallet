from components.colors import default, purple


def welcome():
    print("\n")
    print(default("Добро пожаловать в Личный финансовый кошелёк!"))

    print(
        "Для работы с приложением Вам нужно вводить в консоль команды\n"
        "Если вы не знаете команды приложения, введите -h, --help или --commands\n"
        "Перед использованием программы рекомендуется изучить руководство в pdf файле в репозитории\n"
    )
    print(
        purple(
            "Автор ПО - Никулин А. А.\t"
            "t.me/animal_q\t"
            "github.com/studentq2003\n"
        ))

