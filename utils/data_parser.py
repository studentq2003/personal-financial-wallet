def parse(data, field, value):
    new_data = []
    for i in data:
        if field == 'type' and i[field] == value:
            new_data.append(i)
        elif field == 'value' and int(i[field]) == int(value):
            new_data.append(i)
        elif field == 'description' and i[field].startswith(value):
            new_data.append(i)
        elif field == 'id' and i[field] == value:
            new_data.append(i)

    return new_data
