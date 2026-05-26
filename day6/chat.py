import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a no-nonsense AI consulting assistant helping business professionals understand how to use AI in their companies.

Rules:
- Keep answers concise and practical
- Always tie advice back to business value
- If someone asks something outside AI consulting, redirect them back to the topic
- Never use jargon without explaining it"""

conversation_history = []

print("AI Consulting Assistant (type 'quit' to exit)")
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