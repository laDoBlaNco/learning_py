# iterating over multiple sequences
# a more pythonic way with enumerate
people = ["Kevin", "Odalis", "Kelen", "Xavi"]
ages = [49, 50, 19, 16]

for pos, person in enumerate(people):
    age = ages[pos]
    print(person, age)

# “better, but still not perfect. We are iterating
# properly on people, but we are still fetching
# age using positional indexing, which we want to
# lose as well. We can achieve that by using the
# zip() function, which we encountered in the
# previous chapter. Let us use it:”
