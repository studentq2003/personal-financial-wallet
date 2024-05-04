path = './'
datafile = 'money.json'
balance_file = 'balance.json'
backup_file = 'backup.json'
system_backup_file = 'system_backup.json'

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
