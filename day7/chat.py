import anthropic
from dotenv import load_dotenv
from datetime import datetime
import json
import os

load_dotenv()

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a helpful AI consulting assistant.
Keep answers concise and practical."""

conversation_history = []

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"conversation_{timestamp}.json"

print("AI Consulting Assistant (type 'quit' to exit)")
print(f"Saving conversation to: {log_file}")
print("-" * 40)

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )

    assistant_message = response.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    print(f"Assistant: {assistant_message}")
    print()

with open(log_file, "w") as f:
    json.dump({
        "timestamp": timestamp,
        "conversation": conversation_history
    }, f, indent=2)

print(f"Conversation saved to {log_file}")