# with divmod
n = 39
remainders = []

while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)

remainders.reverse()
print(remainders)

# it works but lets make it more pythonic
# with divmod()
