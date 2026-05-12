# import the random module
import random

# Welcome player
print("Welcome to simple dice game")

# generate random number for player and computer
user_roll = random.randint(1, 6)
computer_roll = random.randint(1, 6)
print(f"User roll: {user_roll}")
print(f"Computer roll: {computer_roll}")

# compare both dice values and determine winner
if user_roll > computer_roll:
    print("User wins")
elif computer_roll > user_roll:
    print("Computer wins")
else:
    print("Its a draw")
