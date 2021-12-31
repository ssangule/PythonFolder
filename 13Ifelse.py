# SOMETIMES IF/ELSE PROGRAMMING IS ALSO CALLED SEQUENTIAL PROGRAMMING----

# SEQUENTIAL PROGRAMMING - 
#                           LINE BY LINE EXECUTION OF CODE...SO WE USED GROUP OF STATEMENTS...FOR THIS WE USED CURLY BRACES...IF WE ADD IF/ELSE THEN IT IS CONDITION OR IF WE NOT ADD IF/ELSE THEN IT IS A SIMPLY BLOCK...

# SELECTION PROGRAMMING - MAIN ROLE OF IF/ELSE (SELECTION STATEMENTS) 

# t1 = 100
# t2 = 200

# if t1>t2: print("team1")
# elif t2>t1: print("team2")
# else: print("draw")


print("ENTER NUMBER:")
n = int(input())

if (n%2 == 0 and n%3 == 0): print("YAY")
elif(n%2 != 0 and n%5 == 0): print("YOYO")
else: print("NAY")


# ANOTHER METHOD - NESTED IF ELSE---->

# if n%2 ==0:
#     if n%3 == 0:
#         print("YAY")
#     else:
#         print("DIVISIBLE BY 2 BUT NOT BY 3")
# elif n%2 != 0:
#     if n%5 == 0:
#         print("YOYO")
#     else:
#         print("NOT DIVISIBLE BY 2 AND NOT BY 5")
# else:
#     print("NAY")