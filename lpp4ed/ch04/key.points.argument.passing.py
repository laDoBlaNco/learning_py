# key.points.argument.passing.py

# INPUT PARAMETERS - Key Points
# 
# • Argument-passing is nothing more than assigning an object to a local
#   variable name
# • Assigning an object to an argument name inside a function does not affect
#   the caller
# • Changing a mutable object argument in a function does affect the caller
# 
# • Python documentation:
#       Parameters are defined by the names that appear in a function 
#       definition, whereas arguments are the values actually passed to a
#       function when calling it. Parameters define what types of arguments
#       a function can accept.

# ARGUMENT-PASSING - the first key point
# (nothing more than assigning an object to a local variable name)

x = 3 
def func(y):
    print(y)

func(x)

# so in a nutshell, what really happens is that the function creates, in its
# local scope, the names defined as parameters and, when we call it, we tell
# Python which objects those names must be pointing toward.
