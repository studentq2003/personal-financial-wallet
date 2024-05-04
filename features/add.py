from components.add_input import add_input
from features.read import read
from features.write import write


def add():
    jdata = read()
    data = add_input()
    jdata.append(data)
    write(jdata)
