import json

merged = {}

with open('users1.json') as f:
    data1 = json.load(f)
    merged.update(data1['table']['users'])

with open('users2.json') as f:
    data2 = json.load(f)
    merged.update(data2['table']['users'])

merged_list = list(merged.values())

with open('users.json', 'w') as f:
    json.dump(merged_list, f, indent=4)
