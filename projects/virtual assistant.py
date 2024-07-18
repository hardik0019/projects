import pyttsx3
import speech_recognition as sr
import requests
import pyjokes
import time
from webscout import Phindv2

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio)

        return text
    
def operation(text):
    if "joke" in text:
        joke  = pyjokes.get_joke()
        speak(joke)
    elif "search" in text:
        ph = Phindv2()
        response = ph.ask(text)
        message = ph.get_message(response)
        print(message)
        speak(message)


if __name__ == "__main__":
    speak("Hello Sir! how can I assist you!!")
    time.sleep(3)
    print("Say Something")
    text = listen()
    print(text)
    operation(text)


    

