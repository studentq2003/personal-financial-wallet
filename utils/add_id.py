from utils.id_generator import id_generator
from features.write import write
from classes import Data


def add_id(data):
    global id
    new_data = []
    for i in data:
        string = Data(i)
        if string.id == '':
            while True:
                id = id_generator()
                for j in data:
                    if j['id'] == string.id:
                        continue
                break

            new_data.append(
                {
                    "id": id,
                    "type": string.category,
                    "value": string.value,
                    "date": string.date,
                    "time": string.time,
                    "description": string.description,
                }
            )
        else:
            new_data.append(
                {
                    "id": string.id,
                    "type": string.category,
                    "value": string.value,
                    "date": string.date,
                    "time": string.time,
                    "description": string.description,
                }
            )
    write(new_data)
