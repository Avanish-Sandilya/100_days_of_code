print("Welcome to silent auction")

bids_record = {}
winner_name = ""
winner_bid = 0
bid_on = True

while bid_on:
    name = input("Enter your name")
    bid = float(input("Enter your bid"))

    bids_record[name] = bid

    another_bidder = input("Is there another bidder? enter y or n").lower()

    if another_bidder == "n":
        bid_on = False

        highest_amount = 0
        for key, value in bids_record.items():
            if value > highest_amount:
                highest_amount = value
                winner_name = key
                winner_bid = value


print(f"Winner of the auction is:{winner_name}\nBid:{winner_bid}")

