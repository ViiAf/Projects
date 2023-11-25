b = [
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "],
]

name   = input("What is your name? ")
print("Welcome to Tic Tac Toe, " + name + ". Here is our playing board:")

print(f"""
  1   2   3
1 {b[0][0]} | {b[0][1]} | {b[0][2]}
 --- --- ---
2 {b[1][0]} | {b[1][1]} | {b[1][2]}
 --- --- ---
3 {b[2][0]} | {b[2][1]} | {b[2][2]}
""")

player = "X"

# Loop for each turn
while True:
  print("It's " + player + "'s turn")
  position = input("Enter a position (i.e., 1,1): ")
  
  # Check the position is valid
  valid = position[0].isnumeric() and position[1] == "," and position[2].isnumeric()
  
  if valid:
    row = int(position[0])-1
    col = int(position[2])-1
  else:
    print("Invalid position. Enter another position.")
    continue
  
  # Update the board
  if (b[row][col] != " "):
    print("Position is occupied! Enter another position.")
    continue
  else:
    b[row][col] = player

  # display the board
  print(f"""
  1   2   3
1 {b[0][0]} | {b[0][1]} | {b[0][2]}
 --- --- ---
2 {b[1][0]} | {b[1][1]} | {b[1][2]}
 --- --- ---
3 {b[2][0]} | {b[2][1]} | {b[2][2]}
""")

  # # Check win conditions      
  # # rows  
  # rows =[]
  # for i in range(3): 
  #   rows.append(b[i])
    
  # # columns
  # col = []
  # for i in range(3)
  # for j in range(3):
  #   col.append(b[j][i])
    
  # # diagonals
  # diag = []
  #  for i in range(3):
  #    diag.append(b[i][i])
  #        diag2 = []
  
  # #Check for board is full
  #  full_board = True
  #  for i in range(3):
  #     for j in range(3):
  #       if b[i][j] == " ":
  #         full_board = False
  #         break 

  # Check win conditions
  # rows  
  for row in b:
    if row[0] == player and row[1] == player and row[2] == player:
      print("The winner is " + player)
      exit(0)
  # columns
  for i in range(0,3):
    if b[0][i] == player and b[1][i] == player and b[2][i] == player:
      print("The winner is " + player)
      exit(0)

  # diagonals
  if b[0][0] == player and b [1][1] == player and b[2][2] == player:
    print("The winner is " + player)
    exit(0)

  if b[2][0] == player and b [1][1] == player and b[0][2] == player:
    print("The winner is " + player)
    exit(0)

  #Check for when the board is full 
  sum = 0
  for row in b:
    if row[0] != " " and row[1] != " " and row[2] != " ":
      sum += 1

  if sum == 3:
    print("Board is full, Draw!")
    exit(0)


      
  
  # Update Player
  if player == "X":
    player = "O"
  else:
    player = "X"
