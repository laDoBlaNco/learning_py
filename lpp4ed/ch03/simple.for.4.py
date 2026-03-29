# iterating over a sequence (more pythonic way)
# when we still need the positions
# using enumerator
surnames = ["Whiteside", "Lorenzo", "Corporan"]

for pos, surname in enumerate(surnames):
    print(pos, surname)

print()
# an enumeration returns 2-tuple and of course
# tuples can be used in multiple assinments like
# pos, surname
print(list(enumerate(surnames)))
# or with a start arg
print(list(enumerate(surnames, 67)))


