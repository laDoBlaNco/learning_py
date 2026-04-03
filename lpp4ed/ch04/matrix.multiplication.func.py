# matrix.multiplication.func.py

# This is much easier right?
def matrix_mul(a,b):
    return [[sum(i*j for i,j in zip(r,c)) for c in zip(*b)] for r in a]
    # still don't understand this, but if I was using the func, I wouldn't
    # need to understand it.

a = [[1,2],[3,4]]
b = [[5,1],[2,1]]
c = matrix_mul(a,b)
print(c)

# readability is improved
