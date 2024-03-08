# using filter function

# find odd numbers in list using filter function

list1 = [11,22,33,44,55,66,77,88]
odds = filter(lambda x: x % 2 == 1 ,list1)
print(list(odds))

# find greater then hundred in the tuple using filter function

tuple1 = (333,44,555,66,7777,88,8888,66,200,100)
hundred = filter(lambda x : x >= 100 , tuple1)
print(tuple(hundred))