# lambda function

x = lambda x,y,z : (x + y + z)*2
print(x(2,3,4))

# lamda function with astric

addition = lambda *args : sum(args)
print(addition(55,44,33,22))

# find substring or nor using lambda function
sub_string = lambda string: string in "live or die"
print(sub_string("live"))

mum = [112,22,33,4444,555,6666,77,88888,9]


 # index using lambda function

index = lambda word : word[-1]
print(index("lambda"))

# palidrome or not

palindrome = lambda word : word == word[::-1]
print(palindrome(word = "madam"))

