# menu.no.walrus.py

"""
In interactive scripts, we often need to ask a user to choose between a
number of options. For example, suppose we are writing an interactive script
that allows customers at an ice cream shop to choose what flavor they want.
To avoid confusion when preparing orders, we want to ensure that the user
chooses one of the available flavors. Without the walrus, we might have to
write something like the following:
"""

flavors = ["pistachio", "malaga", "vanilla", "chocolate"]
prompt = "Choose your flavor: "
print(flavors)

while True:
    choice = input(prompt)
    if choice in flavors:
        break
    print((f"Sorry, '{choice}' is not a valid option"))
print(f"You chose '{choice}'.")

"""
Note the condition on the loop: while True means "loop forever", which
is not what we want. We want to stop the loop when the user inputs a
valid flavor (choice in flavors). To achieve that, we have an if statement
and a break inside the loop. The logic to control the loop isn't immediately
obvious. Despite that, this is actually quite the common pattern when the
value needed to control the loop can only be obtained inside of the same.

How can we improve on this? menu.walrus.py
"""
