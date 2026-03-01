import speech_recognition as sr
from dotenv import load_dotenv
import os
from openai import OpenAI
from system_prompt import system_prompt
import pyttsx3

# ---------- VOICE SETUP ----------
listener = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as mic:
        print("Listening...")
        listener.adjust_for_ambient_noise(mic)
        audio = listener.listen(mic)

    try:
        command = listener.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Could not understand audio.")
        return ""

# ---------- MAIN ----------
def main():
    print("Program started")

    load_dotenv()
    GEMINI_API_KEY = os.getenv("Apikey")

    client = OpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    user_query = listen()

    if user_query == "":
        return

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )

    reply = response.choices[0].message.content
    print(reply)
    speak(reply)

if __name__ == "__main__":
    main()