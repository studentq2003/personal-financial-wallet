from components.colors import default
def commands():
    print('Список доступных комманд:')
    print(default('\t--help'))
    print(default('\t--show'))
    print(default('\t--exit or /q'))
    print(default('\t--order'))
    print(default('\t--search'))
    print(default('\t--update'))
    print(default('\t--remove or -rm'))