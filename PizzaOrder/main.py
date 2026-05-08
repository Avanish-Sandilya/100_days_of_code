size = input("What size pizza do you want. S, M or L")
pepperoni = input("Do you want pepperoni on your pizza y, n")
cheese = input("Do you want extra cheese on your pizza. y, n")

total = 0

if size == "s":
    total = 15
elif size == "m":
    total = 20
else:
    total = 25

if pepperoni == "y":
    total += 2

if cheese == "y":
    total += 1

print(f"Your total bill is: {total}")