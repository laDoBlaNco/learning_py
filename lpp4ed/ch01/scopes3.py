# scopes3.py
# Local, Enclosing and Global

def enclosing_func():
    age = 13
    def local():
        # age doesn't belong to the scope defined by the local function
        # so python will keep looking into the next enclosing scope,
        # This time age is found in the enclosing scope
        print(age,'printing from the local scope')

    local()

age = 5
print(age, 'printing from the global scopes')
enclosing_func()

