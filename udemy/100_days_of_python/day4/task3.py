# task3.py
import random
# Banker Roulette
# Figure out how to pick a random name from the list
friends = ['Alice','Bob','Charlie','David','Emmanuel']

print(friends[random.randint(0,len(friends)-1)])  # my way

print(random.choice(friends)) # Angela's way from python random doc


