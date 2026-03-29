# Operators are used to operate on the values of variable.

# Arihmetic Operators
a = 34
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a%b) # Return remainder
print(a/b) # Return type float quotient
print(a//b) # Return type integer , Returns the largest integer ≤ result
# It rounds down (towards negative infinity)
print(a**b)  # a is raised to the power b.

# Conditional Operators: Return only true or False.
print(a>4)
print(a<4)
print(a!=34) # != not equal to

# Logical Operators
c=True
d=False
print(c and d)
print(c and c) # and returns true when both are true.
print(d and d)
print(d and c)
a=True
b=False
print(a or b)
print(a or a)
print(b or a)
print(b or b) # Or returns true if any one of is true.

print(not(True)) # Reverses the written.
print(not(False))

#Assignment Operator(Every Arithmetic Operator with = means assigning value)
a = 32
print(a)
a+=9
a-=3
print(a)
