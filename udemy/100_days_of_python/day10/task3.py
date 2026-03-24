# task3.py - DOCSTRINGS


# Now functions with outputs
def my_function():
    '''A stupid little sample function'''
    result = 3 * 2
    return result


print(my_function())
print()

# doc strings go right after the declaration and with triple quotes

def format_name(f_name: str, l_name: str) -> str:
    '''Take a first and last name and format them to 
    return the title case version of the name.'''
    if f_name == "" or l_name == "":
        return "You didn't provide a valid name"
    return f"{f_name.title()} {l_name.title()}"


print(
    format_name(input("What is our first name?: "), input("What is your last name? "))
)

print()
