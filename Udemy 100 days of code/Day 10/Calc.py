logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
import os
playing = True
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def is_digit(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def calculator():
    os.system('clear')
    print(logo)
    print("Welcome to the Pythonista Calculator")

    def valid_operation(operation_symbol):
        return operation_symbol in operations

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = input("What's the first number?: ")
    while not is_digit(num1):
        num1 = input("Invalid input. Please enter a number: ")

    print("\nWhich operation would you like to perform?")
    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")
    while not valid_operation(operation_symbol):
        operation_symbol = input("Invalid operation. Pick an operation from the line above: ")

    num2 = input("What's the second number?: ")
    while not is_digit(num2):
        num2 = input("Invalid input. Please enter a number: ")

    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(float(num1), float(num2))

    print(f"{num1} {operation_symbol} {num2} = {first_answer}\n")

    proceed = True

    while proceed:
        continue_calculating = input(f"Type 'y' to continue calculating with {first_answer},\n"
                                     f"type 'n' to start a new calculation,\n"
                                     f" or type 'q' to exit the program\n : ").lower()
        if continue_calculating == "q":
            global playing
            playing = False
            proceed = False

        elif continue_calculating == "n":
            proceed = False

        elif continue_calculating == "y":
            os.system('clear')
            print(logo)
            print(f"Your current answer is {first_answer}\n")

            print("\nWhich operation would you like to perform?")
            for symbol in operations:
                print(symbol)

            operation_symbol = input("Pick an operation from the line above: ")
            while not valid_operation(operation_symbol):
                operation_symbol = input("Invalid operation. Pick an operation from the line above: ")

            num3 = input("What's the next number?: ")
            while not is_digit(num3):
                num3 = input("Invalid input. Please enter a number: ")

            calculation_function = operations[operation_symbol]
            second_answer = calculation_function(first_answer, float(num3))
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}\n")
            first_answer = second_answer


while playing:
    calculator()
