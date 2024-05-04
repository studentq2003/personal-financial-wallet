from features.read import read
from features.write import write
from components.update_row_interface import update_row_interface
from classes import Data


def update_row():

    target_id, field, value = update_row_interface()

    data = read()
    new_data = []

    for i in data:
        string = Data(i)
        if string.id == target_id:
            if field == 'value':
                string.value = value
            elif field == 'date':
                string.date = value
            elif field == 'time':
                string.time = value
            elif field == 'description':
                string.description = value
        new_data.append({
            'id': string.id,
            'type': string.category,
            'value': string.value,
            'date': string.date,
            'time': string.time,
            'description': string.description
        })
    write(new_data)


