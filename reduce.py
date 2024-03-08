# using reduce function

from functools import reduce

num = [33,44,55,66,77,88]
def func(a,b):
    return(a+b)
print(reduce(func,num))

result = reduce(lambda x,y :x+y,num )
print(result)

# find smallest elament in the list unsing reduce
def small(x,y):
    if x < y:
        return x
    else:
        return y
print(reduce(small,num))

# lambda function used

smallest_value = reduce(lambda x,y :x if x < y else y ,num)
print(smallest_value)

