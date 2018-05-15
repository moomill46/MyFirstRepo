import pyautogui as pg
import time
import webbrowser


# Sets points to zero at start
points = 0

# Question 1
# Questions for player
answer = pg.prompt("""
Which would you rather be?
a) Actor
b) Paleontologist
c) Chef
d) Massuse

""")

pg.alert("You Chose " + answer)

if answer == "a":
    pg.alert("Next question")
    points += 1
elif answer == "b":
    pg.alert("Next Question")
    points += 2
elif answer == "c":
    pg.alert("Next Question")
    points += 3
elif answer == "d":
    pg.alert("Next Question")
    points += 4

# Question 2
# Questions for player
answer = pg.prompt("""
What would you rather do?
a) Eat a sandwich with many meats
b) Play with Dinosaurs
c) Clean
d) Play the Guitar

""")

pg.alert("You Chose " + answer)

if answer == "a":
    pg.alert("Next question")
    points += 1
elif answer == "b":
    pg.alert("Next Question")
    points += 2
elif answer == "c":
    pg.alert("Next Question")
    points += 3
elif answer == "d":
    pg.alert("Next Question")
    points += 4


# Question 3
# Questions for player
answer = pg.prompt("""
What is most like your personality?
a) Out going
b) Brainy and whiney
c) Perfectionist
d) Hippy

""")

pg.alert("You Chose " + answer)

if answer == "a":
    pg.alert("Next question")
    points += 1
elif answer == "b":
    pg.alert("Next Question")
    points += 2
elif answer == "c":
    pg.alert("Next Question")
    points += 3
elif answer == "d":
    pg.alert("Next Question")
    points += 4


# Question 4
# Questions for player
answer = pg.prompt("""
What is your favorite animal?
a) Duck
b) Dinosaur
c) Dog
d) Cat

""")

pg.alert("You Chose " + answer)

if answer == "a":
    pg.alert("Next question")
    points += 1
elif answer == "b":
    pg.alert("Next Question")
    points += 2
elif answer == "c":
    pg.alert("Next Question")
    points += 3
elif answer == "d":
    pg.alert("Next Question")
    points += 4


    
#END OF SURVEY
pg.alert("OK, here is your character...")
#Joey
if points <= 7:
    pg.alert("You are Joey!")
    webbrowser.open("http://cdn.playbuzz.com/cdn/d8db7404-1a40-467e-a31f-d3eddf050426/4c3492b7-e405-4499-bb99-0e7149800fe5.jpg")

#Ross
elif points >= 8 and points < 10:
    pg.alert("You are Ross!")
    webbrowser.open("https://i.ytimg.com/vi/VBT0VcqP6Y0/maxresdefault.jpg")

#Monica
elif points >= 10 and points <=12:
    pg.alert("You are Monica!")
    webbrowser.open("http://images.intouchweekly.com/uploads/images/file/31975/courteney-cox-friends-minca-hair-8.png?fit=crop&h=680&w=680")

#Phoebe
elif points >12 and points <= 16:
    pg.alert("You are Phoebe!")
    webbrowser("https://img.buzzfeed.com/buzzfeed-static/static/2014-07/30/10/enhanced/webdr04/anigif_original-grid-image-25729-1406730466-13.gif?crop=240:240;2,0}")
