#pip install pipwin
#pipwin install pyaudio
#pip install playsound
#pip install speechrecognition
#pip install pywhatkit
#pip install gtts
#pip install lxml
import selenium
import webbrowser
import pywhatkit
from pywhatkit import search
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import requests
from lxml import html
import googletrans
from googletrans import Translator
import bs4

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#engine.setProperty('voice', voices[1].id) eğer asistan erkekse

engine.say("hi babe i am alexa")
engine.say("what can I do for you")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommands():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command=''
            try:
                command = listener.recognize_google(voice)
                #command = listener.recognize_google(voice, language='tr-TR')# if you want TR launguage
                print(command)
            except sr.UnknownValueError:
                print("i didn't get that")
            except sr.RequestError:
                print("i didn't know that")
            return command
    except:
        pass
#    return command

def runAlexa():
    command = takeCommands().lower()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        partOfDay = datetime.now()
        time = datetime.now().strftime('%H:%M:%S')
        print(time)
        talk("current time is " + time)
        if partOfDay.hour < 12 and partOfDay.hour > 6:
            morning ="good morning most powerful streamer"
            print(morning)
            talk(morning)
        elif partOfDay.hour >= 12 and partOfDay.hour < 16:
            afternoon = "good afternoon"
            print(afternoon)
            talk(afternoon)
        elif partOfDay.hour >= 16 and partOfDay.hour < 23:
            evening = "good evening"
            print(evening)
            talk(evening)
        else:
            night = "good night"
            print(night)
            talk(night)
    elif 'search' in command:
        search = command.replace('search','')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
    elif 'day' in command:
        day = datetime.today().weekday()+1
        days = {1: 'Monday' , 2: 'Tuesday' , 3 :'Wednesday' , 4: 'Thursday' , 5: 'Friday' , 6:'Saturday', 7: 'Sunday'}
        if day in days.keys():
            today = days[day]
            print(today)
            talk("today is " + today)
            if 5 or 6 in days.keys():
                weekend = "have a good weekend"
                print(weekend)
                talk(weekend)
            else :
                weekday ="have a good weekday , I wish you good work"
                print(weekday)
                talk(weekday)
    elif 'dollar' in command:
        r = requests.get("https://uzmanpara.milliyet.com.tr/canli-borsa/")
        tree = html.fromstring(r.content)
        dollar = tree.xpath('//*[@id="usd_header_son_data"]')
        sayDollar = "1 dollar now {} Turkish liras".format(dollar[0].text)
        print(sayDollar)
        talk(sayDollar)
    elif 'euro' in command:
        r = requests.get("https://uzmanpara.milliyet.com.tr/canli-borsa/")
        tree = html.fromstring(r.content)
        euro = tree.xpath('//*[@id="eur_header_son_data"]')
        sayEuro = "1 euro now {} Turkish liras".format(euro[0].text)
        print(sayEuro)
        talk(sayEuro)
    elif 'gold' in command:
        r = requests.get("https://uzmanpara.milliyet.com.tr/canli-borsa/")
        tree = html.fromstring(r.content)
        gold = tree.xpath('//*[@id="gld_header_son_data"]')
        sayGold = "1 gold now {} Turkish liras".format(gold[0].text)
        print(sayGold)
        talk(sayGold)
    elif 'translate' in command:
        translate = command.replace('translate','')
        translator = Translator()
        dedectedTranslate = translator.detect(translate)
        translation = translator.translate(text=translate , dest='tr')
        print(translation.text)
        talk(translation.text)
while True:
    runAlexa()
