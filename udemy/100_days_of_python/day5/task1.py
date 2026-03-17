# task1.py

# For loops, Ranges, and code blocks

# using for loops on python lists
# for Loops:
# Loops allow us to tell the computer to repeat actions  without having to write repeated code.
# If we wanted the computer to print out  1 through 100, it would be very painful to type a print
# statement for every number, or even just typing out all the numbers 1 through 100. Loops allow
# us to create a rule and the computer can follow it to do a repeated action.

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: # after the colon the indents are "inside" the construct
    print(fruit)    # the block is everything indented to the same level here
    print(fruit,'pie')
    # print(fruits) # inside the loop
print(fruits) # outside the loop

