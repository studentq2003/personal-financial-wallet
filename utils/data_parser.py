def parse(data, field, value):
    new_data = []
    for i in data:
        if i[field] == value:
            new_data.append(i)
        if field == 'value' and int(i[field]) == int(value):
            new_data.append(i)
        if field == 'description' and i[field].startswith(value):
            new_data.append(i)

    return new_data
