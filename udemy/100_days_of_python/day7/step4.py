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

# TODO-8 - Create a variable lives to keep track of the number of lives left. Set lives to
# equal 6

# TODO-9 - if guess is not a letter in the chosen_word then reduce lives by 1
#   If lives goes down to 0, then the game should end and should print 'YOU LOSE!'

# TODO-10 - print the ascii art from the list stages that corresponds to the current number of
#   lives the user has remaining

stages:list[str] = ['''
  +---+
  |   |
  O   |
 /|\  |  
 / \  |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========
''', '''
  +---+
  |   |
      |
      |
      |
      |
========

''']





word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
placeholder = "_" * len(chosen_word)
print(chosen_word)
print(placeholder)
print()

game_over = False
correct_letters: list[str] = (
    []
)  # my first type annotation in python for the Black type checker

while not game_over:
    guess = input("Guess a letter: ").lower()
    # correct = guess in chosen_word
    display = ""
    
    if guess not in chosen_word:
      lives-=1


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("".join(display))

    if "_" not in display:
      game_over = True
      print('YOU WIN!')
    elif lives == 0:
      game_over = True
      print('YOU LOSE!')

    print(stages[lives])

# print("Right") if correct else print("Wrong")
