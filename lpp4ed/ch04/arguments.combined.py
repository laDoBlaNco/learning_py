# arguments.combined.py

# We have already seen that positional and kw args can be used together,
# as long as they are passed in the right order. We can also combine unpacking
# (of both kinds) with normal positional and kw args. We can even combine
# unpacking multiple iterables and dictionaries. 

# Arguments must be passed in the following order:
#   • first, positional arguments: both ordinary (name) and iterable unpacking
#     (*name)
#   • Next come keyword arguments (name=value), which can be mixed with 
#     iterable unpacking (*name)
#   • Finally, there is dictionary unpacking (**name), which can be  mixed with
#     keyword arguments (name=value)

def func(a,b,c,d,e,f):
    print(a,b,c,d,e,f)

func(1,*(2,3),f=6,*(4,5))
func(*(1,2),e=5,*(3,4),f=6)
func(1,**{'b':2,'c':3},d=4,**{'e':5,'f':6}) # its **{k:v} not **kwarg as I thought
# o sea **kwarg means kwarg is a dict
func(c=3,*(1,2),**{"d":4},e=5,**{'f':6,})
# func(c=3,**{'f':6,},*(1,2),**{"d":4},e=5) SyntaxError: iterable arg unpacking follows keyword argument unpacking

# All of the above calls to func() are equivalent and print 1 2 3 4 5 6. 