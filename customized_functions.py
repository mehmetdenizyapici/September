from speech_engine import speak
import random

def name():
    speak(random.choice(["Oh, My name is Aurora", "I am Aurora", "You can call me Aurora"]))

def favorite_color():
    speak(random.choice(["My favorite color is White","White is my favorite color","I like White"]))

def liked_things():
    speak(random.choice(["Well, I like Books,  Workout, and  Computers","I like Books,  Workout, and  Computers"]))

def hated_things():
    speak(random.choice(["Well, I hate  Sweet perfume scent,  Exams, and Injuries","I hate  Sweet perfume scent,  Exams, and Injuries"]))

def pet():
    situation = random.choice(["Happy","Sad","Tired","Hungry","Sleepy"])
    speak(f"I have a fish, It's name is Alex, It is {situation} right now.")

def favorite_song():
    speak(random.choice(["My favorite song is Dear Mama","Dear Mama is my favorite song","I like to listen to Dear Mama"]))
    
def favorite_film():
    speak(random.choice(["My favorite film is The Matrix","The Matrix is my favorite film","I like to watch The Matrix"]))
    
def favorite_book():
    speak(random.choice(["My favorite book is 1984","1984 is my favorite book","I like to read 1984"]))