# scoping.level.2.py


def outer():
    test = 1  # outer scope

    def inner():
        nonlocal test
        test = 2  # now its the nearest non-
        # closing scope which alters outer
        print("inner:", test)

    inner()
    print("outer:", test)


test = 0  # global scope
outer()
print("global:", test)

# We can get read access to those names if we
# use them in a nested scope that does not
# define them, but we cannot modify them
# because when we write an assignment
# instruction, we are actually defining a
# new name in the current scope.
#
# We can use the nonlocal statement to
# change this behavior. According to the
# official documentation:
#
#      ”The nonlocal statement causes the
#      listed identifiers to refer to
#      previously bound variables in the
#      nearest enclosing scope excluding
#      globals.”
#

# If we removed the nonlocal test line from
# the inner() function and tried it inside
# the outer() function, we would get a
# SyntaxError, because “the nonlocal
# statement works on enclosing scopes, but
# not in the global one.” To get to the global
# one we ise the global statement
#
