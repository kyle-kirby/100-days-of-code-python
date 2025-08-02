# Higher Lower game where user guess which celebrity has the most followers
import random
from game_data import data
from art import logo, vs

item1 = random.choice(data)
item2 = random.choice(data)
if item1 == item2:
    item2 = random.choice(data)

score = 0
keep_playing = True

print(logo)
while keep_playing:
    print(f"Compare A: {item1["name"]}, a {item1["description"]}, from {item1["country"]}.")
    print(vs)
    print(f"Against B: {item2["name"]}, a {item2["description"]}, from {item2["country"]}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if item1["follower_count"] > item2["follower_count"] and guess == "A":
        score += 1
        print(f"You're right! Current score: {score}")
        item2 = random.choice(data)
    elif item1["follower_count"] < item2["follower_count"] and guess == "B":
        score += 1
        print(f"You're right! Current score: {score}")
        item1 = item2
        item2 = random.choice(data)
    else:
        print("\n" * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        keep_playing = False
