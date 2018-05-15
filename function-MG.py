def hello(name):
    print("Hello " + name + "!")
    print("How's it going?")
    day = input("Is your day looking good?")
    day = day.title()
    if day == "Yes":
        print("That's great!")
    elif day == "No":
        print("Sorry to hear that!")
    else:
        print("I didn't quite catch that.")

    while True:
        food = input("What's for lunch?")
        food = food.lower()
        if food == "chicken nuggets":
            print("One of us had a dream about that!")
        elif food == "tacos":
            print("Taco Tuesday!!")
        elif food == "barbecue chicken":
            print("That's correct!")
            break
        else:
            print("I guess it could be that...")
    print("Okay Bye!")

hello('Milli')
hello('Annie')
hello('Lauren')
hello('Alexa')
