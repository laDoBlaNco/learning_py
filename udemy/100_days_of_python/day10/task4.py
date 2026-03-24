# task4.py
import art

# Final project of the day. the Calculator Project

def add(n1: float, n2: float) -> float:
    """Adding two numbers and returning the sum"""
    return n1 + n2


def substract(n1: float, n2: float) -> float:
    """Subtracting two numbers and returning the difference"""
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    """Muliplying two numbers and returning the product"""
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    """Dividing two numbers and returning the quotient"""
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def calculator()->None:
    print(art.logo)
    should_accumulate = True
    first_num = float(input("What's the first number?: "))

    while should_accumulate:
        print("+\n-\n*\n/")
        op = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        answer = operations[op](first_num, second_num)
        print(f"{first_num} {op} {second_num} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: "
        )

        if choice=='y':
            first_num=answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()

calculator()