# obj_life_cycle.py

# OBJECT LIFE CYCLE
# 
#   • Objects are created, used and discarded
#   • We have special blocks of code (methods) that get called
#       • at the moment of creation (constructor)
#       • at the moment of destruction (destructor)
#   • Cosntructors are used a lot
#   • Destructors are not

# CONSTRUCTOR
# 
#   • The primary purpose of the constructor is to set up some instance
#     variables to have the proper initial values when the object is created
#   • in OOP a constructor in a class is a special block of statements called
#     when an object is created


class PartyAnimal:
    def __init__(self):
        self.x = 0
        print('I am constructed')

    def party(self):
        self.x+=1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed',self.x)

an= PartyAnimal()
an.party()
an.party()
an=42 # this is where our object is destructed
# del an # is the same thing as __del__ but called on an object 
print('an contains',an)

# Both the constuctor and destructor are optional. The constructor is 
# typically used to set up variables. The destructor is seldom used.

# MANY INSTANCES
# 
#   • We can create lots of objects - the class is the template for the obj
#   • We can store each distinct object in its own variable
#   • We call this having multiple instances of the same class
#   • Each instance has its own copy of the instance variables
