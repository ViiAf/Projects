# Code to accept the "weight" and "height" values as input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

#  Calculate the BMI value based on the weight and height values

BMI = weight / height**2

# Rounds the value
BMI = round(BMI, 1)

print(f"The body mass index is: {BMI}")

print("\n------BMI Categories------")

print("<18.5        : Underweight")
print("18.5 – 24.9  : Normal weight")
print("25 - 29.9    : Underweight")
print(">=30         : Obesity")
