#  Silent Auction Program using dictionaries to declare the winner (highest bidder)
import art
print(art.logo)

max = 0
winner = ""
final_dictionary = {}
keep_going = True
while keep_going:

    # TODO-1: Ask the user for input
    name = input("What is your name? : ")
    price = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    dictionary = {name: price}
    for key in dictionary:
        final_dictionary[key] = dictionary[key]

    # TODO-3: Whether if new bids need to be added
    go_again = input("Are there any other bidders? Type 'yes or 'no'.")
    if go_again == "no":
        keep_going = False
    print("\n" * 20)

    # TODO-4: Compare bids in dictionary
    for key in final_dictionary:
        if final_dictionary[key] > max:
            max = final_dictionary[key]

winner = ""
for key in final_dictionary:
    if max == final_dictionary[key]:
        winner += key

print(f"The winner is {winner} with ${max}!")
