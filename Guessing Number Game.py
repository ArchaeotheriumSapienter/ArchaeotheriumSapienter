# This is a guess the number game.
import random

print('What is your name?')
name = input()

print('Well, ' + name + ', I am guessing a number between 1 and 20, care to know what it is? You only have six tries before I get bored so you better make your choices count!')
secretNumber = random.randint(1, 20)

for guessesTaken in range (1, 7):
    print('Take a guess')
    playerGuess = int(input())

    if abs(secretNumber - playerGuess) == 1:
        print('So close!')
    elif playerGuess < secretNumber:
        print('Your guess is too low.')
    elif playerGuess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess

if playerGuess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
