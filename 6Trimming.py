ss = "   \n\t\t  Hello World  \t\t\n   "
print(ss)          
print(repr(ss))     
ss1 = ss.strip()
print(ss1)
print(repr(ss1))
s2 = ss.strip("")     

sss = "!@#$%&*$@#%!!@#Rajat@Khandelwal#$@%$#!&"
sss1 = sss.strip("$#@!%*&")                          # Here all the symbols are remove

print(sss1)