path = './'
datafile = 'money.json'
balance_file = 'data/balance.json'
backup_file = 'data/backup.json'
system_backup_file = 'data/system_backup.json'

schema = {
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "enum": ["+", "-"]
        },
        "value": {"type": ["number", "string"]},
        "date": {"type": "string"},
        "time": {"type": "string"},
        "description": {"type": "string"},
    },
    "required": ["value", "date", "time"],
}
