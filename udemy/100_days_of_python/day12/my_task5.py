# task5.py - final project
import art
import random

# Final Projecgt - Guessing game

print(art.logo)
print()

num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 10 if difficulty == "easy" else 5

for n in range(attempts, 0, -1): # interesting, the 1 isn't inclusive regardless
    # if we are going down from 10 to 1. Need to change to 10,0
    print(f"You have {n} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    if len(guess) < 1:
        print("You wasted an attempt. Please enter a numerical guess.")
        continue  
    guess = int(guess)  
    if guess == num:
        print(f"You got it! The answer was {num}")
        break
    elif guess < num:
        print("Too low.")
    else:
        print("Too high.")

    print("Guess again.")
print("You've run out of guesses, you lose.")