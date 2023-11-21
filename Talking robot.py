
#pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
a = input("say: ")
engine.say(a)
engine.runAndWait()
