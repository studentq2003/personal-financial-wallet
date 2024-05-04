class Data:
    def __init__(self, data):
        id = data['id']
        category = data['type']
        value = data['value']
        date = data['date']
        time = data['time']
        description = data['description']

        self.id = id
        self.category = category
        self.value = value
        self.date = date
        self.time = time
        self.description = description


class Balance:
    def __init__(self, data):
        value = data['balance']
        self.value = value
