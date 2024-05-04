from jsonschema import validate
from features.read import read


def validate_json(data, schema):
    try:
        for i in data:
            try:
                validate(i, schema)
            except Exception:
                return False
        return True
    except Exception:
        return False


# schema = {
#     "type": "object",
#     "properties": {
#         "type": {
#             "type": "string",
#             "enum": ["+", "-"]
#         },
#         "value": {"type": ["number", "string"]},
#         "date": {"type": "string"},
#         "time": {"type": "string"},
#         "description": {"type": "string"},
#     },
#     "required": ["value", "date", "time"],
# }
#
# data = [
#     {
#         "type": "+",
#         "value": "100",
#         "date": "04-05-2024",
#         "time": "10:50",
#         "description": "Example test balance"
#     },
#     {
#         "type": "+",
#         "value": 20000,
#         "date": "05-01-2001",
#         "time": "11:11",
#         "description": "Example"
#     },
#     {
#         "type": "+",
#         "value": 2222,
#         "date": "04-05-2024",
#         "time": "12:06",
#         "description": "1"
#     }
# ]
#
# data = {
#     "type": "+1",
#     "value": "65000",
#     "date": "03-05-2024",
#     "time": "15:00",
#     "description": "Salary"
# }

#
# try:
#     validate_json(data, schema)
# except Exception as e:
#     print(e)
