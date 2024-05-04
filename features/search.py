from features.read import read
from utils.data_parser import parse
from features.show import show


def search(field, value):
    data = read()

    new_data = parse(data, field, value)

    show(new_data)
