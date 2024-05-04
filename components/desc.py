def desc():
    print('\nСортировать по убыванию? [Y/n]?')
    inp = input('\n')
    if inp.upper() == 'Y' or inp == '':
        return True
    else:
        return False
