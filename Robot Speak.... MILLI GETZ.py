import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Heyo Milli, What do you want me to look up for you?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("Oki doki, let's look for " + r.recognize_google(audio))
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


'''
https://www.youtube.com/results?search_query=

            https://www.google.com/search?q=dogs&rlz=1C1GCEA_enUS752US752&oq=dogs&aqs=chrome..69i57j69i60l3j0l2.706j0j7&sourceid=chrome&ie=UTF-8
'''
