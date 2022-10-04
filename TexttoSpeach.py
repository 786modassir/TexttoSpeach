from gtts import gTTS # We have imported this module for text to speach conversion.

import os 

# if you want from file that you can change 
abc = open('sample.txt')
text = abc.read() # Text that you want to convert

language = 'en' # en for English language

obj = gTTS(text = text,lang=language,slow = False)
# we have used from slow = False because our converted video will have a high speed

obj.save("sample.mp3")
# to open the video file autometically we have to import os
os.system("sample.mp3")

# defination of gTTS(google text-to-Speach) liabrary, Which is a very easy liabrary that converts text into Audio.
# The play sound module is used to play audio files. 
# With this module, We can play a sound file with a single line of code.
# first stap is go on cmd prompth to type the pip install gTTS.
# We have imported this module for text to Speach coversion.
# text that you want to convert. 
# en is for english  language.
# we have used slow because our converted video will have a asign speed.

