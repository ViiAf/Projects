import gtts




print("Title: A Glimpse of My Whimsical Future")

# Declaring variables for inputs in the matlib

house_type = input("What type of house would you like to own?: ")
plural_noun = input("what scenery would you like to see?: ")
dream_job = input("What is your dream job?: ")
dream_workplace = input("Where would you love to see yourself working?: ")
confirm_plans = int(input("Confirm the number of years you would to fulfill these plans: "))
hobby = input("What is your favorite hobby or activity?: ")
travel = input("Where would you like to travel to?: ")
attraction = input("What attracts you to this place you would like to travel to?: ")
family_adjective = input("What adjective would you use to describe your future family?: ")
emotion = input("What kind of emotion would you like to feel in your family life?: ")
number_of_children = int(input("How many children would you like to have?: "))
children_adjective = input("What adjective would you use to describe your children?: ")
names_of_children = input("First name of you children separated by a comma: ")
partner = input("Input the name of your partner: ")

#Printing our story for the matlib
print()
print()
print("A Glimpse of My Whimsical Future")
print()
print(f"In a decade, I'll wake up in {house_type}, surrounded by {plural_noun}. My job as a {dream_job} will have me working in {dream_workplace} just as I had dreamed of {confirm_plans} years ago. In my free time, I'll enjoy {hobby}, and travel to {travel} to explore {attraction}. Family life will be filled with {family_adjective} laughter and {emotion}, as I share it with all my {number_of_children} {children_adjective} children namely {names_of_children} and my partner, {partner}.")




# Converting Text To Speech

tts = gtts.gTTS(f"In a decade, I'll wake up in {house_type}, surrounded by {plural_noun}. My job as a {dream_job} will have me working in {dream_workplace} just as I had dreamed of {confirm_plans} years ago. In my free time, I'll enjoy {hobby}, and travel to {travel} to explore {attraction}. Family life will be filled with {family_adjective} laughter and {emotion}, as I share it with all my {number_of_children} {children_adjective} children namely {names_of_children} and my partner, {partner}.")

tts.save('Glimpse.mp3')

