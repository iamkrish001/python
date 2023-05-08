from tracemalloc import start
from webbrowser import open_new
from gtts import gTTS
import os
fo = open("text.txt","r")
language = 'en'
mytext = fo.read()
output = gTTS(text=mytext)
output.save("output.mp3")
os.system("start output.mp3")