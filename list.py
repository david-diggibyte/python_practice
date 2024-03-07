# List and built-in function

list1 = [55,66,77,85,4356,78,90987654,78,65,789,765,32]
list1.sort() # sorting the list asc to desc
print(list1)
list1.reverse() # reversed the list
print(list1)
count=list1.count(78) # return how many times there that element in list
print(count)
index=list1.index(85) #return that element index
print(index)
list1.append(10000) # add the element in end of the list
print(list1)
list1.insert(0,1) # insert the element based on the index in list
print(list1)
list2 = [555,666,777,888,999]
list1.extend(list2) # adding the another list into list
print(list1)
list1.pop(0) # remove the element based on the index
print(list1)
list1.remove(10000) # remove the element based on the value
print(list1)
print(len(list1)) # return the length of list
print(min(list1)) # return the smallest element in the list
print(max(list1)) # return the largest element in the list
copy_list1 = list1.copy() # copy the list into another variable
print(copy_list1)
copy_list1.clear() # rempved the all element in the list
print(copy_list1)
