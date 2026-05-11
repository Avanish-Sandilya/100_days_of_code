def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


sol = 0

first_number = float(input("Enter the first number"))

calculation_on = True

while calculation_on:
    operation = input("Choose operation:\n+\n-\n*\n/")

    second_number = float(input("Enter the second number"))

    if operation == "+":
        sol = add(first_number, second_number)
    elif operation == "-":
        sol = subtract(first_number, second_number)
    elif operation == "*":
        sol = multiply(first_number, second_number)
    elif operation == "/":
        if second_number == 0:
            print("Division by 0")
            continue
        sol = divide(first_number, second_number)

    print(f"The result of operation is: {sol}")

    query = input(f"Do you want to continue with {sol}. yes/no").lower()

    if query == "yes":
        first_number = sol
    else:
        calculation_on = False
        print("Calculator closed")

