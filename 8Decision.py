# IF ELSE IN PYTHON

# if condition 1: #bina column ke no spaces
#     #spaces we used have indentated space before it
#     st1
#     st2
#     st34
#     if condition 2:
#         st4   # we not used semicolon in python bcoz in python each line is new line
#         st5
#     else : 
#         st6
#         st7
#         st8

choice = input("choice : (yes/no)").strip().lower()
print(repr(choice))

if choice == "yes":
    print("Continue reading")
else: 
    print("WE can go home")