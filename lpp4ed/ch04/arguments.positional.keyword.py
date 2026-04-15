# arguments.positional.keyword.py

# we can also use both positional and keyword arguments at the same
# time:

def func(a,b,c):
    print(a,b,c)

func(42,b=1,c=2)

# we need to keep in mind that that positional args always have to be listed
# before any keyword args or we'll get a SyntaxError: positional argument follows keyword argument
