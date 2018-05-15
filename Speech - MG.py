import win32com.client as wincl
import pyautogui as pg

speak = wincl.Dispatch("SAPI.SpVoice")

speak.speak("What is your favorite show?")

answer = pg.prompt("Enter your favorite show.")

if answer == "90210":
    speak.Speak("Wow, that's my FAVORITE show too")

elif answer == "friends":
    speak.Speak("I LOVE THAT SHOW!")

elif answer == "Grey's Anatomy":
    speak.Speak("hmmmmmmmmmm... why? that is not my favorite...")

else:
    speak.Speak("Okay, your favorite show is " + answer)
