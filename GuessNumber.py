
#importing random library
import random
# Set secret number
number = random.randint(1,100)

print("I'm thinking of a number between 1 and 99")
user= 0

while user != number:
 user = int(input("Enter your guess: "))
 if user > number:
  print("You guess is too high")
 elif user < number:
  print("You guess is too low")
 else:
  print(f"Congrats! The number was {number}")
  break