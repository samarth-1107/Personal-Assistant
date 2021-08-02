# Import Modules/Packages/Libraries

import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os

# initiate Engine & Voice

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)

# Set Voice

engine.setProperty('voice', voices[1].id)


# Create Speak Functionality

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Greet the user according to the present time

def greet_user():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif time >= 12 and time < 16:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("I am Shivi, your personal assistant. How may I help you?")
    speak("I am Shivi, your personal assistant. How may I help you?")


# Take Commands from the user

def take_user_commands():

    # Take Input from user (microphone) and return string o/p

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")
    except Exception as e:
        # print(e)

        # speak("Sorry! Can you please say that again?")

        return "None"
    return query


# Main Method

if __name__ == '__main__':

    # Executing Commands/Tasks

    greet_user()
    condition = True

    # Runs Infinite times

    while condition:
        query = take_user_commands().lower()

        # Search from Wikipedia

        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        # Open YouTube

        elif 'open youtube' in query:
            print("Opening YouTube...")
            speak("Opening YouTube...")
            webbrowser.open("youtube.com")

        # Open Google

        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("google.com")

        # Open 'Movies' folder in your system

        elif 'open movies' in query:
            print("Opening Movies, Enjoy!...")
            speak("Opening Movies, Enjoy!...")
            dir_movies = f"C:/Users/SAMARTH/Videos/Movies"
            movies = os.listdir(dir_movies)
            os.startfile(dir_movies)

        # Tells the current time (HH:MM)

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is {str_time}")
            speak(f"The time is {str_time}")

        # Goes to sleep (Loop Terminates)

        elif 'go to sleep' in query or 'ok bye' in query:
            print("Yeah sure. Bye!")
            speak("Yeah sure. Bye!")
            condition = False
