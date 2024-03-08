# map function
# syntax --> map(function, iterables)

def add(number):
    return number + number
number = [11,22,33,44,55,66]
num = list(map(add,number))
print(number,num)


# type casting using map function in list

number = ["1","2","3","4","5","6"]
number = list(map(int,number))
print(number,type(number[5]))

# suere using map and lambda function in list

number = [11,22,33,44,55,66,22]
num = list(map(lambda x: x*2,number))
print(num)

# break the sub string using in map

names = ["david","mari","salman","kishore","vijay"]
names = list(map(tuple,names))
print(names)

# using 2 list in map function

list1 = [22,33,44,55,66,77]
list2 = [88,77,66,55,44,33]
result = map(lambda x,y : x-y,list1,list2)
print(list(result))