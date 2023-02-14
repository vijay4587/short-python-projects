from gtts import gTTS
from playsound import playsound

booktext = open(r"C:\Users\vijay\OneDrive\Desktop\short projects\audio book\audio book.txt").read()
audio = gTTS(booktext)
audio.save("audio.mp3")
playsound("audio.mp3")
