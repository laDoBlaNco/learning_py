# walrus.if.py

"""
ASSIGNMENT EXPRESSIONS

Before looking at more examples, we need to look at a new feature intro'd
in 3.8. Assignment expressions allow us to bind a value to a name in places
where normal assignments aren't allowed. Instead of = we use := . (known
as the walrus operator)

STATEMENTS VS EXPRESSIONS

To udnerstand the difference between normal assignments and assignment
expressions, we need to understand the difference between statements and
expressions.

According to the python docs:
• a statement is part of a suite (a "block" of code). A statement is either
  an expression or one of several constructs with a keyword, such as if,
  while, or for.

• an expression is a piece of syntax which can be evaluated to some value.
  in other words, an expression is an accumulation of expression elements
  like literals, names, attribute access, operators or function calls WHICH
  ALL RETURN A VALUE.

The key distinguishing feature of an expression is that it has a value.
Notice that an expression can be a statement, but not all statements are
expressions, so they don't have a value. In particular, ASSIGNMENTS like
name = "kevin" are not expressions, so they do not have a value.
This means that we can't use an assignment statement in the condition
expression of a while loop or if statement (or any other place where a value
is required). (This is why when you put an assignment in the py console, it
doesn't print a result.)

USING THE WALRUS OPERATOR

Without assignment expressions, we'd have to use two separate statements if
we wanted to bind a value to a name and use that value in an expression. For
example, it is quite common to see the following:
"""

remainder = 155 % 3
if remainder:
    print(f"Not divisible! The remainder is {remainder}")

# with assignment expressions, we can rewrite this as:

if remainder := 155 % 3:
    print(f"Not divisible! The remainder is {remainder}")

"""
Assignment expressions allow us to write fewer  lines of code. Used with care,
they can also lead to cleaner, more understandable code. let's look at a 
slightly bigger example to see how an assignment expression can simplify a
while loop.
"""
