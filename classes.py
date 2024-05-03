class Data:
    def __init__(self, data):
        category = data['type']
        value = data['value']
        date = data['date']
        time = data['time']
        description = data['description']

        self.category = category
        self.value = value
        self.date = date
        self.time = time
        self.description = description
