# first_class.py


class PartyAnimal:  # class is a reserved word that defines the template
    def __init__(self):  # When an object is constructed a specially named
        # method is called to allocate and initialize attributes
        # like the "constructor" in other languages like Dart
        self.x = 0

    # each PartyAnimal object has a bit of code (method = function in class)
    def party(self):
        self.x += 1
        print(f"So far {self.x}")

# Construct a PartAnimal object with 'PartyAnimal()' and store
# in 'an'
an = PartyAnimal()

# tell the an object/instance to run the party() code
an.party()
an.party()
an.party()
print(an.x) # an.x is our self.x (self is an)
PartyAnimal.party(an) # this is the same thing its doing
print()

# playing with dir() and type()
print(f"Type: {type(an)}")
print(f"Dir: {dir(an)}")
print(f"Type: {type(an.x)}")
print(f"Type: {type(an.party)}")
