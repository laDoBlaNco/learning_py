# To generate the sequence of prime numbers, we
# will consider each natural number, starting from
# two, up to the limit, and test whether it is a
# prime. We will write two versions of this, the
# second of which will exploit the for...else
# syntax:

primes = []
upto = 100
for n in range(2, upto + 1):
    is_prime = True  # flag
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
print(primes)
