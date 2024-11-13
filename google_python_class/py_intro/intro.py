## a lot of the following you can put right into the interpreter
## Python is a great lang for testing and seeing how things work interactively
## Python is dynamic, interpreted (bytecode-compiled). There are no type 
## declarations of vars, params, funcs or methods. Its a compromise because
## while its easier, code is short and flexible, we lose the compile-time checks
## Python does track types of all values at runtime and flags code that
## doesn't make sense as it runs.

## as mentioned an excellent way to see how py works is tor un it on the 
## interpreter. We can answer most questions just doing that. For example:

## I've run the following right in the interepreter, though I'm documenting
## it here 

## set a var and print it
a = 6
print(a)

# then we can use that var in other expressions
print(a+2)

# 'a' can hold other things as well since py is dyanmic
a = 'hi'
print(a)

# call the builtin len() function on a string
print(len(a))

# let's try something that doesn't work
# print(a + len(a)) # this gives us a TypeError: can only concatenate str (not "int") to str
# we need to then comment this
# out, since py executes top to bottom, it won't go any further until we
# deal with this error

# but we can do this
print(a + str(len(a)))

# here is something else that errors our. 
print(foo) # NameError: name 'foo' is not defined.

# then we get out of the interepreter with either ^d or 'quit()'

# Like C++ and Java, py is case sensitive so 'a' and 'A' are different vars
# The end of the line marks the end of a statement, so unlike C++ and Java
# py doesn't require a semicolon at the end of each statement. Comments, as
# seen above begin with '#' and extend to the end of the current line.