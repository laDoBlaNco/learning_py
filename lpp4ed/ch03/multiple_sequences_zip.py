# iterating over multiple sequences in n an even
# more pythonic way with zip
people = ["Kevin", "Odalis", "Kelen", "Xavi"]
ages = [49, 50, 19, 16]

for person, age in zip(people, ages):
    print(person, age)

# even more elegant. zip zips them up and delivers to
# for in a 2-tuple which is unpacked to our vars

# now more on this unpacking…
