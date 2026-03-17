# task4.py

# Final project of the day
# PyPassword Generator
import random

letters = [chr(n) for n in range(65, 91)] + [chr(n) for n in range(97, 123)]
numbers = [chr(n) for n in range(48, 58)]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

gen_password_list = (
    random.choices(letters, k=nr_letters)
    + random.choices(symbols, k=nr_symbols)
    + random.choices(numbers, k=nr_numbers)
)

# print(gen_password_list)
random.shuffle(gen_password_list)
print('Your new password is: ',''.join(gen_password_list))