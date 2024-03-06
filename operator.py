# operator
# Arithmetic operators
a = 20
b = 10
print(f"addition:{a+b}")
print(f"subtraction:{a-b}")
print(f"multiplication:{a*b}")
print(f"division:{a/b}")
print(f"floor division:{a//b}")
print(f"Exponation:{a**b}")

# Assignment operators

x = 5
x += 2
print({x})
x -= 1
print(x)
x *= 2
print(x)
x /= 2
print(x)
x //= 2
print(x)
x **= 2
print(x)
x %= 2
print(x)

# Relation operator
a = 5
print(a)
b = 10
print(a == b)
print( a != b)
print(a > b)
print(a < b)
print( a >= b)
print(a <= b)

# logical operator
print("Logical operator")
print( 5 > 10 and 15 > 10)
print(5 > 10 or 15 > 10)
print(not(True))

# identity operator (in this operator is compare thr memory address of two object)
# 1) is 2) is not
a = 10
b = 20
print( a is b)
print( a is not b)

# membership operator
# 1) in 2) in not
a = [33,22,44,55,6]
print(21 in a)
print(21 not in  a)