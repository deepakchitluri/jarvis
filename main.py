import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voices[0].id)
#print(rate)


def speak(text):
#speak function will pronounce the string which we pass
    engine.say(text)
    engine.runAndWait()

def greet():
#greet function is used to greet me
    hour = datetime.datetime.now().hour
    if hour>=0 and hour <12:
        speak("Good morning"+master)
    elif hour>=12 and hour <16:
        speak("Good afternoon"+master)
    else:
        speak("good evening"+master)

def wishMe():
#wishMe function says time everytime i run jarvis
    hour = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    time = f"{hour}:{min}"
    print(time)
    rnti = f"right now the time is {time}"
    speak(rnti)

def takeCommand():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query} \n")
    except Exception as e:
        print("say that again please!")
        speak("say that again please!")
        query = None
    return query

#logic for executing tasks as per the query

"""
def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    speak("please enter your gmail eddress...")
    print("please enter your gmail eddress...")
    mail1 = input()
    speak("please enter your password...")
    print("please enter your password...")
    pass1 = input()
    server.ehlo()
    server.starttls()
    server.login(mail1, pass1)
    print("please enter the email address that you want to send email...")
    speak("please enter the email address that you want to send email...")
    tmail = input()
    print("please enter the content here...")
    speak("please enter the content here...")
    conte = input()
    server.sendmail(tmail,"",conte)
    print(f"mail has been succesfully sent to {tmail} ")
    speak("mail has been succesfully sent to corresponding address")
    server.close()
    del mail1
    del pass1
    del tmail
    del conte
"""

def fblogin():
    from selenium import webdriver
    # Open Firefox
    browser = webdriver.Chrome()
    # Go to the Facebook URL
    browser.get("http://www.facebook.com")
    print( "Enter the username")
    speak("enter your email address...")
    u1=input()
    print("Enter the password")
    speak("Enter your password...")
    u2 = input()
    uname = browser.find_element_by_id('email')
    psword = browser.find_element_by_id('pass')
    submit = browser.find_element_by_id("loginbutton")
    # Send the details to respective fields
    uname.send_keys(u1)
    psword.send_keys(u2)
    # Automate Click Login
    speak("Automating your login details...")
    submit.click()
    print("Done")
    speak("It's done....")
    print("It's done...")

def myWords():
    query = takeCommand()
    query = query.lower()
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")
    elif 'open facebook' in query:
        webbrowser.open("www.facebook.com/login")
    elif 'open google' in query:
        webbrowser.open("www.google.co.in")
    elif 'search internet for' in query:
        speak('searching in internet')
        query = query.replace("search internet for","")
        webbrowser.open(query)
    elif 'who are you' in query:
        result = '''Iam an Artificial Intelligent system that functions as your's assistant, running and taking care of all the internal systems of 
        your accessories. '''
        speak(result)
    elif 'play music' in query:
        speak("playing music...")
        songs_dir="D:\\video songs"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
    elif 'the time' in query:
        wishMe()

    elif 'open python' in query:
        speak("opening your software...")
        charmPath ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
        os.startfile(charmPath)
    elif 'login facebook' in query:
        fblogin()
    elif 'exit' or 'close' in query:
        exit()
#MAIN program starts here
speak("hi, how do i address you ? sir... or mam... ?")
ades = takeCommand()
ades = ades.lower()
if 'mam' in ades:
    master = "Mam"
else:
    master = "sir"
# speak(f"could you please tell me your name {master}?")
# fr = takeCommand()
# fr = fr.lower()
# master = f"{master} {fr}"
speak("Initialising jarvis...")
print("Intialising jarvis...")
greet()
speak(f"What can i do for you {master}?")
myWords()
while(True):
    speak("Is there anything else i can do for you sir ?..")
    ddr=takeCommand()
    ddr= ddr.lower()
    if "yes" in ddr:
        speak("please tell me the command sir...")
        myWords()
        continue
    elif "no" in ddr:
        break



