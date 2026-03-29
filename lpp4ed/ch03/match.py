# match.py

day_number = 4

match day_number:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print(f"{day_number} is not a valid day number")
print()
print()
# also adding some examples from match pep 636 tutorial

command = input("What are you doing next")
match command.split():
    case [action]:  # note no meed for break here
        ...
    case [action, obj]:
        ...

# matching specific values rather than assigning variables
match command.split():
    case ["Quit"]:
        print("Goodbye")
    case ["look"]:
        ...
    case ["get", object]:  # specific value and assignment
        # here we only match a 2-element sequence and
        # the first must be equal to 'get' while the second
        # subject[1] will be bound to obj
        ...
    case ["go", direction]:
        # we can also ise different vars in diff patterns
        ...
    case ["drop",*objects]: # extended sequence unpacking
        for obj in objects:
            ...
        # match any sequences having “drop” as its first 
        # elements. All remaining elements will be 
        # captured in a list object which will be 
        # bound to the objects variable.
    case _:
        print(f"Sorry I couldn't understand {command!r}")
        # NOTE: adding the !r in the string forces python to use 
        # the repr version meaning we get 'command' rather 
        # than just command
        
# there is a lot more to this but more than I want to
# type here. ill come back to it on the laptop. but
# pattern-matching in python is powerful
