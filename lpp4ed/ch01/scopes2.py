# scopes2.py
# Local versus global
def local():
    # age doesn't belong to the scope defined by the local function
    # so Python will keep looking into the next enclosing scope.
    # age is finally found in in the global scope
    print(age,'printing from the local scope')

age = 5
print(age, 'printing from the global scope')
local()
