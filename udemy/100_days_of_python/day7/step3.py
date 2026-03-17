# step1.py

# Flowchart programming - drawing out the logic of your project.
# https://drive.google.com/file/d/1XyGGNGGiEvN0kW8mPmSZkkEJWN4zbpWr/view?usp=drive_link
import random


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen word. Print "Right" if it is,
#   "Wrong" if it's not

# TODO-4 - Create an empty String called placeholder and for each letter in the chosen_word, add a '_'
#   to placeholder

# TODO-5 - Create an empty string called display by looping through each letter in the chosen_word.
#   if the position matches guess then reveal that letter in the display version at that position.

# TODO-6 - use a while loop to let the user guess again. The should only stop once the user has
#   guessed all the letters in teh chosen_word. At that point display has no more blanks. And the
#   user has won.

# TODO-7 - Update the for loop so that previous guesses are added to the display string. At the 
#   moment when the user makes a new guess, the previous guess gets replaced by "-". We need to
#   fix that by updating the for loop. This doesn't really impact me since I'm using a list
#   instead of Angela's solution. So my solution is mutable.

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
placeholder = "_" * len(chosen_word)
print(chosen_word)
print(placeholder)
print()

game_over = False
correct_letters:list[str] = [] # my first type annotation in python for the Black type checker

while not game_over:
    guess = input("Guess a letter: ").lower()
    # correct = guess in chosen_word
    display=''

    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'

    print("".join(display))

    game_over = True if '_' not in display else False


# print("Right") if correct else print("Wrong")
