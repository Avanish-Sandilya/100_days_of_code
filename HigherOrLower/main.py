# Import random and data
from data import data
import random

score = 0
game_on = True

while game_on:

    # get 2 random people
    person1, person2 = random.sample(data, 2)

    print("\nCompare A:")
    print(
        person1["name"] + ", " +
        person1["description"] + ", from " +
        person1["country"]
    )

    print("\nVS\n")

    print("Against B:")
    print(
        person2["name"] + ", " +
        person2["description"] + ", from " +
        person2["country"]
    )

    followers_query = input(
        "\nWho has more followers? Type A or B: "
    ).lower()

    # determine correct answer
    if person1["followers"] > person2["followers"]:
        correct_answer = "a"
    else:
        correct_answer = "b"

    # check answer
    if followers_query == correct_answer:

        score += 1

        print(f"\nCorrect! 🎉 Current score: {score}")

    else:

        game_on = False

        print("\nWrong answer 😢")
        print(f"Final score: {score}")