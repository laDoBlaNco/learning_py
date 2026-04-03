# matrix.multiplication.nofunc.py

# would you rather see this?
a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]
c = [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]
# i don't even know what this is doing 🤯🤯🤯
