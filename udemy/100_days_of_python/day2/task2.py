# task2.py

# print(len(1234)) # the function len() can't take the number data type
print(len("string"))
print()

# how do we check types - type()
print(type("hello"))  # <class 'str'>  Note types are classes as expected
print(type(2))  # <class 'int'>
print(type(2.5))  # <class 'float'>
print(type(True))  # <class 'bool'>
print()

# type conversion (type casting)
print(type(int("123")))
print(int("123") + int("456"))
# print(int('abc')) #ValueError: invalid literal for int() with base 10: 'abc'
print()

print('Number of letters in your name: '+str(len(input("Enter your name: "))))
