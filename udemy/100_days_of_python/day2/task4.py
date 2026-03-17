#task4.py

bmi = 84/1.65**2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi,2))
print()

# acumulator assignment
score = 0
print(score)
score+=1
print(score)
score+=1
print(score)
print()

# f-strings
print('Your score is ' + str(score))

height = 1.8
is_winner = True

# so fstrings in python is interpolation in other languages. nice
print(f'Your score is = {score}, your height is {height}. You are winning is{is_winner}')

