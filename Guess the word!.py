import random

number = random.randint(0,3)

words = ["Ice Cream", "Dog", "Grass", "Pencil"]

hint1 = ["Melting", "Bone", "Green", "Case"]
hint2 = ["Summer", "Woof", "Lawn", "Sharpen"]

guess = ""

counter = 1

secretword = words[number]

while True:
    print("Guess the word!")
    print("Please write the first letter with a capital letter. Type 'hint1', 'hint2', 'first letter', 'last letter', or 'give up' for help.")
    guess = input()

    if guess == secretword:
        print("That is correct! You win!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "last letter":
        print(secretword[-1])

    elif guess == "give up":
        print("The word was " + secretword + ".")
        break

    else:
        print("Try again.")
        counter += 1
