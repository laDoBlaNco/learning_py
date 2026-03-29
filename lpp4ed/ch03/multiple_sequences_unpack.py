# unpacking

people = ["Kevin", "Odalis", "Kelen", "Xavi"]
ages = [49, 50, 19, 16]
instruments = ["Drums", "Keyboards", "Bass", "Guitar"]

for person, age, instrument in zip(people, ages, instruments):
    print(person, age, instrument)

# we now get a 3-tuple from zip and they are unpacked
# and assigned
