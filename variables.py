path = './'
datafile = 'data/money.json'
balance_file = 'data/balance.json'
backup_file = 'data/backup.json'
system_backup_file = 'data/system_backup.json'

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "type": {
            "type": "string",
            "enum": ["+", "-"]
        },
        "value": {"type": ["number", "string"]},
        "date": {"type": "string"},
        "time": {"type": "string"},
        "description": {"type": "string"},
    },
    "required": ["id", "value", "date", "time"],
}
