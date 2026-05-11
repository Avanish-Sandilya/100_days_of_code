def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


first_number = float(input("Enter first number: "))

continue_calculation = True

while continue_calculation:

    operation = input("Choose operation (+, -, *, /): ")

    second_number = float(input("Enter second number: "))

    if operation == "+":
        result = add(first_number, second_number)

    elif operation == "-":
        result = subtract(first_number, second_number)

    elif operation == "*":
        result = multiply(first_number, second_number)

    elif operation == "/":

        if second_number == 0:
            print("Cannot divide by zero")
            continue

        result = divide(first_number, second_number)

    else:
        print("Invalid operation")
        continue

    print(f"Result: {result}")

    choice = input(
        f"Do you want to continue with {result}? (yes/no): "
    ).lower()

    if choice == "yes":
        first_number = result

    else:
        continue_calculation = False
        print("Calculator closed")