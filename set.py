# set and build-in function

set1 = {444,33,3,3554,654,65,4345,765345,876}
set1.add(92) # add the element
print(set1)
set2 = {55,555,5555,55555}
set1.update(set2) # add set into another setr
print(set1)
pop = set1.pop() # removed the element in set
print(pop)
set1.remove(444) # removed the element based on the value
print(set1)
set1.discard(444) # removed the element based on the value
print(set1)