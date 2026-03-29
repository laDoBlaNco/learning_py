# using a while loop to find the binary rep
# of an int
n = 39
remainders = []

while n > 0:
    remainder = n % 2
    remainders.append(remainder)
    n //= 2

remainders.reverse()
print(remainders)

# it works but lets make it more pythonic
# with divmod()
