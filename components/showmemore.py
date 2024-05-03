def showmemore():
    print('\nПоказаны 10 послених записей, показать все?[Y/n]?')
    inp = input()
    if inp.upper() != 'Y' and inp != '':
        return False
