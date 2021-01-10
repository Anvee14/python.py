import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 9)

print('Well, ' + myName + ', I am thinking of a number between 1 and 9.')

while guessesTaken < 6:

    print('Take a guess.') 

    guess = input("Enter your guess:")
    guess = int(guess)
    guessesTaken=guessesTaken + 1

    if guess < number:

        guess = str(guess)
        print('Your guess is too low.-Guess higher than ' + guess)
        guess = int(guess)

    if guess > number:
        guess = str(guess)
        print('Your guess is too high.-Guess lower than ' + guess)
        guess = int(guess)

    if guess == number:
        break

if guess == number:
    guessesTaken=str(guessesTaken)
    print('Great, ' + myName + '! You guessed my number in ' +
          guessesTaken + ' guesses!')

if guess != number:
    number=str(number)
    print('Nope. The number I was thinking of was ' + number)
