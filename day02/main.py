# This takes inputs and converts them into a split bill - including tip
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = (bill + ((tip/100) * bill)) / people
print(f"Each person should pay: ${total:.2f}")
