from variables import system_backup_file, backup_file, schema
from features.read import read_backup, read_system_backup
from features.write import write
from utils.validate_json import validate_json
from components.colors import error


def restore_backup():
    try:
        data = read_backup()
        if validate_json(data, schema):
            write(data)
            print(f"datafile восстановлен из {backup_file}")
    except Exception:
        pass


def restore_system_backup():
    try:
        data = read_system_backup()
        if validate_json(data, schema):
            write(data)
            print(f"datafile восстановлен из {system_backup_file}")
    except Exception:
        print(
            error(
                "Все бекап файлы потеряны, даже системный. "
                "Скачивайте программу заново, и в будущем не трогайте системные файлы"
            ))
