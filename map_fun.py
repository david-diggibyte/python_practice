# map function
# syntax --> map(function, iterables)

def add(number):
    return number + number
number = [11,22,33,44,55,66]
num = list(map(add,number))
print(number,num)


