import random

from art import text2art
from speech_engine import speak


default_functions = open("default_functions.py","r").read()
customized_functions  = open("customized_functions.py", "w+")

print(text2art("September"))

speak("Hello, I am September. I am here to help you to create your own Virtual Assistant.")
print("Hello, I am September. I am here to help you to create your own Virtual Assistant.")

speak("I am going to ask you some questions, I want you to write the answer.")
print("I am going to ask you some questions, I want you to write the answer.")

speak("Do you want to choose the name of your Virtual Assistant.")
name = input("Do you want to choose the name of your Virtual Assistant (If yes, please type the name, else please type enter):")
if name == "":
    name = random.choice(["Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper", "Luna", "Camila", "Gianna", "Elizabeth", "Eleanor", "Ella", "Abigail", "Sofia", "Avery", "Scarlett", "Emily", "Aria", "Penelope", "Chloe", "Layla", "Mila", "Nora", "Hazel", "Madison", "Ellie", "Lily", "Nova", "Isla", "Grace", "Violet", "Aurora", "Riley", "Zoey", "Willow", "Emilia", "Stella", "Zoe", "Victoria", "Hannah", "Addison", "Leah", "Lucy", "Eliana", "Ivy", "Everly"])

speak("Choose a music genre.")
music_genre = input("Choose music genre (Rock, Rap, Pop):").lower()
if music_genre == "rock": favorite_music = random.choice(["Stairway to Heaven", "Bohemian Rhapsody", "Hotel California", "Free Bird", "Purple Haze", "Comfortably Numb"])
elif music_genre == "rap": favorite_music = random.choice(["Fight the Power","Top Billin","The World is Yours","Dear Mama","The Message","I used to love her"])
elif music_genre == "pop": favorite_music = random.choice(["Single Ladies","Umbrella","Shake it Off","Toxic","Rolling in the Deep","Firework","Rehab"])
else: favorite_music = random.choice(["Bad and Boujee","Africa","Bam Bam","Respect","A Change Is Gonna Come","Like a Rolling Stone"])


speak("Choose a film genre.")
film_genre = input("Choose a film genre (Action, Comedy, Crime, Horror, Romace):").lower()
if film_genre == "action": favorite_film = random.choice(["Apocalypse Now","The Matrix","Gladiator","Mad Max","Terminator"])
elif film_genre == "comedy": favorite_film = random.choice(["The Jerk","Groundhog Day","This is Spinal Tap","Wayne's World","Blazing Saddles","Best in Show"])
elif film_genre == "crime": favorite_film = random.choice(["The Godfather","Heat","Goodfellas","L.A. Confidential","Scarface"])
elif film_genre == "horror": favorite_film = random.choice(["American Pyscho","Get Out","Us","Alien","King Kong","The Invisible Man","A Quiet Place"])
elif film_genre == "romance": favorite_film = random.choice(["Annie Hall","The Apartment","Punch-Drunk Love","Wall-e","Up"])
else: favorite_film = random.choice(["The Godfather","12 Angry Men","Casablanca","Rear Window","City Lights","Pulp Fiction"])

speak("Choose a book genre?")
book_genre = input("Choose a book genre (Fantasy, Dystopian, Adventure, Mystery, Historical, Romance):")
if book_genre == "fantasy": favorite_book = random.choice(["Alice's Adventures in Wonderland","The Hobbit","The Sword in the Stone","The Last Unicorn","A Wizard"])
elif book_genre == "dystopian": favorite_book = random.choice(["The Hunger Games","1984","Divergent","Brave New World","Fahrenheit 451"])
elif book_genre == "adventure": favorite_book = random.choice(["The Three Musketeers","Treasure Island","King Solomon's Mines","Journey to the Center of the Earth"])
elif book_genre == "mystery": favorite_book = random.choice(["And Then There Were None","The Big Sleep","Gone Girl","The Postman Always Rings Twice","In Cold Blood"])
elif book_genre == "historical": favorite_book = random.choice(["What Is History","Lies My Teacher Told Me","Democracy: A Life","Salt: A World History","A Short History of Nearly Everything"])
elif book_genre == "romance": favorite_book = random.choice(["Outlander","Jane Eyre","Gone with the wind","Sense and Sensibility","The notebook"])
else: favorite_book = random.choice(["Pride and Prejudice","1984","Crime and Punishment","Hamlet","Anna Karenina"])

speak("Tell me 5 things you like")
things_liked = random.sample(input("Write 5 things you like (with commas between them):").split(","),3)
liked1 = things_liked[0]
liked2 = things_liked[1]
liked3 = things_liked[2]

speak("Tell me 5 things you hate")
things_hated = random.sample(input("Write 5 things you hate (with commas between them):").split(","),3)
hated1 = things_hated[0]
hated2 = things_hated[1]
hated3 = things_hated[2]

favorite_color = random.choice(["Blue","Red","Red","Purple","Black","Orange","Yellow","Gold","White","Pink"])
pet_type = random.choice(["fish","cat","dog","bird"])
pet_name = random.choice(["Abigail", "Ace", "Adam", "Addie", "Admiral", "Aggie", "Aires", "Aj", "Ajax", "Aldo", "Alex", "Alexus", "Alf", "Alfie", "Allie", "Ally", "Amber", "Amie", "Amigo", "Amos", "Amy", "Andy", "Angel", "Angus", "Annie", "Apollo", "April", "Archie", "Argus", "Aries", "Armanti", "Arnie", "Arrow", "Ashes", "Ashley", "Astro", "Athena", "Atlas", "Audi"])

default = ["DEFAULTNAME",
           "DEFAULTCOLOR",
           "LIKED1",
           "LIKED2",
           "LIKED3",
           "HATED1",
           "HATED2",
           "HATED3",
           "DEFAULTTYPE",
           "DEFAULTPETNAME",
           "DEFAULTSONG",
           "DEFAULTFILM",
           "DEFAULTBOOK"]

custom = [name,
          favorite_color,
          liked1,
          liked2,
          liked3,
          hated1,
          hated2,
          hated3,
          pet_type,
          pet_name,
          favorite_music,
          favorite_film,
          favorite_book]

speak(f"That's it. Now, Please give me time to create {name}, your new virtual assistant.")
speak("Please do not touch anything")

for i in range(len(custom)):
    default_functions = default_functions.replace(default[i], custom[i])
customized_functions.write(default_functions)

speak(f"Now, All you have to do is to start desktop_assistant.py")
speak("Press Anything to Close the Program")
input("Press Anything to Close the Program")
