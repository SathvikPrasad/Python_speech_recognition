import speech_recognition as sr
import os
import time


def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            speech.i = text
        except:
            print("Sorry could not recognize what you said")


x = 2
while x == 2:
    speech()
    print(speech.i)
    time.sleep(3)
    name = speech.i.find('quit')
    if name != -1:
        x += 1
    else:
        pass


# pyinstaller.exe --onefile  speech.py
