# Guess the Number - A game where a user has 5 or 10 guesses to find the correct number
import random
import art

number_to_guess = random.randint(1, 100)
print(f"Answer: {number_to_guess}")
print(art.logo)


def choose_difficulty():
    """Difficulty determines total lives to start with"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    return lives


def play_game(lives):
    """Compares guesses to predetermined number and decrements lives"""
    lives_left = lives
    while lives_left > 0 or guess != number_to_guess:
        if lives_left == 0:
            return print("You've run out of guesses. Rerun to play again.")
        else:
            print(f"You have {lives_left} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number_to_guess:
                print("You guessed correctly, you win!")
                return
            elif guess < number_to_guess:
                lives_left -= 1
                print("Too low.\nGuess again.")
            else:
                lives_left -= 1
                print("Too high.\nGuess again.")


play_game(choose_difficulty())
