# parameter.variable.keyword.py

# variable keyword parameters are very similar to variable positional params.
# The only difference is the syntax (**instead of *) and the fact that they
# are collected in a dict


def func(**kwargs):
    print(kwargs)


func(a=1, b=24)
func()
func(a=1, b=46, c=99)

# As seen here we are adding ** in front of the parameter name in the function
# definition which tells py to use the name to collect a variable number of
# keyword parameters. As in the case of variable positional parameters, each
# function can have at most one variable keyword parameter - and we can't
# specify a default value.
# Just like variable positional parameters resemble iterable unpacking, variable
# keyword parameters resemble dict unpacking. Dict unpacking is also often
# used to pass arguments to functions with variable keyword parameters.

# Though it might be as evident right now, this is very important. As we'll
# see in the next example - parameters.variable.db.py