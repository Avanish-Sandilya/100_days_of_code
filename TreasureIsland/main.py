print("Welcome to treasure island")

direction_choice = input("You are at a crossroad, choose left or right")
if direction_choice == "right":
    print("You fell into a pit, Game Over")
else:
    lake = input("You are at a lake, choose to swim or wait for boat")
    if lake == "swim":
        print("You drowned, game over")
    else:
        room = input("You reached near three rooms they have red, green and yellow gates, choose one")
        if room == "red":
            print("You entered fire room, game over")
        elif room == "green":
            print("You entered jungle full of snakes, game over")
        else:
            print("You found the treasure, you won")
