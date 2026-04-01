# permutation.py

# Combinatoric generators

# A permutation, also called an “arrangement
# number” or “order,” is a rearrangement of the
# elements of an ordered list S into a one-to-one
# correspondence with S itself

from itertools import permutations

perms = list(permutations("abc"))
print(perms)
print(len(perms))

# Summary
# In this chapter, we have taken another step
# toward expanding our Python vocabulary. We have
# seen how to drive the execution of code by
# evaluating conditions, along with how to loop and
# iterate over sequences and collections of
# objects. This gives us the power to control what
# happens when our code is run, which means we get
# an idea of how to shape it so that it does what
# we want, having it react to data that changes
# dynamically.

# We have also seen how to combine everything
# together in a couple of simple examples, and
# finally, we took a brief look at the itertools
# module, which is full of interesting iterators
# that can enrich our abilities with Python to a
# greater degree.
#
# Now, it is time to switch gears, take another
# step forward, and talk about functions. The next
# chapter is all about them, and they are extremely
# important. Make sure you are comfortable with
# what has been covered so far. We want to provide
# you with interesting examples, so let’s go.
#
