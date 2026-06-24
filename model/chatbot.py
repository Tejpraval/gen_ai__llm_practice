# pyrefly: ignore [missing-import]

from email import message

from dotenv import load_dotenv
load_dotenv()


# pyrefly: ignore [missing-import]
from langchain.chat_models import init_chat_model

print("______welcome type 0 to exit from this application _______")
messages = []
while True:
    prompt = input("Enter your prompt::  ")
    messages.append(prompt)
    if prompt == "0":
        break
    model = init_chat_model("mistral-small-2603",temperature=0.9, max_tokens=100)
    res = model.invoke(messages)
    print("BOT :: ",res.content)
    print(messages)
