# write a program to prompt the user for hours and rate per
# hour using input to compute gross pay. Pay the hourly rate for 
# the hours  up to 40 and 1.5 times the hourly rate for all hours 
# worked above 40 hours. Use 45 hours and a rate of 10.50
# per hour to test the program (the pay should be 498.75). You should
# input to read a string to a number. Do not worry about error checking
# the user input yet - assume the user types numbers properly

hrs = input('Enter Hours:')
rate = input('Enter the Rate:')
try:
  h = float(hrs)
  r = float(rate)
except:
  print("Error, please enter numeric input")
  quit()
if h<=40:
  print(r*h)
else:
  ot = h-40
  print((r*40)+(r*1.5*ot))