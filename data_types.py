# data types and variables

x = 33
print(type(x))

# converting the data type using type casting

y = float(x)
print(x,type(y))

# converting to string

z = str(x)
print(z , type(z))

# string to list

list1 = list(z)
print(list1,type(list1))

# converting list to tuple using type casting

tuple1 = tuple(list1)
print(tuple1,type(tuple1))

# converting tuple to set using type casting

set1 = set(tuple1)
print(set1,type(set1))

# converting set to list using type casting
list2 = list(set1)
print(list(set1))

# converting tuple to list

v = (1,2,3,54,6)
print(v,type(v))