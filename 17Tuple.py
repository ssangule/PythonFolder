print("TUPLE IS IMMUTABLE LIST, WE CANNOT CHANGE OR UPDATE THE VALUES, LIST AND TUPLE BOTH STORE REFERENCES NOT DATA")

t = (1,2,3)
print("Tuple Is: ", t) 
print("Type of this tuple: ",type(t))


lang = ('java', 'c', 'c++', 'python')
print("Tuple is: ", lang)
print("Type of tuple is : ", type(lang))
print(lang[2])
print(lang[-2])
print(lang[:-2])
print(dir(lang))
print(lang.count('java'))
print(lang.index('c'))         
print(lang.index('python'))

#lang[2] = 'Hii'  IT WILL SHOW ERROR BECAUSE WE CANNOT CHANGE OR ASSIGN VALUES

print("DIFFERENT TYPES OF TUPLES : ")
tup = 5
print(type(tup))
tup1 = (5)
print(type(tup1))
tup2 = (5,)
print("SINGLE ELEMENT TUPLE : " ,type(tup2))
tup3 = 1,2,3,4,5,6,7,8,9
print(type(tup3))

print("EXAMPLE SHOWING, TUPLE STORE REFERENCES NOT DATA")
tu = (1,2,3,4,5)
print(tu)
tu = tu[::-1]
print(tu)

t1 = (1,2,3,4,5)
x = t1                               # REFERENCE CREATED
print(t1, id(t1))
print(x, id(x))
t1 = t1[::-1]
print(t1, id(t1))
print(x, id(x))

print("TUPLE CONTAINS LIST SO WE CAN CHANGE VALUES OF TUPLE")
tup4 = (1,2,[3,4],5)
print(tup4, type(tup4))
tup4[2].append(100)
print(tup4)