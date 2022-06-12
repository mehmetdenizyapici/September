from speech_engine import speak
import random

def name():
    speak(random.choice(["Oh, My name is DEFAULTNAME", "I am DEFAULTNAME", "You can call me DEFAULTNAME"]))

def favorite_color():
    speak(random.choice(["My favorite color is DEFAULTCOLOR","DEFAULTCOLOR is my favorite color","I like DEFAULTCOLOR"]))

def liked_things():
    speak(random.choice(["Well, I like LIKED1, LIKED2, and LIKED3","I like LIKED1, LIKED2, and LIKED3"]))

def hated_things():
    speak(random.choice(["Well, I hate HATED1, HATED2, and HATED3","I hate HATED1, HATED2, and HATED3"]))

def pet():
    situation = random.choice(["Happy","Sad","Tired","Hungry","Sleepy"])
    speak(f"I have a DEFAULTTYPE, It's name is DEFAULTPETNAME, It is {situation} right now.")

def favorite_song():
    speak(random.choice(["My favorite song is DEFAULTSONG","DEFAULTSONG is my favorite song","I like to listen to DEFAULTSONG"]))
    
def favorite_film():
    speak(random.choice(["My favorite film is DEFAULTFILM","DEFAULTFILM is my favorite film","I like to watch DEFAULTFILM"]))
    
def favorite_book():
    speak(random.choice(["My favorite book is DEFAULTBOOK","DEFAULTBOOK is my favorite book","I like to read DEFAULTBOOK"]))