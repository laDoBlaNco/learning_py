# task5.py

# Write a pizza delivery program. You've got a job at Python Pizza. Our first task
# is to build an automatic pizza order program.

# Based on user order, work out their final bill. use the input() function to get a user's
# preferences and then add up the total for their order and tell them how much they have
# to pay.

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or Large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# TODO: work out how much they need to pay based on their size choice
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# TODO: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# TODO: work out their final amount based on whether they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
