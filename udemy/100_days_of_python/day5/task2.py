# task2.py

#  Highest score
# Sum
# Python has lots of built-in functions to help us work with numbers. One of them helps us
# calculate the sum, but how does it work behind the scenes

student_scores = [
    72,
    96,
    86,
    98,
    86,
    82,
    78,
    92,
    88,
    71,
    70,
    79,
    81,
    83,
    100,
    99,
    92,
    72,
    95,
    85,
    84,
    86,
    77,
    81,
    96,
    95,
    88,
    98,
    87,
    80,
    88,
    72,
    82,
    80,
    79,
    74,
    91,
    75,
    89,
    96,
    88,
    86,
    100,
    87,
    94,
    94,
    97,
    77,
    78,
    94,
    81,
    94,
    70,
    77,
    75,
    76,
    92,
    83,
    74,
    83,
    70,
    77,
    71,
    70,
    75,
    87,
    70,
    90,
    95,
    97,
    76,
    77,
    80,
    79,
    81,
    95,
    71,
    85,
    79,
    85,
    75,
    92,
    71,
    91,
    74,
    73,
    80,
    78,
    90,
    76,
    96,
    99,
    83,
    88,
    71,
    73,
    76,
    74,
    85,
    70,
]

print("Count:", len(student_scores))
print("Python Sum:", sum(student_scores))

my_sum = 0
for score in student_scores:
    my_sum += score
print('My Sum:',sum)
print()

print('Python Max:',max(student_scores))

my_max = 0
for score in student_scores:
    if score > my_max:
        my_max = score

print('My Max:',my_max)