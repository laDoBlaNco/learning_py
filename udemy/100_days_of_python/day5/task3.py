# task3.py

# For loops with Range
# The combination of the range() function with the Python For loop allows us to runa  loop
# for as many times as we decide. Instead of looping through each item in a list, we can loop
# through a range of numbers.

for num in range(1, 11,2): # (a <= x < 10) also with optional step
    print(num)

print()

tot = 0
for num in range(1,101):
    tot+=num
print(tot)

