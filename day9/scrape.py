import requests
from bs4 import BeautifulSoup
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

def scrape_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Remove noise
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    
    text = soup.get_text(separator="\n", strip=True)
    return text[:3000]  # limit to avoid token overflow

def classify(text, url):
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"This text was scraped from {url}. In 3 bullet points summarize what the company does, who their target customer is, and one business opportunity for an AI consultant:\n\n{text}"
        }]
    )
    return response.content[0].text

# Test on a real company
url = "https://www.anthropic.com"
print(f"Scraping {url}...")
text = scrape_page(url)

print("Sending to Claude...")
result = classify(text, url)

print("\n=== ANALYSIS ===")
print(result)