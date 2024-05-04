import json
from variables import path, datafile, balance_file, backup_file


def write(data):
    with open(path + datafile, 'w') as f:
        json.dump(data, f)

def write_backup(data):
    with open(path + backup_file, 'w') as f:
        json.dump(data, f)


def write_balance(data):
    with open(path + balance_file, 'w') as f:
        json.dump(data, f)
