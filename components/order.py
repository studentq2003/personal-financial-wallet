from features.read import read
from features.order import order_date, order_value
from components.desc import desc
from components.colors import error, default


def order():
    global ordered_data

    try:
        data = read()
    except Exception:
        error(error)

    while True:
        print(default(
            "\nПо какому полю сортировать?"
        ))
        print(
            '\n[1] По дате и времени'
            '\n[2] По сумме'
        )
        inp = input('\n')
        if inp == '1':
            state = desc()
            ordered_data = order_date(data, state)
            return ordered_data
        elif inp == '2':
            state = desc()
            ordered_data = order_value(data, state)
            return ordered_data
        else:
            print(error('\nНекорректный ввод, введите номер пункта'))
