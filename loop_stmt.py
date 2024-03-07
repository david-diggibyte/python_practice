# looping statement
#iterate list using for loop"
x = ["david","susai","sasi","chandrhu","seelan","akilan"]
for i in x:
    print(i)
# using range function in for loop
for i in range(0,20,2):
    print(i)
# iterate dictionary using for loop

user = {"name":"david","age":22,"gender":"male","degree":"bsc","native":"kallakuruchi"}
for i,j in user.items():
    print(i,j)
# While loop
n = int(input("Enter a number:"))
count = 0
while count <= n:
    print(count)
    count += 1
#  iterate sequence using while loop
names = ("mani","david","anand","sasi","alex","sathya")
count = 0
while count < len(names):
    print(names[count])
    count += 1