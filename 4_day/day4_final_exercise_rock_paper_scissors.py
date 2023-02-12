import random

print("Welcome to Rock, Paper and Scissors")

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

outcome = [rock, paper, scissors]

player_index = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n")) - 1
random_index = random.randint(0, 2)

player = outcome[player_index]
bot = outcome[random_index]

if player == 0 and bot == 2:
  print("You\n",player)
  print("Bot\n",bot)
  print("You win!")
elif player == 0 and bot == 2:
  print("You\n",player)
  print("Bot\n",bot)
  print("You lose")
elif player > bot:
  print("You\n",player)
  print("Bot\n",bot)
  print("You lose")
elif bot > player:
  print("You\n",player)
  print("Bot\n",bot)
  print("You win!")
elif player == bot:
  print("You\n",player)
  print("Bot\n",bot)
  print("It's a draw")