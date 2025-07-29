# Blackjack game against the computer
# TODO: Rework implementing functions
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = True
while play:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == "y":
        print("\n" * 20)
        print(art.logo)

        player_hand = [random.choice(cards), random.choice(cards)]
        player_total = player_hand[0] + player_hand[1]
        computer_hand = [random.choice(cards)]
        computer_total = computer_hand[0]

        print(f"     Your cards: [{player_hand[0]},{player_hand[1]}], current score: {player_total} ")
        print(f"     Computer's first card: {computer_hand[0]}")

        another_card = True
        while another_card:
            if player_total == 22:
                for x in range(len(player_hand)):
                    if player_hand[0] == 11:
                        player_hand[0] = 1
                        player_total = 0
                        for x in range(len(player_hand)):
                            player_total += player_hand[x]

            elif player_total < 22:
                get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

                if get_another_card == "y":
                    player_total = 0
                    player_hand.append(random.choice(cards))
                    for x in range(len(player_hand)):
                        player_total += player_hand[x]
                        if player_total > 21:
                            for x in range(len(player_hand)):
                                if player_hand[x] == 11:
                                    player_hand[x] = 1
                                    player_total = 0
                                    for x in range(len(player_hand)):
                                        player_total += player_hand[x]
                    print(f"     Your cards: {player_hand}, current score: {player_total} ")
                    print(f"     Computer's first card: {computer_hand[0]}")
                else:
                    another_card = False
                    while computer_total < 17:
                        computer_total = 0
                        computer_hand.append(random.choice(cards))
                        for x in range(len(computer_hand)):
                            computer_total += computer_hand[x]
                            if computer_total > 21:
                                for x in range(len(computer_hand)):
                                    if computer_hand[x] == 11:
                                        computer_hand[x] = 1
                                        computer_total = 0
                                        for x in range(len(computer_hand)):
                                            computer_total += computer_hand[x]

                    print(f"    Your final hand: {player_hand}, final score: {player_total}")
                    print(f"    Computer's final hand: {computer_hand}, final score: {computer_total}")

                    if player_total <= 21 and player_total > computer_total:
                        print("You win :^)")
                    elif player_total <= 21 and computer_total > 21:
                        print("Computer went over. You win :^)")
                    elif player_total == computer_total:
                        print("It's a draw :^|")
                    else:
                        print("You lose :^(")

            else:
                another_card = False
                print(f"    Your final hand: {player_hand}, final score: {player_total}")
                print(f"    Computer's final hand: [{computer_hand[0]}], final score: {computer_total}")
                print("You went over. You lose :^(")

    else:
        play = False
        print("\n" * 20)
