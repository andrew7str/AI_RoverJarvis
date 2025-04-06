import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 130)

def speak(text):
    print("🤖 AI:", text)
    engine.say(text)
    engine.runAndWait()
