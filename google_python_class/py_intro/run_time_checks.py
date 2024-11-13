#!/usr/bin/python3

# Defines a 'repeat' function that takes 2 args
def repeat(s,exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use 's * 3' which is faster (why?)
    # becasue '+' must be called 3 times, and '*' only once
    if exclaim:
        # again notice the grouping by indentation
        result = result + '!!!'
    return result 


def main():
    # name = 'Guido'
    name = 'Kevin' 

    if name == 'Guido':
        print(repeeeet(name,True))
    else:
        print(repeat(name,True)) 

if __name__=='__main__':
    main()

# py does very little checking at compile time (to bytecode), deferring almost
# all checking (type, name, etc) to runtime. For example, 

# These types of things are the compromise when using loosely type languages
# like python instead of strongly typed languages Java

# But in py3 we now have type hints, which allow us to indicate what the type
# is for each argument in a function as well as what the type is of the object
# returned by the function. For example:
# def is_positive(n:int)->bool:  Type hints are totally optional though. But
# with the use of type hints some editors like VS code can run checks to verify
# functions are called with the right arg types. 




