from datetime import datetime


def check_date(date):
    if datetime.now().date() < datetime.strptime(date, '%d-%m-%Y').date():
        print("Нельзя вводить время позже текущего.\n"
              "Если Ваша операция запланирована на более позднее время, "
              "укажите любое время, потом обновите его командой --update")
        return False
    return True


def check_time(date, time):
    current_time = datetime.now().strftime("%H:%M")
    if datetime.now().date() < datetime.strptime(date, '%d-%m-%Y').date():
        print("Нельзя вводить дату позже текущей.\n"
              "Если Ваша операция запланирована, "
              "введите любую предыдущую дату, а в день операции "
              "обновите данные командой --update")
        return False
    elif current_time < time:
        if datetime.now().date() == datetime.strptime(date, '%d-%m-%Y').date():
            print("Нельзя вводить время позже текущего.\n"
                  "Если Ваша операция запланирована на более позднее время, "
                  "укажите любое время, потом обновите его командой --update")
            return False
    return True
