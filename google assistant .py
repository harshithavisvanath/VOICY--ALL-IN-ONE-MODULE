import speech_recognition as sr
import os
import openpyxl
import webbrowser
from docx import Document
from openpyxl import Workbook
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something!')
        audio1 = r.listen(source)
        print ('Done!')
    text = r.recognize_google(audio1)
    text1=text.lower()
    return text1
def open_app(textt):

    if textt.startswith("chrome"): 
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    elif textt.startswith("i"): 
        webbrowser.open('http://www.google.com')
    elif textt.startswith("w"): 
        os.system("start test.docx")
    elif textt.startswith("e"):
        wb=Workbook()
        ws=wb.active
        wb.save("sample.xlsx")
        os.system("sample.xlsx")
    else:
        print("no")
textt=speak()
print(textt)
open_app(textt)            
