# write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Use 35 hours and a rate of 2.75 per hour to est the 
# program (the pay should be 96.25). You should use input to read a string 
# and float() to convert the string to a number. Do not worry about error 
# checking or bad user data.

hrs = float(input('Enter Hours: '))
pay_rate = float(input('Enter Rate of Pay: '))

print('Pay:',hrs*pay_rate)