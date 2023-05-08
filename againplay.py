import os
from gtts import gTTS
fo = open("filetext.txt","r")
read = fo.read()
language = 'en'
output = gTTS(text=read)
output.save("fileread.mp3")
os.system("start fileread.mp3")