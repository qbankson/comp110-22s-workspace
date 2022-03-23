"""Conditional Practice in PY"""

SECRET: int = 3 
print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? ")) 
if guess == SECRET:
    print("You guessed correctly!!!")
else: 
    print("Sorry, you guessed incorrectly. :[ ")
    print("Twenty five cents to play again.") 
print("Game over.") 
