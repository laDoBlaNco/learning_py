#!/usr/bin/python3

#import modules use here -- sys is a very common one for working with your
# your system
import sys

# gathering our code into a main() function, though this isn't needed for all
# scripts, its a good practice.
def main():
    print('Hello there',sys.argv[1])
    # command line args are in sys.argv[1], sys.argv[2], ...
    # sys.argv[0] will always be the script itself being run which is why 
    # above we start with sys.argv[1]

# standard boilerplate to call the main() function to begin the program
# The 'if __name__ == '__main__': has to do with whether or not we are 
# using the interpreter or importing, vs simply running the program
if __name__ == '__main__':
    main()



# py source files use the .py ext and are called 'modules' With a py module
# the easiest way to rn it is with the shell command 
# python3 hello.py or
# py3 hello.py  (depending on your environment) or
# py hello.py

# You can also add args in the shell. The interpreter will execute the
# code in the module, passing it the args you pass it, for example:
# py hello.py Kevin

# note also that in py the blocks of code are delimited with identation rather
# than curly braces.

# As hinted above, when a module is run directly, the special var __name__ is
# set to __main__, therefore the last line 'if __name__=='__main__' will then
# run main(). but when the module is imported, main isn't run. Its simple goes
# through top to bottom setting all the vars and functions.
