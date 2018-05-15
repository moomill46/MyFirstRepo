import pyautogui as pg
import webbrowser
import time

answer = pg.confirm("How hungry are you on a scale from 1 to 5.", "", ["1", "2", "3", "4", "5"])

answer = pg.confirm("Do you have any food restrictions?", "", ["No Food Restrictions", "Gluten Free", "Lactose Intolerant", "Vegan", "Vegietarian"])

answer = pg.confirm("What meal would you like to make?", "", ["Snack", "Snack", "Snack", "Snack", "or Snack"])

if answer == "No Food Restrictions":
    print("Here is recipe")



'''
# Question 1
# Questions for player
answer = pg.prompt("""
How hungry are you on a scale from 1 to 5.
1
2
3
4
5
'''


