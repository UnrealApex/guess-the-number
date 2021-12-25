# TODO: add difficultly levels using enums
import random
# kill_game = False 
difficultly = 0

def playGame():
  kill_game = False
  while kill_game == False:
    x  = random.randint(0, 100)
    print("Welcome to the random number guessing game\nTo play, enter a number between 0 and 100 and press enter.\n====================");
    try:
      y = int(input("Enter your guess here: "))
      print(y)
    except ValueError:
      print("Enter a number!")
      y = int(input("Enter your (number) guess here: "))
      print(y)  
    if x == y:
      print("Congratulations, you guessed the number!")
    else:
      print("You didn't guess the number\nThe number was " + str(x));  
    playAgain()
  return kill_game  



# FIXME: make sure that game starts again and stops when users wants it to  
def playAgain():
  z = str(input("\nWant to play again? (Y/n): ")).lower()
  print(z)
  if z == "y" or z == "yes":
    killgame_game = False
  elif z == "n" or z == "no":
    print("Game terminated")
    killgame_game = True
  else:
    print("Enter the letter y or n")  
  return killgame_game


playGame()