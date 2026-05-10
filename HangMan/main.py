import random

lives = 6
word_guess_list = []
# Getting a random word
word_list = ["bubble", "trouble", "game", "winner"]
random_word = random.choice(word_list)

# Creating blanks
for char in random_word:
    print("_", end=" ")
    word_guess_list.append("_")


def print_current():
    for i in word_guess_list:
        print(i, end=" ")


# taking user input
while lives > 0:
    user_input = input("\nEnter your guess\n")
    found = False
    for i in range(len(random_word)):
        if random_word[i] == user_input and word_guess_list[i] == "_":
            word_guess_list[i] = user_input
            found = True

    if not found:
        lives -= 1
        print(f"Wrong guess, lives remaining: {lives} ")
    print_current()

    if "_" not in word_guess_list:
        print("\nyou win")
        break

if "_" in word_guess_list:
    print(f"You loose, the word was: {random_word}")





