# task1.py

# LOCAL SCOPE
# 
# Varibles declared inside functions have local scope. They are only seen
# by other code within the same block of code. 

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # NameError: name 'potion_strength' is not defined

# Global scope
player_health = 10

def drink_potion2():
    potion_strength = 2
    print(player_health,potion_strength) # global variable available

drink_potion2()

