# to illustrate the point lets adapt one of our
# flr examples to while

people = ["Kevin", "Odalis", "Kelen", "Xavier"]
ages = [49, 50, 19, 16]
pos = 0

while pos < len(people):
    person = people[pos]
    age = ages[pos]
    print(person, age)
    pos += 1
