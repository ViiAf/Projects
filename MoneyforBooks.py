# Write your code below. See the Instructions in the tab to the right
desired_num = int(input("How many books do you want to buy? "))
money = int(input("How much money do you have? "))
amount_remaining = abs(int(money - (desired_num*20)))
 # calculating if one can buy the book with the amount of money they have
if (desired_num*20) <= money :
  print("You have enough money, go for it!")
elif amount_remaining==12:
  print("You need $12 more to buy that number of books")
else:
  print(f"You need ${amount_remaining} more to buy that number of books")