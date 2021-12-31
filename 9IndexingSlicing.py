print("*******************INDEXING*****************************")

s = "HELLO WORLD!"

print("Accessing element in string-->")
char = s[-5]
char1 = s[10]
print(char, char1)

print("Printing whole string one by one-->")
for i in range(0, 11):
    print("At Index -",i, "Value - ",s[i])


print("***********************SLICING*******************************")

print("Trying to get a part of the string-->")
s1 = s[3] + s[4] + s[5] + s[6]
print(s1)

print("With the help pf in-built function--->")
s2 = s[3:7]                                          #default value of step is +1
print(s2)
print(repr(s2))                                      #repr basically print with double quotes

print("Doing some slicing operations with positive steps ahead--->")
print(repr(s[2:9]))
print(repr(s[0:5]))
print(repr(s[:5]))
print(repr(s[1:10:2]))
print(repr(s[::2]))

print("Doing some slicing operations with negative steps ahead--->")
print(repr(s[-12:-7]))
print(repr(s[-5:12]))
print(repr(s[::-1]))
print(repr(s[-11:9:4]))
print(repr(s[:5:-2]))
print(s[4::-1])
print(s[10:5:-1])
print(s[-4:1:-2])


print("Problem Is we have a string given and we have to print the word 'Awesome'--->")
str1 = "AOWMEES"
str2 = str1[::2]                    #it will takes values like - "awes"
str3 = str1[1::2]                   #it will take vaues like - "ome"
str4 = str2 + str3
print(str4)
