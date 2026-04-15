#  arguments.unpack.iterable.py

# Iterable unpacking uses the syntax *iterable_name to pass elements of
# an iterable as positional arguments (similar to '...' in other langs?🤔)


def func(a, b, c):
    print(a, b, c)


vals = 1, 3, -7

func(*vals)

# This is very useful, particularly when we need to programtically generate
# arguments for a function.
