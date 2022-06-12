from neuralintents import GenericAssistant
from functions import greeting, thanks, options, goodbye, hate, love, open_program, find_ip, open_whatsapp_web, get_latest_news, get_random_joke, get_random_advice, search_on_wikipedia, search_on_google, play_on_youtube, get_weather, input_type
from customized_functions import name, favorite_color, liked_things, hated_things, pet, favorite_song, favorite_book, favorite_film

import nltk

nltk.download("omw-1.4")

mapping = {"name":name,
           "favorite_color":favorite_color,
           "liked_things":liked_things,
           "hated_things":hated_things,
           "pet":pet,
           "favorite_song":favorite_song,
           "favorite_book":favorite_book,
           "favorite_film":favorite_film,
           "greeting": greeting,
           "thanks": thanks,
           "options": options,
           "goodbye":goodbye,
           "hate": hate,
           "love": love,
           "open_program":open_program,
           "find_ip":find_ip,
           "open_whatsapp_web":open_whatsapp_web,
           "get_latest_news":get_latest_news,
           "get_random_joke":get_random_joke,
           "get_random_advice":get_random_advice,
           "search_on_wikipedia":search_on_wikipedia,
           "search_on_google":search_on_google,
           "play_on_youtube":play_on_youtube,
           "get_weather":get_weather} 

assistant = GenericAssistant("intents.json",intent_methods=mapping)
assistant.train_model()

while True:
    try:
        message = input_type()
        assistant.request(message)
    
    except KeyboardInterrupt:
        break
    
    except Exception as e:
        print(e)