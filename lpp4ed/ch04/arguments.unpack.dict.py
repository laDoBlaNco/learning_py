# arguments.unpack.dict.py

# Dictionary unpacking is to keyword arguments what iterable unpacking is to
# positional arguments. We use the **dictionary_name to pass keyword args,
# (I remember this from when I first learned Python and it was one of the
# tough concepts for me to get at that time) constructed from the keys and 
# values of a dictionary, to a function:

def func(a,b,c):
    print(a,b,c)

vals = {'b':1,'c':2,'a':42}

func(**vals)

