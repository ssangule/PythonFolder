print("\n***************************LIST***************************")

print("\n\nList is the Collection of mutable and immutable objects")
print("List is the Collection of types/ data types")
print("Homogeneous list also known as Array")
print("List itself is Mutable data type")
print("List does not store data it stores references")
print("List Is ordered data type in this we can use slicing Also...")

nums = [10,20,30,40];
print("\n\nNums list of same data type, All Elements are integers so this is homogeneous")
data = ["sachin", "rajat", "kushal", "simran"]
print("Data list contains all the elements of string data type that is homogeneous")
info = ["sachin", 90, "rajat", 100]
print("Info list contains elements of string & int data type that is heterogeneous")
print(type(info))

print("\n\nSuppose datas are given and there are two teams in which first team is Team1 and second one is Team2..So find total scores of both teans and also Which team win")
datas = [4,2,4,6,7,3,4,5,7,8,9,10]
data1 = sum(datas[::2])
data2 = sum(datas[1::2])
if data1 > data2 : print(f"TEAM1 Wins as {data1-data2} points more")
else: print(f"TEAM2 wins as {data2-data1} points more...")
