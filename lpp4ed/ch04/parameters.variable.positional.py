# parameters.variable.positional.py

# sometimes we might not want to specify the exact number of positional params
# so we can do variable positional params.
def minimum(*n):
    print(type(n))  # is a tuple
    if n:  # explained after the code
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum(1, 3, -7, 9)
minimum()

# so defining a param with an * (not to be confused with using an arg with
# an *), prepended to its name, we are telling py that this parameter will
# collect a variable number of positional arguments. So this is the ..., not
# what I put in a script earlier.

# NOTE: a function can have at most ONE variable positional parameter -- it
# wouldn't make sense to have more than 1. Py would have no way of dividing
# them up between the two. There is also no default for a variable positional
# parameter. The default is always an empty ()

# NOTE: Another key note. Note the 'if n:' in the code above? We are checking
# whether n is empty here. This works since collection objects (including str)
# evaluate to True when non-empty, and otherwise False, in py. This is the case
# for tuples, sets, lists, dicts, etc.

# NOTE: One last note as mentioned early, the syntax for defining variable
# parameters looks a lot like the syntax for iterable unpacking. (which has
# confused me before) This is no coincidence. After all, teh two features
# mirror each other. They are also frequently used together, since variable
# positional params save us from worrying about whether the length of the
# iterable we are unpacking matches the number of params in the function def.
