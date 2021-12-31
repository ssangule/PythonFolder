print("DIFFERENCE BETWEEN SHALLOW COPY AND DEEP COPY ")

print("Answer --- The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original. A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original")

print("QUESTION 1 --- >")

users = ['ram', 'shyam', 'ghanshyam', 'hari', 'mohan']
password = ['123','456','65445', 'irah','nahom']
accounts = [1001, 1002, 1003, 1004, 1005]
balance = [50000, 60000, 10000, 25000, 90000]

acc = int(input("Account Number : "))
amount = int(input("Amount: "))
i = accounts.index(acc)
if(balance[i] >= amount): balance[i] = balance[i] - amount
print(balance)

print("QUESTION 2 --- >")

data = []
data.append(5)
data.insert(0, 'Hello')
data.extend('123')
data.pop(2)
data.append('World')
data.insert(3, 'Python')
data.append('Python')
data.pop(0)
data.remove('Python')
data.reverse()
print(data)