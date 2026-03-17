# task6.py
# multiple conditions and logical operators

# and, or, & not
# Age 45 to 55 modifier - udpate code so that people age 45 to 55 (inclusive of both) ride
# for free.

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age>=45 and age<=55:
    # simplified chain 'elif 45 <= age <= 55:' but harder to read for noobs
        print('Everything is going to be ok. Have a free ride on us!')
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input(
        "Do you want to have a photo taken? Type y for Yes and n for No: "
    )
    if wants_photo == "y":
        # add $3 to the bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you need to grow taller before you can ride.")
