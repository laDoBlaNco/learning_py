# but if we want to work with the tuple directly
# in the body, we can simply not unpack it by giving
# only one var to assign

people = ["Kevin", "Odalis", "Kelen", "Xavi"]
ages = [49, 50, 19, 16]
instruments = ["Drums", "Keyboards", "Bass", "Guitar"]

for all_data in zip(people, ages, instruments):
    print(all_data)
