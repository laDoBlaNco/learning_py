# task5.py
# Final project for the day
# Rock, Paper, Scissors
import random
import sys


# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

plays = [rock,paper, scissors]

player_play = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n '))
pc_play = random.randint(0,2)

if player_play > 2 or player_play < 0:
    print("That's not a valid option. You lose!")
    sys.exit()
elif player_play==2 and pc_play==0:
    res = 'You lose!'
elif player_play==0 and pc_play==2:
    res = 'You Win!'
elif player_play < pc_play:
    res = 'You Lose!'
elif player_play == pc_play:
    res = 'You tied!'
else:
    res = 'You Won!'

print(f'You chose: {player_play}')
print(plays[player_play])
print('Computer chose:')
print(plays[pc_play])
print(res)

