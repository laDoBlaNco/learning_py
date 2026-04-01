# We are not going to try to make this code
# more efficient from an algorithmic point of
# view. But let us use some of what we learned
# in this chapter to at least make it easier to
# read:
#

primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)

# “Using an else clause on the inner loop allows
# us to get rid of the is_prime flag. Instead,
# we append n to the primes list when we know that
# the inner loop has not encountered any break
# statements. It is only two lines shorter, but
# the code is simpler, cleaner, and reads better.
# This is important, as simplicity and readability
# count for a lot in programming. Always look for
# ways to simplify your code and make it easier
# to read.”
