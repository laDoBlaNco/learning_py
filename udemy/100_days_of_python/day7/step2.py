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

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
placeholder = '_' * len(chosen_word)
display = list(placeholder)
print(chosen_word)
print(placeholder)
print()


guess = input("Guess a letter: ").lower()
correct = guess in chosen_word

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i]=guess


print(''.join(display))


# print("Right") if correct else print("Wrong")
