# task2.py


# Multiple inputs. We can have multiple inputs in functions. All we need to do is separate
# the params with ','s - These are 'positional arguments'

def greet_with_name(nam: str):
    print(f"Hello {nam}")
    print(f"How do you do {nam}")


greet_with_name("Kevin")
print()

def greet_with(name:str,location:str):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Odalis","Santo Domingo")
print()

# keyword arguments, simply add '=' to the args and the order doesn't matter
greet_with(location='Santo Domingo',name='Kevin')
print()




