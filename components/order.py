from features.read import read
from features.order import order_date, order_value
from features.show import show
from components.desc import desc

def order():
    global ordered_data
    data = read()
    print('\nПо какому полю сортировать?'
          '\n[1] По дате и времени'
          '\n[2] По сумме')
    inp = input('\n')
    if inp == '1':
        state = desc()
        ordered_data = order_date(data, state)
    elif inp == '2':
        state = desc()
        ordered_data = order_value(data, state)
    else:
        print('\nНекорректный ввод, введите номер пункта')
    show(ordered_data)