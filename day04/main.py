# Rock, paper, scissors game between user and computer using random number generation
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choices = [rock, paper, scissors]
decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
print(choices[decision])

print("Computer chose:")
computer_decision = choices[random.randint(0, 2)]
print(computer_decision)

if computer_decision == rock:
    computer_decision = 0
elif computer_decision == paper:
    computer_decision = 1
else:
    computer_decision = 2


if decision == computer_decision:
    print("It's a draw")
elif decision + 1 == computer_decision:
    print("You lose")
else:
    print("You win")
