import speech_recognition as sr
for i in range(0,1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something!')
        audio1 = r.listen(source)
        print ('Done!')
        text = r.recognize_google(audio1)
        print(text)
