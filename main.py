from dotenv import load_dotenv
import os
from openai import OpenAI
from system_prompt import system_prompt

def main():
    load_dotenv()
    GEMINI_API_KEY = os.getenv("Apikey")
    client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    user_query = input("Enter your query: ")
    
    response = client.chat.completions.create(
    model="gemini-2.5-flash",

    messages=[
        {   "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_query
        }
    ]
    )

    print(response.choices[0].message)


if __name__ == "__main__":
    main()
