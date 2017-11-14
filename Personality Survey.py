import time
points = 0
print("What is your name?")
name = input()
print("Hello " + name)

print("What is your favorite animal?")
animal = input()
if animal == "dog":
    points += 2
    print("Mine too!")
elif animal == "elephant":
    points += 1
    print("That is an awesome animal!")
else:
    print("That is a cool animal.")

print("What is your favorite color?")
color = input()
if color == "green":
    points += 3
    print("That is the best color!")
elif color == "blue":
    points += 2
    print("That is my second favorite color!")
else:
    print("That color is good too, but green and blue are the best colors.")

print("What is your favorite food?")
food = input()
if food == "potatoes":
    points += 2
    print("I LOVE POTATOES")
elif food == "chicken":
    points += 2
    print("Chicken is SO yummy!")
elif food == "tofu":
    points -= 2
    print("YUM?????")
else:
    print(food + " is good too!")

print("What sport do you like to play most?")
sport = input()
if sport == "soccer":
    print("What position do you play?")
    soccerposition = input()
    if soccerposition == "defence":
        print("Me too!")
    elif soccerposition == "goalie":
        print("That is a tough position!")
    else:
        print(soccerposition + " is a good one!")
elif sport == "tennis":
    points += 2
    print("I love tennis!")
elif sport == "surfing":
    points += 3
    print("Surfing is the best sport ever!")
else:
    print(sport + " is a fun sport too!")

print("Are you reading a book right now?")
readinganswer = input()
if readinganswer == "yes":
    print("What book are you reading?")
    book = input()
    if book == "Everything Everything":
        print("That is the best book ever!")
    else:
        print(book + " sounds like a great book!")
elif readinganswer == "no":
    print("Then are you watching a show?")
    showanswer = input()
    if showanswer == "yes":
        print("What TvShow is it?")
        tvshow = input()
        if tvshow == "friends":
            print("That is the best show!")
        else:
            print(tvshow + " sounds like a pretty good show!")
    else:
        print("Okay")

print("How old are you?")
age = input()
if age == "14":
    print("Me too! When is your birthday?")
    birthday = input()
    if birthday == "November 12":
        print("NO WAY! ME TOO!")
        
    
      
  
time.sleep(200)
        
'''
print("What sport do you like to play most?")
sport = input()
if sport == "soccer":
    print("What position do you play?")
    soccerposition = input()
    if soccerposition == "defence":
        print("Me too!")
    elif soccerposition == "goalie":
        print("That is a tough position!")
    else:
        print(soccerposition + " is a good one!")
elif sport == "tennis":
    print("I love tennis!")
else:
    print(sport + " is a fun sport too!")
 '''   
    
