# AC Load Estimator Code
width = float(input("enter width of room: "))
height = float(input("enter height of room: "))
number_of_people = int(input("enter number of people in the room: "))
# formula for calculating AC load
horsepower = width * height * 0.1 + number_of_people * 0.06
#Rounding the horsepower to 3 decimal place and printing it out
print(f"AC load estimate is {horsepower:.3f} HP")
