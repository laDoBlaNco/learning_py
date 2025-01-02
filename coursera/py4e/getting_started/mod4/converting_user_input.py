# If we want to read a number from the user, we must convert it
# from a string to a number using a type conversion function
# Later we will deal with bad input data

# Convert elevator floors
inp = input('Europe floor? ')
usf = int(inp)+1
print('US floor:',usf)