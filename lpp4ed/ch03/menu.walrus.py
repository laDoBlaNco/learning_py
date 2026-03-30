# menu.walrus.py

# We can improve on this with the walrus aperator
flavors = ['pistachio','malaga','vanilla','chocolate']
prompt = 'Choose your flavor: '
print(flavors)

while(choice:=input(prompt)) not in flavors:
    print(f"Sorry, '{choice}' is not a valid option.")
print(f"You chose '{choice}'.")

# Note the loop conditional now says exactly what we want. That is much 
# easier to understand. The code is also three line shorter than it was. 
# NOTE: The ()s around the assignment expression in this example is because
# the := operator has lower precedence than the 'not in' operator. 
# 
# The walrus operator is also useful in lambda expressions as well as 
# comprehensions and generators
# 
# A WORD OF WARNING
# 
# The introduction of the := in python as been somewhat contraversial. Some 
# people featd that it would make it too easy to write ugly, non-pythonic 
# code, but this isn't entirely justified. The walrus operator can improve
# code and make it easier to read. Like any powerful feature, it can, however
# be abused to write obfuscated code. We should use it only when we need to.
# Let's put it all together.