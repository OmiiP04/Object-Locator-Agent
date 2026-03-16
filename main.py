import speech_recognition as sr
from dotenv import load_dotenv
import os
from openai import OpenAI
from system_prompt import system_prompt
import pyttsx3
import tkinter as tk

# Voice setup
listener = sr.Recognizer()
try:
    engine = pyttsx3.init()
except:
    engine = None

def speak(text):
    if engine:
        engine.say(text)
        engine.runAndWait()

def listen():
    with sr.Microphone() as mic:
        status_label.config(text="Listening...")
        audio = listener.listen(mic)

    try:
        command = listener.recognize_google(audio)
        return command.lower()
    except:
        return ""

def ask_assistant():
    user_query = listen()

    if user_query == "":
        status_label.config(text="Couldn't understand")
        return

    text_box.insert(tk.END, "You: " + user_query + "\n")

    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ]
        )
        reply = response.choices[0].message.content
        text_box.insert(tk.END, "Assistant: " + reply + "\n\n")
        speak(reply)
        status_label.config(text="Ready")
    except Exception as e:
        text_box.insert(tk.END, f"Error: {str(e)}\n\n")
        status_label.config(text="Error")

def clear_chat():
    text_box.delete(1.0, tk.END)

# Load API
load_dotenv()
client = OpenAI(
    api_key=os.getenv("Apikey"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# GUI
root = tk.Tk()
root.title("Object Locator Assistant")
root.geometry("600x500")

text_box = tk.Text(root, height=20, width=70)
text_box.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

button = tk.Button(button_frame, text="🎤 Ask", command=ask_assistant, font=("Arial", 12))
button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_chat, font=("Arial", 12))
clear_button.pack(side=tk.LEFT, padx=5)

status_label = tk.Label(root, text="Ready", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()