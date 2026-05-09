import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

# taking user inputs
password_length = int(input("How long you want the password to be"))
letters_required = int(input("How many letters do you want in password"))
numbers_required = int(input("How many numbers you need in the password"))
symbols_required = int(input("How many symbols you need in the password"))

password = []

# creating password list
for _ in range(letters_required):
    password.append(random.choice(letters))

for _ in range(numbers_required):
    password.append(str(random.choice(numbers)))

for _ in range(symbols_required):
    password.append(random.choice(symbols))

random.shuffle(password)

final_password = ""

for var in password:
    final_password = "".join(password)

print(final_password)
