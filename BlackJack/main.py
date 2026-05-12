import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
dealer_hand = []


def deal_card_player(number_of_cards):
    for card in range(number_of_cards):
        player_hand.append(random.choice(cards))


def deal_card_dealer(number_of_cards):
    for card in range(number_of_cards):
        dealer_hand.append(random.choice(cards))


# Handle Ace logic
def calculate_score(hand):

    score = sum(hand)

    # Convert Ace from 11 to 1 if busted
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score


def check_winner():

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"\nYour final hand: {player_hand} | Score: {player_score}")
    print(f"Dealer final hand: {dealer_hand} | Score: {dealer_score}")

    if player_score > 21:
        print("Dealer wins! You busted 😢")

    elif dealer_score > 21:
        print("You win! Dealer busted 🎉")

    elif player_score > dealer_score:
        print("You win! 🎉")

    elif dealer_score > player_score:
        print("Dealer wins!")

    else:
        print("It's a draw!")


game_on = True

while game_on:

    user_choice = input(
        "\nDo you want to play a game of Blackjack? (y/n): "
    ).lower()

    if user_choice == "y":

        # Reset hands every game
        player_hand.clear()
        dealer_hand.clear()

        deal_card_player(2)
        deal_card_dealer(2)

        playing = True

        while playing:

            print(f"\nYour hand: {player_hand}")
            print(f"Your score: {calculate_score(player_hand)}")

            print(f"Dealer's first card: {dealer_hand[0]}")

            # Check immediate blackjack/bust
            if calculate_score(player_hand) >= 21:
                break

            hit_or_show = input(
                "Type 'hit' to get another card or 'show' to stand: "
            ).lower()

            if hit_or_show == "hit":
                deal_card_player(1)

            else:
                playing = False

        # Dealer keeps drawing until 17+
        while calculate_score(dealer_hand) < 17:
            deal_card_dealer(1)

        check_winner()

    else:
        game_on = False
        print("Game closed")