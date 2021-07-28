import pyttsx3
from googletrans import Translator

p = Translator()

engine = pyttsx3.init()

engine.say("my cat black")
engine.runAndWait()


