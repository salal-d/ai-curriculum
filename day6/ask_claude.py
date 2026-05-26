import pandas as pd
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

# Load and clean
df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["satisfied"] = df["satisfied"].map({"yes": True, "no": False})

# Build summary to send to Claude
summary = f"""
Here is consulting business data:

Total revenue: ${df['revenue'].sum():,}
Total projects: {len(df)}
Satisfaction rate: {df['satisfied'].mean()*100:.0f}%

Revenue by industry:
{df.groupby('industry')['revenue'].sum().sort_values(ascending=False).to_string()}

Revenue by project type:
{df.groupby('project_type')['revenue'].mean().sort_values(ascending=False).to_string()}

Unsatisfied clients:
{df[df['satisfied']==False][['client','project_type','revenue']].to_string()}
"""

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": f"You are a business analyst. Analyze this consulting data and give 3 specific, actionable recommendations:\n{summary}"
    }]
)

print(response.content[0].text)