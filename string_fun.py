# string and build-in function

x = "the mind is Everything, what you think you become !!"
print(x.count("m"))     # conut the occurrence
print(x.find("you"))    # return the index the character it's not return -1
print(x.index("!"))     # return the index
print(x.capitalize())   # first letter capital
print(x.title())        # all word first latter capital
print(x.lower())        # all character lower
print(x.upper())        # all character upper
print(x.swapcase())     # trun the swapcase
print(x.replace("!!","...")) # replace the character
print(x.split(" "))     # split the word into return list
print(x.startswith("the")) # find start word return boll values
print(x.endswith("!!"))   # find end word return boll values
print(x.isalnum())
print(x.isalpha())
print(x.isupper())
print(x.islower())

n = "     david      "
print(n.strip())
print(n.rstrip())
print(n.lstrip())

d = "mariya selvam"
d = d.split(" ")
print(" ".join(d))
