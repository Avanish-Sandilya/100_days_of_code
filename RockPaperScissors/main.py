import random

# available choices
choice_list = ["rock", "paper", "scissors"]

# Taking user input
user_input = input("What would you choose, 0 for rock, 1 for paper, 2 for scissors")

user_number = int(user_input)

user_choice = choice_list[user_number]

# Generating computer choice
computer_number = random.randint(0, 2)

computer_choice = choice_list[computer_number]

# Logic to determine winner
if user_number == computer_number:
    print(f"your choice: {user_choice}\ncomputer choice: {computer_choice}\nIts a draw")
elif (user_number == 0 and computer_number == 1) or (user_number == 1 and computer_number == 2) or (user_number == 2 and computer_number == 0):
    print(f"your choice: {user_choice}\ncomputer choice: {computer_choice}\nComputer wins")
else:
    print(f"your choice: {user_choice}\ncomputer choice: {computer_choice}\nYou win")