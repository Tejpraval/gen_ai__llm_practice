import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

if not os.getenv("MISTRAL_API_KEY"):
    raise RuntimeError("Set MISTRAL_API_KEY in model/.env before running this script.")

model = init_chat_model(
    model="mistral-small-2603",
    model_provider="mistralai",
    temperature=1.0,
)

messages = [
    SystemMessage(
        content=(
             "Ask easy GK questions one at a time. When the user answers, "
            "roast every answer i give and be a bully by using a decent foul language , but also give the correct answer if wrong and explain it in a simple way. "
        )
    ),
    HumanMessage(content="Start the quiz."),
]

print("Type 'exit' to stop.\n")

res = model.invoke(messages)
print(f"AI: {res.content}\n")
messages.append(AIMessage(content=res.content))

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in {"exit", "quit"}:
        break
    if not user_input.strip():
        print("Please type an answer, or type 'exit' to stop.\n")
        continue

    messages.append(HumanMessage(content=user_input))

    res = model.invoke(messages)
    print(f"AI: {res.content}\n")
    messages.append(AIMessage(content=res.content))
