# Write a program to take person name, DOB as input and print a message like
# input: name = "sachin"
# birthyear = '1996'
# output: "hello sachin, you are 25 years old"


current_year = 2021
name = input("enter your name : ")
birthyear = int(input("year: "))
age = current_year-birthyear

print("hello",name,"you are",age, "years old.")
print(f"hello {name}, you are {age} years old.")

# You are writting in one line but that is large sentence then use backslash and come in second line then also it will treated as same line
