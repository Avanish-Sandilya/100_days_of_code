import random

print("Welcome to guess the number")

random_number = random.randint(1, 100)

print("I am thinking of a number between 1 to 100, try to guess it")

easy_or_hard = input("which mode do you want, easy or hard")

lives = 0

if easy_or_hard == "easy":
    lives = 10
else:
    lives = 5

while lives > 0:
    user_guess = int(input("Enter your guess"))
    if user_guess == random_number:
        print("Correct guess, you won")
        break
    elif user_guess > random_number:
        print("Too high")
        lives -= 1
        print(f"Lives: {lives}")
    elif user_guess < random_number:
        print("Too low")
        lives -= 1
        print(f"Lives: {lives}")
    else:
        print("Invalid input")
        lives -= 1
        print(f"Lives: {lives}")

    if lives == 0:
        print(f"You lose, the number was {random_number}")
