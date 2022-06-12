import pyttsx3

engine = pyttsx3.init("sapi5")

# Setting Rate
engine.setProperty("rate", 190)

# Set Volume
engine.setProperty("volume", 1.0)

# Set Voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Text to Speech Conversion
def speak(text):
    """To speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()
    