# dictionary and build-in function

dict1 = {"name":"david","age":22,"gender":"male","state":"tamil nadu","streem":"computer science"}
print(dict1)
print(dict1["name"]) # using key
print(dict1.get("age")) # using get function
print(dict1.keys()) # print all keys only
print(dict1.values()) # print all values only
print(dict1.items()) # print all keys and values
dict1.update(degree="bsc") # updated one key and values
print(dict1)
print(dict1.popitem()) #popitem delete end of the key and value
print(dict1.pop("name")) # delete itenm using key
dict2 = dict1.copy() # copy the dict to another variable
print(dict2)
dict2.clear() # delete the all items in dictionary
print(dict2)

