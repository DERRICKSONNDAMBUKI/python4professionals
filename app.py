print('Hello Sensei')

# Integer
a = 2
print(a)
# Output: 2
# Integer
b = 9223372036854775807
print(b)
# Output: 9223372036854775807
# Floating point
pi = 3.14
print(pi)
# Output: 3.14
# String
c = 'A'
print(c)
# Output: A
# String
name = 'John Doe'
print(name)
# Output: John Doe
# Boolean
q = True
print(q)
# Output: True
# Empty value or null data type
x = None
print(x)
# Output: None

import keyword
print(keyword.kwlist) # list all the keywords

a = 2
print(type(a))
# Output: <type 'int'>
b = 9223372036854775807
print(type(b))
# Output: <type 'int'>
pi = 3.14
print(type(pi))
# Output: <type 'float'>
c = 'A'
print(type(c))
# Output: <type 'str'>
name = 'John Doe'
print(type(name))
# Output: <type 'str'>
q = True
print(type(q))
# Output: <type 'bool'>
x = None
print(type(x))
# Output: <type 'NoneType'>

a, b, c = 1, 2, 3
print(a, b, c)
# Output: 1 2 3
a, b, _ = 1, 2, 3
print(a, b)
# Output: 1, 2
a = b = c = 1
print(a, b, c)
# Output: 1 1 1

x = [1, 2, [3, 4, 5], 6, 7] # this is nested list
print (x[2])
# Output: [3, 4, 5]
print(x[2][1])
# Output: 4