# task1.py


# Now functions with outputs
def my_function():
    result = 3 * 2
    return result


print(my_function())
print()


def format_name(f_name: str, l_name: str) -> str:
    return f"{f_name.title()} {l_name.title()}"


print(format_name("keVin", "whiteSide"))

print()


def function_1(text: str) -> str:
    return text + text


def function_2(text: str) -> str:
    return text.title()

output = function_2(function_1('hello'))
print(output)
