import threading
import time
from vosk import Model, KaldiRecognizer
from vosk import SetLogLevel
import pyaudio
import easyimap as e
import pyttsx3
from tkinter import*
from PIL import ImageTk,Image
import smtplib
import re


SetLogLevel(-1)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()


def listen():

    model = Model(r"C:\Users\kamal\vosk-model-en-in-0.5\vosk-model-en-in-0.5")
    recognizer = KaldiRecognizer(model, 16000)
    str="speak now"
    speak(str)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        try:
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()
                return text[14:-3]
        except:
            str("sorry could not recognize what you said")
            speak(str)
            return

def login():
    uname = ['voice8151@gmail.com', 'kamalesh21082002@gmail.com']
    passw = ['zocvphzhmlcbxzfe', 'eqcmgonkxllimvzc']
    print("=========================================")
    str="SAY THE SERIAL NUMBER TO SELECT AN EMAIL ID"
    speak(str)


    str="SPEAK EXIT TO EXIT"
    speak(str)

    str="first email id VOICE8151@GMAIL.COM"
    speak(str)

    str = "second email id KAMALESH21082002@gmail.COM"
    speak(str)
    print("=========================================")

    ch=listen()


    if (ch == "two" or ch == "though" or ch == 'to' or ch == 'too'):
        ch = "2"
        print(uname[0],passw[0])
        cred=[uname[0],passw[0]]
        return cred
        str="login successful"
        speak(str)

    elif (ch == "one" or ch == "on" or ch == "n"):

        ch = "1"
        cred=[uname[1],passw[1]]
        return cred
        str = "login successful"
        speak(str)


    elif (ch == 'exit' or ch == 'agreed' or ch == 'exit exit'):
        str = "you have chosen to exit,bye bye"
        speak(str)
        exit(1)

    else:
        login()

def sendmail(unm,pwd):
    global msg
    rec = "kamales21082002@gmail.com"
    str = "please speak the body of your email"
    speak(str)
    msg = listen()
    str = "you have spoken"
    speak(str)
    speak(msg)
    str = "speak OK to confirm sending email   speak AGAIN to say the body again   speak something to return to main menu"
    speak(str)
    c = listen()

    if(c == 'okay' or c == 'ok' or c == 'k'):
        str = "the email is getting processed"
        speak(str)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(unm, pwd)
        server.sendmail(unm, rec, msg)
        server.quit()
        str = "the email has been sent"
        speak(str)

    elif(c == 'again'):
        sendmail(unm,pwd)

    else:
        return

def readmail(unm,pwd):
    server = e.connect("imap.gmail.com",unm,pwd)
    server.listids()

    str = "please say the serial number"
    speak(str)
    a = listen()
    str = "you have spoken"
    speak(str)
    speak(a)
    str = "speak OK to confirm    speak AGAIN to say the serial number again"
    speak(str)
    ch1 = listen()
    if(ch1 == "okay" or ch1 == "ok" or ch1 == "k"):
        if(a == "free" or a == "three" or a == "tree"):
            a = "3"
        elif(a == "two" or a == "though" or a == 'to' or a == 'too'):
            a = "2"
        elif(a == "one" or a == "on" or a == "n"):
            a = "1"
        elif(a == "four" or a == "for" or a == "far"):
            a = "4"
        elif(a == "five" or a == "fi" or a == "phi"):
            a = '5'
        elif(a == "six" or a == "sex" or a == "x"):
            a = '6'
        elif(a == "seven" or a == "even" or a == "sound"):
            a = '7'
        elif(a == "eight" or a == "eid" or a == "height"):
            a = '8'
        elif(a == "nine" or a == "fine"):
            a = '9'
        b = int(a)-1

        email = server.mail(server.listids()[b])

        str = "the email is from:"
        speak(str)
        speak(email.from_addr)
        str = "the subject of the email is:"
        speak(str)
        speak(email.title)
        str = "the body of the email is :"
        speak(str)
        speak(email.body)
    elif(ch1 == "again"):
        readmail(unm,pwd)

# def login():
#     global unm,pwd
#     list = globals()
#     print("=========================================")
#     str="SAY THE SERIAL NUMBER TO SELECT AN EMAIL ID"
#     speak(str)
#
#
#     str="SPEAK EXIT TO EXIT"
#     speak(str)
#
#     str="first email id VOICE8151@GMAIL.COM"
#     speak(str)
#
#     str = "second email id KAMALESH21082002@gmail.COM"
#     speak(str)
#     print("=========================================")
#
#     ch=listen()
#
#
#     #if (ch == "two" or ch == "though" or ch == 'to' or ch == 'too'):
#     if(True):
#         ch = "2"
#         list['unm'] = "voice8151@gmail.com"
#         list['pwd'] = "zocvphzhmlcbxzfe"
#
#         str="login successful"
#         speak(str)
#
#     elif (ch == "one" or ch == "on" or ch == "n"):
#         ch = "1"
#         list['unm'] = "kamalesh21082002@gmail.com"
#         list['pwd'] = "eqcmgonkxllimvzc"
#
#         str = "login successful"
#         speak(str)
#
#
#     elif (ch == 'exit' or ch == 'agreed' or ch == 'exit exit'):
#         str = "you have chosen to exit,bye bye"
#         speak(str)
#         exit(1)
#
#     else:
#         login()

str="Please select the mail id to continue"
speak(str)


if __name__=="__main__":
    creds = login()
    while (1):
        print("===============================================================")
        str = "what do you want to do?"
        speak(str)

        str = "speak SEND to send email  speak READ to read email   speak EXIT to exit"
        speak(str)

        ch = listen()

        if (ch == 'send' or ch == 'and' or ch == 'sen' or ch == 'sending' or ch == 'send send' or ch == 'se' or ch == 'singh' or ch == 'sindhu'):
            str = "you have selected send option"
            speak(str)
            sendmail(creds[0],creds[1])

        elif (ch == 'read' or ch == 'raid' or ch == 'greed' or ch == 're' or ch == 'read read' or ch == 'eid' or ch == 'aid' or ch == 'freed'):
            str = "you have selected read a mail"
            speak(str)
            readmail(creds[0],creds[1])
        elif (ch == 'exit' or ch == 'agreed' or ch == 'exit exit'):
            str = "you have chosen to exit,bye bye"
            speak(str)
            exit(1)
        else:
            str = "Invalid choice,you said:"
            speak(str)
            speak(ch)

