import random
import time

number = random.randint(1, 100)

guess = 0

counter = 0


while True:
    print("Guess the number! It is between 1 and 100.")
    guess = int(input())
    counter += 1

    if guess == number:
        print("You guessed right! Good job!")
        print("You tried " + str(counter) + " guesses.")
        break

    elif guess < number:
        print("Too low, try again.")

    elif guess > number:
        print("Too high, try again.")
