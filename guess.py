# Python Number Guessing Game
# Developed by Max Pertgen
# v1.0 6/9/18

import random

guessesTaken = 0

print('Hi! What is your name?')
playerName = input()

number = random.randint(1, 20)
print('Hello ' + playerName + ', I am thinking of a number between 1 and 20, try to guess it!')

while guessesTaken < 6:
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('I\'m sorry, your guess is too low, try again!')
        print()

    if guess > number:
        print('I\'m sorry, your guess is too high, try again!')
        print()

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Way to go ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Sorry, you didn\'t guesss the number, it was ' + number)