# key.points.assignment.py

# ASSIGNMENT TO PARAMETER NAMES - our second key point
# (assigning an object to an argument name inside a function 
# does not impact the caller)

x=3

def func(x):
    x=7 #defining a local x, not changing the global one  # noqa: F841

func(x)
print(x)

# calling the function func(x), the instruction x=7 is executed within the
# local scope for the func() function; the name x is pointed to an integer
# with a value of 7, leaving the global x unaltered or in other words
# leaving the caller unimpacted.


