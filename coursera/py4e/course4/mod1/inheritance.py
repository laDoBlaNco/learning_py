# inheritance.py

# INHERITANCE
#
#   • We can make a new class or we can reuse an existing class and INHERIT
#     all the capabilities of an existing class and then add our own little
#     bit to make our new class
#   • Another form of store and reuse
#   • Write once - reuse many times
#   • The new class (child) has all the capabilities of the old class (parent)
#     and then some more.


# TERMINOLOGY: INHERITANCE
#
# 'Subclasses' are more specialized versions of a class, which inherit
# attributes and behaviors from their parent classes, and can introduce
# their own.


class PartyAnimal:
    def __init__(self, name):
        self.x = 0
        self.name = name
        print(f"{self.name} constructed")

    def party(self):
        self.x += 1
        print(f"{self.name} party count {self.x}")

class FootballFan(PartyAnimal): # subclassing easier than Dart 🤔
    def __init__(self,name):
        super().__init__(name)
        self.points = 0

    def touchdown(self):
        self.points+=7
        self.party()
        print(f"{self.name} points {self.points}")

s = PartyAnimal('Sally')
s.party()
print()


j = FootballFan('Jim')
j.party()
j.touchdown()

# DEFINITIONS
# 
# Class - a template
# Attribute - A variable within a class
# Method - An associated function within a class
# Object/instance - A particular instance of a class
# Constructor - Code that runs when an object is created
# Inheritance - The ability to extend a class to amek a new class.

#  SUMMARY
#   • Object Oriented Programming (OOP) is a very structured approach to
#     code reuse
#   • We can group data and funtionality together and create many independent
#     instances of a class