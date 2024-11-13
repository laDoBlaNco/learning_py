# py has a built-in string class named 'str' with may handy features
# (there is an older module named 'string' which we shouldn't use). String
# literals can be enclosed by either double or single quotes, although
# single are more commonly used. Backslashes are used to escape. But a 
# double quoted string literal can contain single quotes and vice versa
# A string literal can span multiple lines, but only with a '\' at the end
# of each line to escape the newline. String literals with """ or ''' can
# span multiple lines with out the '\'

# Py strings are immutable which means they cannot be changed after they
# are created (Java strings also use this immutable style) 
# Since strings can't be changed, we construct new strings as we go to
# as we go to represent computed values. So for example the expression
# 'hello' + ' there' builds a new string

# Characters in a string can be accessed using the standard [] syntax and
# like Java and C++, py uses 0 based indexing.. If the index is out of bounds
# for the string, then we get an error raised. Py, unlke languages like Perl 
# and JS is to halt if it can't figure out what to do, rather than try to
# start to convert things continue. The handy 'slice' syntax also works to
# extract substrings. As we saw before len(string) will give us the length
# of the string. Py goes far to make sure there is consistency between different
# types, so both len() and [] work with any sequence type (strings,lists,tuples,etc)
# A py newbie gotcha: don't use len as a variable name to avoid blocking the len()
# function. The '+' operator can concatenate two strings as we've seen before. 

s = 'hi'
print(s[1])
print(len(s))
print(s + ' there')

# unlike java, the '+' doesn't automatically convert numbers or other types
# to a str form. We need to use the str() function to explicitly convert values
# so they can be combined with other strings.
pi = 3.14
# text = 'The value of pi is ' + pi # this doesn't work - TypeError: can only concatenate str (not 'float') to str
text = 'The value of pi is ' + str(pi)
print(text)



