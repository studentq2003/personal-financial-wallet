import json
from variables import path, datafile, balance_file, backup_file, system_backup_file
from components.colors import error, purple


def read():
    try:
        with open(path + datafile, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(
            error(
                f"Файл {datafile} с данными не найден. Восстановление файла из {backup_file}..."
            ))
        try:
            with open(path + backup_file, "r") as f:
                data = json.load(f)
            with open(path + datafile, "w") as f:
                json.dump(data, f)
                print(
                    purple(
                        f'Файл {datafile} успешно восстановлен из {backup_file}...'
                    )
                )
        except Exception:
            pass


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
