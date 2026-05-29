import requests
from bs4 import BeautifulSoup
import anthropic
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv()
client = anthropic.Anthropic()

def scrape_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator="\n", strip=True)[:3000]
    except Exception as e:
        return f"Error scraping {url}: {e}"

def analyze(text, url):
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"""You are a competitive intelligence analyst. Be blunt and honest. Analyze this company's website and provide:
1. What they do (1 sentence)
2. Target customer
3. Key differentiator
4. Potential weakness an AI consultant could exploit as an opportunity
5. How to market myself using these tools 

Website: {url}

Content:
{text}"""
        }]
    )
    return response.content[0].text

# List of companies to analyze
companies = [
    "https://www.anthropic.com",
    "https://openai.com",
    "https://www.cohere.com"
]

results = []
for url in companies:
    print(f"Scraping {url}...")
    text = scrape_page(url)
    analysis = analyze(text, url)
    results.append({"url": url, "analysis": analysis})
    print(f"Done.\n")

# Print report
print("\n=== COMPETITIVE INTELLIGENCE REPORT ===")
for r in results:
    print(f"\n{r['url']}")
    print("-" * 40)
    print(r["analysis"])

# Save
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
outfile = f"intel_{timestamp}.json"
with open(outfile, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {outfile}")