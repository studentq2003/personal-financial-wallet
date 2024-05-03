class Stats:
    def __init__(self, type, value, date):
        if type == '-':
            self.type = 'Списание'
        else:
            self.type = 'Пополнение'
        self.value = value
        self.date = date
