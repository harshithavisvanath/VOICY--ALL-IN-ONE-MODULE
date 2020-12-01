import speech_recognition as sr
import requests
import webbrowser as wb
r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something!')
    audio1 = r.listen(source)
    print ('Done!')
    text = r.recognize_google(audio1)
    url="https://www.google.com/search?q="+text
    wb.open(url)
