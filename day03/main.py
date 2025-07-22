# This uses if/elif/else statements to create a pick-your-own-adventure game
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("*Make sure your answers match the options surrounded in 'quotes'.")

decision = input("You're at a fork in the road, do you go 'left' or 'right'? ")
if decision == "right":
    print("You end up walking off a ledge to your death. Try again in another life!")
if decision == "left":
    decision = input("You head left and end up at a lake. Do you 'swim' to the island, or 'wait' for the boat? ")

    if decision == "swim":
        print("A mystical current forces you down, drowning you. Try again in another life!")
    if decision == "wait":
        decision = input("After getting off the boat you are faced with three doors, "
                         "do you open the 'red', 'blue', or 'yellow' door? ")

        if decision == "red":
            print("After opening the red door, a bomb goes off blowing you up. Try again in another life!")
        elif decision == "blue":
            print("After opening the blue door, you're life force is sucked out of you. Try again in another life!")
        else:
            print("After opening the yellow door, you see it is filled with treasure. Congrats, you win!")
