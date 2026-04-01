# task2.py
# BLOCK SCOPE
# 
# python is a bit different from other programming languages in that
# it does not hae block scope. 
# 
# This means that variables created nested in other blocks of code e.g.
# for loops, if statements, while loops etc, don't get local scope.
# They are given function scope if they are in a function or global scope
# if they are not.

game_level = 3
enemies = ["Skeleton","Zombie","Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


