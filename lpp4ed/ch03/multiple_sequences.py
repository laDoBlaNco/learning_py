# Oyerating over multiple sequences
people = ["Kevin", "Odalis", "Kelen", "Xavi"]
ages = [49, 50, 19, 16]

for pos in range(len(people)):
    person = people[pos]
    age = ages[pos]
    print(person, age)

# “The code works, but it is not very Pythonic.
# It is cumbersome to have to get the length
# of people, construct a range, and then
# iterate over that. For some data structures,
# it may also be expensive to retrieve items by
# their position. It would be better if we could
# iterate over the sequences directly, as we do
# for a single sequence. Let us try to improve it
# by using enumerate():”
