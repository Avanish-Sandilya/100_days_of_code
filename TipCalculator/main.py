print("Welcome to tip calculator")

# taking total bill as input
total = input("Enter the total bill amount\n")

# taking percentage to tip
tip_percent = input("What percentage would you like to tip\n")

# number of people splitting the bill
people_count = input("How many people are splitting the bill\n")

# tip calculation
tip_amount = (float(tip_percent)/100)*float(total)
tip=tip_amount/float(people_count)

print(f"Each person will pay {round(tip,2)} as tip")
