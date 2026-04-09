# key.points.mutable.py

# CHANGING A MUTABLE OBJECT - our 3rd key point
# (changing a mutable object argument in a function DOES impact the caller)
# This is similar to what I learned in languages like Go. This is important
# because although Python appears to behave differently with mutable objects
# the behavior is, in fact, perfectly consistent.

x = [1,2,3]

def func(x):
    x[1] = 42 # this does in fact affect the 'x' argument (caller)

func(x)
print(x)

# so here we changed the original object. There is nothing strange about this
# behavior. When we call func(x), name x in the function's namespace is set 
# to point to the same object as global x. Within the body of the function, we
# are not changing the global x, that that we are not changing which object
# it points to. We are merely accessing the element at position 1 in that 
# object and changing that value. Compared to "Assigning an object to a 
# parameter not affecting the caller", this should make sense:

x = [1,2,3]
def func2(x):
    x[1]=42 # this changes the original 'x' argument!
    x = 'something else' # while this points LOCAL x to a NEW STRING OBJECT

func2(x)
print(x) # still [1,42,3]

