# PROBLEM STATEMENT : 
# You are given n rounds of two teams 
# Write a program to print name of winner team 
# If both teams scored same print draw

# INPUT FORMAT :
# First line contain an integer n which denotes number of rounds
# Second line contains 2*n space seprated integers such that 
# First n integers are performance of team 1 in n rounds 
# Last n integers are performance of team 2 in n rounds

# OUTPUT FORMAT :
# Print "TEAM1" if team 1 wins the game
# Otherwise print "TEAM2" if team 2 wins the game
# Else print "DRAW"

# CONSTRAINTS :
# 2 <= n <= 10
# 0 <= arr[i] <= 100

# TEST CASE 1 :
# 3
# 1 2 3 3 2 1

# OUTPUT :
# DRAW

#TEST CASE 2 :
# 5
# 3 5 3 2 6 7 4 3 2 1

# OUTPUT :
# TEAM1

# STEP 1:
# n = int(input())
# arr = input()                   // spit and then parsing/looping, iteration is accessing each value
# print(repr(arr), type(arr))

# STEP 2:
# map(function, iterable)
# list(map(int, ["12","6"])) it converts string into int...acting like a function

# STEP 3:
# n = int(input())
# arr = input().split()
# print(arr)
# result = list(map(int,arr))
# print(result)

print("ENTER NUMBER: ")
n = int(input())
scores = list(map(int, input().split()))
print(scores)
list1 = sum(scores[:5])
list2 = sum(scores[5:])
if(list1>list2) : print("TEAM1 WINS")
elif(list2 >list1): print("TEAM2 WINS")
else: print("MATCH DRAW")
