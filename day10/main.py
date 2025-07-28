#  Calculator program that works as a basic calculator using user inputs

import art
print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


math_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    first_number = float(input("What's the first number?: "))
    power = True
    while power:
        print("+")
        print("-")
        print("*")
        print("/")
        operation = input("Pick an operation: ")
        second_number = float(input("What's the second number?: "))

        result = math_dictionary[operation](first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {result:.1f}")
        keep_going = input(f"Type 'y' to continue calculating with {result:.1f}, "
                           f"or type 'n' to start a new calculation: ")
        if keep_going == "y":
            first_number = result
        else:
            print("\n" * 20)
            print(art.logo)
            power = False
            calculator()


calculator()
