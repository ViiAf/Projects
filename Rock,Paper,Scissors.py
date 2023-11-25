# Write your solution below the starter code
# Follow the instructions in the tab to the right
import random
from random import seed
from random import randint
# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

# Get a choice from the user

user_choice = input("Rock,Paper or Scissors? ")
user_choice.lower()

# Make a choice for the computer player
play = ['Rock','Paper','Scissors']
comp = play[random.randint(0,2)]
print(f"The computer chooses {comp}")


# Compare the user and computer choice
if comp == user_choice:
  print("It's a draw")
elif comp == 'Rock' and user_choice == 'Paper':
  print("You win")
elif comp == 'Rock' and user_choice == 'Scissors':
  print("You lose")
elif comp == 'Paper' and user_choice == 'Rock':
  print("You lose")
elif comp == 'Paper' and user_choice == 'Scissors':
  print("You win")
elif comp == 'Scissors' and user_choice == 'Rock':
  print("You win")
elif comp == 'Scissors' and user_choice == 'Paper':
  print("You lose")
  # Print the right message, based on the choices
else:
  print("That's not a valid choice. You have to enter either rock, paper or scissors.")