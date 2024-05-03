def category_selector():
    print("Введите номер категории операции:\n"
          "\t[1] Доход\n"
          "\t[2] Расход\n")
    while True:
        category = input()
        if category == '1':
            return '+'
        elif category == '2':
            return '-'
        else:
            print(
                "Введите корректный номер категории\n"
                "\t[1] Доход\n"
                "\t[2] Расход\n"
            )
