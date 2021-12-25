# TODO: add difficultly levels using enums
# TODO: add score
import math
import random
# loop in which our game runs
while True:
  # generate a random number between 1 and 100
  x  = random.randint(1, 100)
  print("Welcome to the random number guessing game\nTo play, enter a number between 1 and 100 and press enter.\n====================");
  # make sure the users enters a number
  try:
    guess = int(input("Enter your guess here: "))
    print(guess)
  # try again if a number isn't entered
  except ValueError:
    print("Enter a number!")
    guess = int(input("Enter your (number) guess here: "))
    print(guess)  
  if x == guess:
    print("Congratulations, you guessed the number!")
  # if the user's guess was 10 numbers away, tell them they were close to the right guess
  else:
    if (x == (guess - 10)) or (x == (guess + 10)):
      print("You didn't guess the number, but you were very close\nThe number was " + str(x)) 
    else:  
      print("You didn't guess the number\nThe number was " + str(x))
  # ask the user if they want to play again, restart if if true, stop it if false 
  play_again = str(input("\n\n\nWant to play again? (Y/n): ")).lower()
  print(play_again)
  if play_again == "y" or play_again == "yes":
    print("\nRestarting game...\n")
  # if the users types anything other than yes, stop the game 
  else:
    print("Game stopped")
    break
