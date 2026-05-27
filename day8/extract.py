from docx import Document
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

def extract_docx(filepath):
    doc = Document(filepath)
    text = ""
    for para in doc.paragraphs:
        if para.text.strip():
            text += para.text + "\n"
    return text

def summarize(text, filename):
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Summarize this document in 3 bullet points, then list any action items:\n\n{text}"
        }]
    )
    return response.content[0].text

# Extract and summarize
text = extract_docx("sample_report.docx")

print("=== EXTRACTED TEXT ===")
print(text)

print("\n=== CLAUDE SUMMARY ===")
summary = summarize(text, "sample_report.docx")
print(summary)