# parameters.default.py

# DEFINING PARAMETERS

# function params can be classified into five groups:
#   • Positional or keyword parameters: allow both positional and keyword args
#   • Variable  positional params: collect an arbitrary number of positional
#     arguments in a tuple
#   • Variable keyword params: collect an arbitrary number of keyword args in
#     a dict
#   • Positional-only parameters: can only be passed as positional args
#   • Keyword-only params: can only be passed as keyword arguments

# Optional parameters: in addition to the above params can be classified as
# required or optional. Optional params have a default value specified in the
# function definition. The syntax is name=value

def func(a,b=4,c=88): # a is required while b,c have defaults, easy enough
    print(a,b,c)

func(1)
func(b=5,a=7,c=9)
func(42,c=9)
func(42,43,44)
