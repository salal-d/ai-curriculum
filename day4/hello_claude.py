import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is one thing an AI consultant should know about working with LLM APIs?"}
    ]
)

print(message.content[0].text)

model="claude-sonnet-4-20250514",

model="claude-sonnet-4-5",