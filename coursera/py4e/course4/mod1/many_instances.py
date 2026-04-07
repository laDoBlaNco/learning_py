# many_instances.py

# MANY INSTANCES
#
#   • We can create lots of objects - the class is the template for the obj
#   • We can store each distinct object in its own variable
#   • We call this having multiple instances of the same class
#   • Each instance has its own copy of the instance variables

class PartyAnimal:
    def __init__(self,z):
        self.x = 0
        self.name = z
        print(self.name,'constructed')

    def party(self):
        self.x += 1
        print(self.name,'party count',self.x)


s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")
j.party()
s.party()

# Constructors can have additional parameters. These can be used to set up
# instance  variables for the particular instance of the class (i.e., for the
# particular object)

