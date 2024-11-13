#!/usr/bin/python3

# Note the alignment of the indentation here. Its important as that's the way
# py knows what lines go in what block

# Defines a 'repeat' function that takes 2 args
def repeat(s,exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use 's * 3' which is faster (why?)
    # becasue '+' must be called 3 times, and '*' only once
    if exclaim:
        # again notice the grouping by indentation
        result = result + '!!!'
    return result 


# both + and * are called 'overloaded' operators because they mean different 
# things for numbers vs strings
# 'def' kw is for defining functions (and as we'll see later 'fn' in mojo)
# The first line of a function can be a documentation string. it can be one
# line or we can use ''' or """ for a multiline string.

# here we have the use of that function above

def main():
    print(repeat('Yay',False))  # YayYayYay
    print(repeat('Woo Hoo',True)) # Woo HooWoo HooWoo Hoo!!!

if __name__=='__main__':
    main()



# Indentation - One usual Python feature is that the whitespace indentation
# of a piece of code affets its meaning. A logical block of statements such
# as the ones that make up a function should all have the same indentation,
# set in from the identation of their parent function or 'if' or whatever.
# If one of of the lines in the group has a different indentation, it is
# flagged as a syntax error.

# this use of whitespace feels a little strange at first, and I an attest
# to that when I was trying to learning Python with Ruby back in the early
# 2000s. But it gets very easy very quickly and is very untuitive. Always
# use spaces instead of 'Tabs' as Tabs are different in different systems.

# A common question has always been, how many spaces per for indentation, 
# 2 4 or even 8. The official style guide (PEP8) says 4, but interestingly
# Google's internal guideline is 2. So if its good enough for Google, 
# its good enough for ladoblanco :)