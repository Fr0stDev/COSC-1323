#Assignment 4 - Guessing Game
#By Guillermo Moran

import random

def main():

    randomNumber = random.randint(1,50)
    guessedNumber = int(input("I'm thinking of a number between 1-50. Take a guess: "))
    attemptCount = 1
    
    while (guessedNumber != randomNumber):
        
        if (guessedNumber > randomNumber):
            guessedNumber = int(input("Guess a lower number: "))
            
        if (guessedNumber < randomNumber):
            guessedNumber = int(input("Guess a higher number: "))

        attemptCount += 1 

    print("Congratulations! You guessed the number", guessedNumber, "in", attemptCount, "attempts!")
        
main()
        
