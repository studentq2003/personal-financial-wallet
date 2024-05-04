from components.colors import error, default

def error_cmd():
    print(error("Такой команды нет. Введите -h или --help для просмотра помощи"))
    print(default('Также вы можете просмотреть доступные команды, введя --commands'))