rock0 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors2 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
PlayerInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
randomNumber = random.randint(0,2)
result = "1"

if PlayerInput == 0:
  print(rock0)
if PlayerInput == 1:
  print(paper1)
if PlayerInput == 2:
  print(scissors2)

print("Computer chose:")
if randomNumber == 0:
  print(rock0)
if randomNumber == 1:
  print(paper1)
if randomNumber == 2:
  print(scissors2)


if PlayerInput == randomNumber:
  result = "Draw"
if PlayerInput == 0 and randomNumber == 1:
  result = "You lose"
if PlayerInput == 0 and randomNumber == 2:
  result = "You win"
if PlayerInput == 1 and randomNumber == 0:
  result = "You win"
if PlayerInput == 1 and randomNumber == 2:
  result = "You lose"
if PlayerInput == 2 and randomNumber == 0:
  result = "You lose"
if PlayerInput == 2 and randomNumber == 1:
  result = "You win"

print(result)