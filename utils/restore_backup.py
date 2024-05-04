from variables import system_backup_file, backup_file, schema, datafile
from features.read import read_backup, read_system_backup
from features.write import write, write_backup
from utils.validate_json import validate_json
from components.colors import error, purple, default


def restore_backup():
    try:
        data = read_backup()
        if validate_json(data, schema):
            write(data)
            print(purple(
                f"{datafile} восстановлен из {backup_file}\n"
            ))
        else:
            print(default(
                "Попытка восстановить из системного бекапа..."
            ))
            restore_system_backup()
    except Exception:
        print(default(
            "Попытка восстановить из системного бекапа..."
        ))
        restore_system_backup()


def restore_system_backup():
    try:
        data = read_system_backup()
        if validate_json(data, schema):
            write(data)
            write_backup(data)
            print(
                purple(
                    f"Файл {datafile} восстановлен из {system_backup_file}\n"
                    f"Файл {backup_file} восстановлен из {system_backup_file}\n"
                ))
        else:
            print(
                error(
                    "Все бекап файлы потеряны, даже системный. "
                    "Скачивайте программу заново, и в будущем не трогайте системные файлы"
                ))
    except Exception:
        print(
            error(
                "Все бекап файлы потеряны, даже системный. "
                "Скачивайте программу заново, и в будущем не трогайте системные файлы"
            ))
