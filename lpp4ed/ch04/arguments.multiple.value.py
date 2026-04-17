# arguments.multiple.value.py

# when we combine positional and keyward args, we must remember that each param
# can only appear once in the arg list:

def func(a,b,c):
    print(a,b,c)

func(2,3,a=1)

# here we pass two values for a: the positional arg and the keyword a=1. This
# results in a TypeError: func() got multiple values for argument 'a'

# now let's look at defining parameters after focusing on the args given
# to our functions.