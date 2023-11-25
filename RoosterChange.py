# See the Instructions tab.
# Scroll down to see where you should write your solution
roster = [
  "Thibaut Courtois",
  "Dani Carvajal",
  "Brahim Díaz",
  "Éder Militão",
  "Jesús Vallejo",
  "Nacho",
  "Eden Hazard",
  "Toni Kroos",
  "Karim Benzema",
  "Takefusa Kubo",
  "Álvaro Odriozola",
  "Luka Modrić",
  "Marco Asensio",
  "Marcelo",
  "Andriy Lunin",
  "Martin Ødegaard",
  "Casemiro",
  "Federico Valverde",
  "Luka Jović",
  "Sergio Ramos",
  "Lucas Vázquez",
  "Gareth Bale",
  "Dani Ceballos",
  "Vinícius Júnior",
  "Raphaël Varane",
  "Rodrygo",
  "Isco",
  "Ferland Mendy",
  "Mariano"
]

# Write your solution below

print("\nThe current Real Madrid roster:\n")
# Print the current roster using a for loop
for player in roster:
  print(player)
  
# Remove players using pop()
players_remov_index = [2, 9, 10, 15, 19, 24]
players_remov_index.sort(reverse=True)

# for index in players_remov:
for index in players_remov_index:
  roster.pop(index)

# Add players using append()
roster.append("Eduardo Camavinga")
roster.append("David Alaba")

print("\n------")
print("\nThe new Real Madrid roster:\n")
# Print the new roster using a for loop
for player in roster:
  print(player)

