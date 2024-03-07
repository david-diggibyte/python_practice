# using control flow stmt in loop
# using break keyword
for i in range(0,10):
    if 6 == i:
        break
    print(i)

# using continue keyword
for i in range(0,10):
    if 5 == i:
        continue # skip the 5
    print(i)

# iterate sequence using break keyword in loop

name = ("david","selvam","mary","sasi","akilan","sathya")
for i in name:
    if "sasi" == i:
        break
    print(i)