# task2.py


# Now functions with outputs
def my_function():
    result = 3 * 2
    return result


print(my_function())
print()


def format_name(f_name: str, l_name: str) -> str:
    if f_name == "" or l_name == "":
        return "You didn't provide a valid name"
    return f"{f_name.title()} {l_name.title()}"


print(
    format_name(input("What is our first name?: "), input("What is your last name? "))
)

print()
