# task1.py

# Dictionaries & Nesting
# allow us to group together and tag related information
# Key : Value pairs

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

# retrieving an item. kinda like a list with []s
print(programming_dictionary["Loop"])
# print(programming_dictionary['Lop']) # KeyError: "Lop"

# adding something to the dictionary also with []
programming_dictionary["Python"] = "The best programming language EVER!"
print(programming_dictionary)
print()

# Wipe a dictionary
# programming_dictionary = {}
# print(programming_dictionary)
# print()

# edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)
print()

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing) # keys

print()

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

print()


