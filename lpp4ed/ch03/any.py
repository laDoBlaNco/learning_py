# any.py

# using break
items = [0, None, 0.0, True, 0, 7] # true and 7 evauate to True
found = False # this is called a 'flag'

for item in items:
    print("scanning item",item)
    if item:
        found = True # we update the flag
        break

if found: # we inspect the flag
    print("At least one item evaluates to True")
else:
    print("All items evaluate to False")

'''
There is no need to write code to detect whether there is at least
oen element in a sequence that evaluates to True, as the built-in
function any() does exactly this.
'''
