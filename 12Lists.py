# GENERATING RANDOM LIST

from random import randint
lst = [randint(1,7) for _ in range(10)]
print(lst)

# FOR RANDOM LIST

list1 = sum(lst[:5])
list2 = sum(lst[5:])
if(list1>list2) : print("TEAM1")
elif(list2 >list1): print("TEAM2")
else: print("DRAW")

# FOR PARTICULAR LIST

# list1 = [4,7,3,4,4,4,7,7,4,4]

# list1 = sum(list[0:5])
# list2 = sum(list[5:10])
# if(list1>list2) : print("TEAM1")
# elif(list2 >list1): print("TEAM2")
# else: print("DRAW")