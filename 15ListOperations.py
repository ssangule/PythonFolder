lst = []

# ALL THESE METHODS DO NOT RETURN VALUES ---
lst.append('Java')
lst.insert(0, 'Ruby')
lst.insert(1, 'Perl')
lst.extend(['C', 'C++', 'Swift'])
lst.insert(3, 'Go')
lst.append(['.net', 'php'])
lst.extend('python') # extend do iterate where as append do add values
lst.append('Dart')
lst.insert(1, "Python")
lst.extend('1234')
lst.extend([["python", "python"], ["java", "C", "C++"]])
print(lst)

# IT WILL PRINT THE LIST IN VERTICAL MANNER----
from pprint import pprint
lst = []

lst.append('Java')
lst.insert(0, 'Ruby')
lst.insert(1, 'Perl')
lst.extend(['C', 'C++', 'Swift'])
lst.insert(3, 'Go')
lst.append(['.net', 'php'])
lst.extend('python') # extend do iterate where as append do add values
lst.append('Dart')
lst.insert(1, "Python")
lst.extend('1234')
lst.extend([["python", "python"], ["java", "C", "C++"]])

# WE HAVE TO PROVIDE PARTICULAR WIDTH IN WHICH IT WILL INCLUDE ELEMENTS
pprint(lst, width=20)

# FOR REMOVE OR DELETE OPERATIONS---

# item = lst.pop() it returns value and delete last element automatically
# item = list.pop(loc) it returns value and delete the value at specified location
# list.remove(item) if item in the list then delete first occurence of that item
# nums.pop(100) it will show index out of range error
# list.count(item) will return frequency of item in list
# list.index(item) will return first index of item
# list.clear() it will deletes each and every relement in list
# Note:-  list should be homogeneous to sort


nums = [1,5,6,2,5,5,3,4,5]
print(nums)
c = nums.count(5)
print(c)
for _ in range(c):
    nums.remove(5)
print(nums)
nums.sort()
print(nums)


lang = ['java', 'c', 'c++', 'python', 'ruby', 'perl']
lang.pop()
lang.pop(2)
print(lang)
lang.insert(1,'python')
lang.insert(3, 'python')
print(lang)
lang.remove('python')
i = lang.index('python')            # if value find then its ok otherwise it will give value error
print(i)
print(lang)


data1 = [
    ['sachin', 80],
    ['rajat', 85],
    ['simran', 95],
    ['kushal',100],
    ['yadavendra', 77]
]
# data1.sort()
print(data1)

# JUST FOR SORT IMPORTED DATA WE IMPORT THIS PACKAGE
from operator import itemgetter
f = itemgetter(2)
lst = ['python', 'java', 'c++']
print(f(lst))

data1.sort(reverse = True, key=itemgetter(1))
print(data1)


print("List does not contain data, it contain references, since list is mutable while using copy function it will copy reference not object...Copy function is used for copying values onlu")
lst11 = lst.copy()
print(lst11)

copy = lst
lst.append(5)
item = copy.pop(0)
print(copy)
print(lst)

lst = [1,2,3,4]
copy = lst[:]
lst.append(5)
item = copy.pop(0)
print(lst)
print(copy)
