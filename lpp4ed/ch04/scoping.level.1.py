# scoping.level.1.py


def my_function():
    #    test = 1  # defined in local scope
    print("my_function:", test)


test = 0  # this is defined in global scope

my_function()
print("global scope:", test)

# It is clear that test = 1 shadows the
# test = 0 assignment in my_function(). In
# the global context, test is still 0, as
# you can see from the output of the program,
# but we define the test name again in the
# function body, and we set it to point to
# the integer 1. Both of the test names
# therefore exist: one in the global scope,
# pointing to an int object with a value
# of 0, and the other in the my_function()
# scope, pointing to an int object with a
# values of 1. Note what happens whem we comment
# out the inner test? LEGB
