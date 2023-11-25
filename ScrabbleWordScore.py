

print("Generate the scrabble score for a word.")

# Get a word as input
word = input("Enter a word: ")

# Start the score at 0
score = 0


# Loop over the letters in the word
for alphabet in word:
  ## At each step in the loop, add the value for that letter
  ## To find the letter value, check if the letter is in the set of letters for each score, like this:

  if alphabet in 'aeilnorstu':
    score += 1
  elif alphabet in 'dg':
    score += 2
  elif alphabet in 'bcmp':
    score += 3
  elif alphabet in 'fhvwy':
    score += 4
  elif alphabet in 'k':
    score += 5
  elif alphabet in 'jx':
    score += 8
  elif alphabet in 'qz':
    score += 10



# Print out the score
print(f"{word} has a scrabble score of {score}")
