import pywhatkit as kit
import speech_recognition as sr
import requests
import wikipedia
import webbrowser
import random
import sys
import pyautogui

from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from speech_engine import speak

#input types
def text_input():
    return input("I am listening:").lower()

def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
    except:
        query = "None"
    
    print("-->",query)
    return query.lower()

def take_input_type():
    question = input("How do you want to interact with your AI?(T for text / V for voice)")
    while not question in ("T","V"):
        question = input("How do you want to interact with your AI?(T for text / V for voice)")
    if question == "T":
        return text_input
    elif question == "V":
        return voice_input

input_type = take_input_type()

#reactions
def greeting():
    speak(random.choice(["Hello", "Hi", "Hi there, how can I help?", "Good to see you again."]))

def thanks():
    speak(random.choice(["Happy to help!", "Any time!", "My pleasure","You are welcome"]))

def options():
    speak(random.choice(["Those are my capabilities: I can open programs for you. I can check your ip adress. I can check weather and news for you. I can search things on wikipedia, google or youtube. I can send whatsapp messages. I can make very good jokes and give perfect advices.","Here is a list of my capabilities: I can open programs for you. I can check your ip adress. I can check weather and news for you. I can search things on wikipedia, google or youtube. I can send whatsapp messages. I can make very good jokes and give perfect advices.","Those are what I am able to do: I can open programs for you. I can check your ip adress. I can check weather and news for you. I can search things on wikipedia, google or youtube. I can send whatsapp messages. I can make very good jokes and give perfect advices."]))

def goodbye():
    speak(random.choice(["See you!", "Have a nice day", "Bye! Come back again soon.", "Goodbye!"])), 
    sys.exit()

def hate():
    speak(random.choice(["Really? I am sorry to hear that!", "Oh, Sorry to hear that!", "I am sorry to hear that."])), 

def love():
    speak(random.choice(["Really? I am happy to hear that!", "Oh, I am happy to hear that!", "Happy sorry to hear that."])), 

#functionalities    
def open_program():
    speak("Which program do you want me to start?")
    answer = input_type().lower()
    pyautogui.typewrite(["win"])
    pyautogui.typewrite(answer)
    pyautogui.typewrite(["enter"])

def find_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    ip_address =  ip_address["ip"]
    speak(f"Your ip address is {ip_address}")
    print(f"Your ip address is {ip_address}")

def open_whatsapp_web():
    webbrowser.open("https://web.whatsapp.com")

def get_latest_news():
    NEWS_API_KEY = "020326ffdd2e412e8c6666321a7d543a"
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    speak(news_headlines[:5])
    for x in news_headlines[:5]:
        print(x)

def get_random_joke():
    headers = {'Accept': 'application/json'}
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    speak(res["joke"])

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    speak(res['slip']['advice'])

def search_on_wikipedia():
    speak("What do you want me to research on wikipedia?")
    subject = input_type()
    try: 
        results = wikipedia.summary(subject, sentences=2)
        speak(results)
        print(results)
    except:
        results = wikipedia.summary(subject, sentences=2, auto_suggest=False)
        speak(results)
        print(results)

def search_on_google():
    speak("What do you want me to research on google?")
    subject = input_type()
    kit.search(subject)

def play_on_youtube():
    speak("What do you want me to play on youtube?")
    video = input_type()
    kit.playonyt(video)

def get_weather():
    speak("Which city do you want me to check the weather for?")
    city = input_type()
    city=city.replace(" ","+")
    city=city+" weather"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')   

    translator = GoogleTranslator(source='auto', target='en')
    
    location = translator.translate(soup.select('#wob_loc')[0].getText().strip())  
    time = translator.translate(soup.select('#wob_dts')[0].getText().strip())       
    info = translator.translate(soup.select('#wob_dc')[0].getText().strip()) 
    weather = translator.translate(soup.select('#wob_tm')[0].getText().strip() + "°C")
    
    
    speak(f"The current temperature is {weather} in {location}")
    speak(f"Also, the weather report talks about {info}")
    print(f"Location: {location}\nTemperature: {weather}\nTime: {time}\nInfo: {info}")
                        
                        
                        
                        