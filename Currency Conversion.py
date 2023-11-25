
# Exchange rate
NAIRA_PER_DOLLAR = 410.59 # exchange rate as of Nov 10 2021
USD_input = float(input("enter the amount of USD to convert to NGN: "))
Naira = USD_input * NAIRA_PER_DOLLAR
# printing out the results after converting dollar to naira
print(f"{USD_input: .2f} USD is" f"{Naira: .2f} NGN")

# print(f"{USD_input:.3f}" + " USD is " + f"{Naira: .2f}" + "NGN")
