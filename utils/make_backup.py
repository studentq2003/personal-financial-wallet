from variables import system_backup_file, backup_file, datafile, schema
from features.read import read
from features.write import write_backup
from utils.validate_json import validate_json

def make_backup():
    data = read()
    if validate_json(data, schema):
        write_backup(data)
        print(f"Backup создан в записан {backup_file}")
