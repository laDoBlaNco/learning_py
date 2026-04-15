# arguments.keywords.py

# Keyword arguments in a function call are assigned to parameters using the
# name=value syntax:

def func(a,b,c):
    print(a,b,c)

func(a=1,c=2,b=3)

# When using keyword arguments, the order of the arguments does not need to
# match the order of the parameters in the function def. This can make our 
# code easier to read and debug. We do not need to remember (or look up) the
# order of parameters in a function definition. We can look at a function call
# and immediately know which argument corresponds to which parameter. 