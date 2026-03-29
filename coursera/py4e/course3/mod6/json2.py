# json2.py
import json

input = '''[
    {
        "id":"001",
        "x":"2",
        "name":"Ladoblanco"
    },
    {
        "id":"009",
        "x":"7",
        "name":"Odalis"
    }
]'''

info = json.loads(input)
print('User count;',len(info))

for obj in info:
    print()
    print('Name:',obj['name'])
    print('Id:',obj['id'])
    print('Attribute:',obj['x'])

