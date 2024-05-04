import json
from variables import path, datafile, balance_file, backup_file, system_backup_file
from components.colors import error


def read():
    try:
        with open(path + datafile, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл с данными не найден. Восстановление файла из backup...")
        with open(path + backup_file, "r") as f:
            data = json.load(f)
        with open(path + datafile, "w") as f:
            json.dump(data, f)


def read_backup():
    try:
        with open(backup_file, "r") as f:
            return json.load(f)
    except Exception:
        pass


def read_system_backup():
    try:
        with open(system_backup_file, "r") as f:
            return json.load(f)
    except Exception:
        pass


def read_balance():
    try:
        with open(path + balance_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(
            error(
                "Файл с данными не найден. Восстановление файла из backup..."
            ))
