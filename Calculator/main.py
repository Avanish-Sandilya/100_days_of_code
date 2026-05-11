def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


first_number = float(input("Enter first number: "))

operation = input("Choose operation\n+\n-\n*\n/\n")

second_number = float(input("Enter second number: "))

final_sol = 0


if operation == "+":
    final_sol = add(first_number, second_number)

elif operation == "-":
    final_sol = subtract(first_number, second_number)

elif operation == "*":
    final_sol = multiply(first_number, second_number)

elif operation == "/":
    final_sol = divide(first_number, second_number)

else:
    print("Invalid operation")


print("Result:", final_sol)