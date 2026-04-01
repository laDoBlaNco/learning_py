# infinite.py

# “Infinite iterators
# Infinite iterators allow you to use a for loop
# as an infinite loop, iterating over a sequence
# that never ends

from itertools import count

for n in count(5, 3):
    if n > 20:
        break
    print(n, end=", ")  # instead of newline on end
    # we use a comma


# The count factory class makes an iterator that
# simply goes on and on counting. In this example,
# it starts from 5 and keeps adding 3 at every
# iteration. We need to break it manually if we
# do not want to get stuck in an infinite loop.
