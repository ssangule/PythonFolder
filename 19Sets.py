print("A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes like we do in lists.")

myset = set(["a", "b", "c"])
print(myset)
myset.add("d")
print(myset)

print("******************************************************************************")

people = {"Jay", "Idrish", "Archi"}
print("People:", end = " ")
print(people)
people.add("Daxit")
for i in range(1, 6):
	people.add(i)
print("\nSet after adding element:", end = " ")
print(people)

print("******************************************************************************")

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
population = people.union(vampires)
print("Union using union() function")
print(population)
population = people|dracula
print("\nUnion using '|' operator")
print(population)

print("******************************************************************************")

set1 = set()
set2 = set()
for i in range(5):
	set1.add(i)
for i in range(3,9):
	set2.add(i)
set3 = set1.intersection(set2)
print("Intersection using intersection() function")
print(set3)
set3 = set1 & set2
print("\nIntersection using '&' operator")
print(set3)

print("******************************************************************************")

set1 = set()
set2 = set()
for i in range(5):
	set1.add(i)
for i in range(3,9):
	set2.add(i)
set3 = set1.difference(set2)
print(" Difference of two sets using difference() function")
print(set3)
set3 = set1 - set2
print("\nDifference of two sets using '-' operator")
print(set3)

print("******************************************************************************")

# s1 == s2	s1 is equivalent to s2
# s1 != s2	s1 is not equivalent to s2
# s1 <= s2	s1 is subset of s2
# s1 < s2	s1 is proper subset of s2
# s1 >= s2	s1 is superset of s2
# s1 > s2	s1 is proper superset of s2
# s1 | s2	the union of s1 and s2
# s1 & s2	the intersection of s1 and s2
# s1 – s2	the set of elements in s1 but not s2
# s1 ˆ s2	the set of elements in precisely one of s1 or s2

set1 = set()
set2 = set()
for i in range(1, 6):
	set1.add(i)
for i in range(3, 8):
	set2.add(i)
print("Set1 = ", set1)
print("Set2 = ", set2)
print("\n")
set3 = set1 | set2
print("Union of Set1 & Set2: Set3 = ", set3)
set4 = set1 & set2
print("Intersection of Set1 & Set2: Set4 = ", set4)
print("\n")
if set3 > set4:
	print("Set3 is superset of Set4")
elif set3 < set4:
	print("Set3 is subset of Set4")
else :
	print("Set3 is same as Set4")
if set4 < set3:
	print("Set4 is subset of Set3")
	print("\n")
set5 = set3 - set4
print("Elements in Set3 and not in Set4: Set5 = ", set5)
print("\n")
if set4.isdisjoint(set5):
	print("Set4 and Set5 have nothing in common\n")
set5.clear()
print("After applying clear on sets Set5: ")
print("Set5 = ", set5)
