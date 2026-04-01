# compress.py

# This iterator takes a sequence of data and a
# sequence of selectors, yielding only those
# values from the data sequence that correspond
# to True values in the selectors sequence. For
# example, compress("ABC", (1, 0, 1)) would give
# back "A" and "C" because they correspond to 1.
# Let us see a simple example:

from itertools import compress

data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

# Notice that odd_selector and even_selector are
# 20 elements in length, while data is only 10.
# compress() will stop as soon as data has
# yielded its last element
#
# Its is a fast and convenient way of selecting
# elements out of an iterable. The code is simple,
# but notice that instead of using a for loop to
# iterate over each value that is given back by
# the compress() calls, we used list(), which does
# the same, but instead of executing a body of
# instructions, it puts all the values into a
# list and returns it.

