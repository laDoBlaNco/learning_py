# task1.py
# Randomisation and lists

# Ramdom module
# Ramdon whole numbers within a range
import random

# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)
# print()

# print(my_module.my_favorit_number)

# random.random() - generates a psuedo-random number 0 <= x < 1 non-inclusive (semi-open)
random_number_0_to_1 = random.random() * 10 # 0 <= x < 10
print(random_number_0_to_1)

random_float = random.uniform(1,10) # 0 <= x <= 10
print(random_float)
print()


# Create a heads or tails program
# coin = int(random.random()+.5) # my version, but Angela's was cleaner using .randint(0,1)
# inclusive int of 0 or 1
coin = random.randint(0,1)
if coin == 0:
    print('heads')
else:
    print('tails')
