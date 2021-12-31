print("DICTIONARY IS COLLECTION OF KEY VALUE PAIR")
print("DICTIONARY IS UNORDERED DATA TYPE")
print("DICTIONARY IS MUTABLE DATA TYPE")
print("DICTIONARY CONTAINS KEYS ARE HASHABLE/ IMMUTABLE")
print("DICTIONARY IS SAID TO BE OBJECT IN JAVASCRIPT")

data = {
    'Name': 'Python',
    'Version': ['1.X', '2.X', '3.X'],
    'Father': 'Guido Van Rossum',
    'Website': 'www.python.org'
}
# IN PLACE OF INDEX WE USE KEYS , KEYS ARE UNIQUE
value = data['Name']
print(value)
value1 = data['Website']
print(value1)
data['Name'] = 'Python Programming'
print(data['Name'])

print(data.keys())
print(data.values())
print(data.items())

keys = list(data.keys())
print(keys)
values = list(data.values())
print(values)
items = list(data.items())
print(items)
value2 = data.get('Name')
print(value2)
value3 = data.get('abcd', 'Not Found')
print(value3)

student = {
    '19EARCS090': ['RAJAT KHANDELWAL', 6377529014],
    '19EARCS091': ['RAJAT YADAV', 9641198745],
    '19EARCS092': ['RAJEEV DEY', 6985214956],
    '19EARCS093': ['REHAN KHAN', 9865326941],
    '19EARCS094': ['ROHAN KHANDELWAL', 8764090615]
}

print(student);
print(student.keys())
print(student.values())
print(student.items())