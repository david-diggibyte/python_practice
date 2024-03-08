# lambda function

x = lambda x,y,z : (x + y + z)*2
print(x(2,3,4))

# lamda function with astric

addition = lambda *args : sum(args)
print(addition(55,44,33,22))

# find substring or nor using lambda function
sub_string = lambda string: string in "live or die"
print(sub_string("live"))

