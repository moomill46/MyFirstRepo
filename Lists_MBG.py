name = "Milli"

subjects = ["English","Math","Science","History","Latin"]
'''
print("Hello " + name)

for i in subjects:
    print("One of my subjects is " + i)
    
Animals = ["Dogs","Elephants","Dolphins",""]
friendsCharacters = ["Ross","Rachel","Monica","Janice","Chandler","Phoebe","Joey"]

for i in friendsCharacters:
    if i == "Ross":
        print(i + " is my least favorite character!")
    elif i == "Phoebe":
        print(i + " is one of my favorite characters!")
    elif i == "Joey":
        print(i + " is the funiest character!")
    elif i == "Rachel":
        print(i + " has the best style!")
    elif i == "Monica":
        print(i + " is a perfectionist, but a great character!")
    elif i == "Janice":
        print(i + " is VERY loud, but very funny!")
    elif i == "Chandler":
        print(i + " is always cracking a joke!")

print(characters[random.randint(0,6)])
'''
movies = []

while True:
    print("What's one of your favorite movies? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)
    
