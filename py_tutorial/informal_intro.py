# informal_intro.py

# this is the first comment
spam = 1 # and this is the second comment
text = "# This is not a comment because it's inside quotes."
print(text)


# NUMBERS
print(2+2)
print(50-5*6)
print((50-5*6)/4)
print(8/5) # division always returns a floating point number

# to do floor division use //; to calculate the remainder use %
print()
print(17/3) # classic division returns a float
print(17//3) # floor division returns an int and throws away the fractional part
print(17%3) # the % operator returns the remainder of the division
print(5*3+2) # 17
print()

# with python its possible to sue the ** operator to raise a number to a power
print(5**2) # 5 squared
print(2**7) # 2 to the power of 7
print()

# The equal sign = is used to assign a value to a variable. Afterwards, no result
# is displayed before the next interative prompt (if in the interactive mode)
width = 20
height = 5*9
print(width*height)
print()

# if a variable is not "defined" (assigned a value), trying to use it will give an error
# print(n) # Error: try to access an undefined variable

# There is full support for floating point; operators with mixed type operands convert the
# integer operand to floating point
print(4*3.75-1)
print()

# in addition to int and float, Python supports other types of numbers, such as Decimal and 
# Fractions. Python also has built-in support for complex numbers and uses the j or J prefix
# to indicate the imaginary part of a complex number

# 3.1.2 - TEXT:
print('spam eggs')  # single quotes
print("Paris rabbit got your back :)! Yay!")  # double quotes
print('1975') # digits and numerals enclosed in quotes are also strings
print()

#escaping special characters
print('doesn\'t') # use \' to escape a single quote
print("doesn't") # ... or use double quotes
print('"Yes," they said')
print("\"Yes,\" they said")
print('"Isn\'t," they said.')
print()

# escape characters work as expected
print('First line.\nSecond line.')
print('C:\this\name')
print(r'C:\this\name')
print()

# string literals are like [[]] in lua and can span multiple lines
print('''
Usage; thingy [OPTIONS]
  -h
  -H hostname
''')
print()

# strings can be concat'd with '+' and repeated with '*'
print(3 * 'un' + 'ium')

# two or more string literals next to each other are automatically concatenated
print('py'    'thon')
# even with breaking up long strings
print('Put several strings within parentheses '
'to have them joined together.') # only works with literals

print()

# in python there are no characters, just strings of size one
word = 'Python'
print(word[0])
print(word[5])
print()

# neg indices start from the end
print(word[-1])
print(word[-2])
print(word[-6])

# -0 is the same as 0, so negs indexes start with -1 not -0
print(word[-0])
print()

# slicing is also supported to get substrings
print(word[0:2])
print(word[2:5])
print()

# slice indices defaults when omitting first, second, or both indexes
print(word[:2])
print(word[4:])
print(word[-2:])
print(word[:])
print()

print(word[:2]+word[2:])
print(word[:4] + word[4:])
print()

# out of range index throw errors, but with ranges they are simply returned as ''
# print(word[42])
print(word[4:42])
print(word[42:])

# python strings are immutable
# word[0] = 'J' # Error 'str' object doesn't support item assignment

# we need to create a new one
print('J' + word[1:])
print(word[:2] + 'py')

# built-in function len() returns the length of a string
s = 'supercalifragilisticexpialidocious'
print(len(s))

# 3.1.3 LISTS






