import pandas as pd
import anthropic
from dotenv import load_dotenv
from datetime import datetime
import json
import sys
import os

load_dotenv()
client = anthropic.Anthropic()

def load_and_profile(filepath):
    df = pd.read_csv(filepath)
    
    profile = {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_string() if not df.select_dtypes(include='number').empty else "No numeric columns",
    }
    
    # Sample rows as string
    profile["sample"] = df.head(5).to_string()
    
    return df, profile

def ask_claude(profile):
    prompt = f"""You are a hardcore data analyst. A client has given you a CSV file. Here is a profile of the data:

Rows: {profile['rows']}
Columns: {profile['columns']}
Data types: {profile['dtypes']}
Missing values: {profile['missing_values']}

Sample data:
{profile['sample']}

Numeric summary:
{profile['numeric_summary']}

Provide:
1. What this dataset appears to be about
2. Data quality issues to flag
3. Three business questions this data could answer
4. One concrete next step for the client
"""
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def save_output(filepath, profile, analysis):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output = {
        "timestamp": timestamp,
        "source_file": filepath,
        "profile": {k: v for k, v in profile.items() if k != "sample"},
        "analysis": analysis
    }
    outfile = f"analysis_{timestamp}.json"
    with open(outfile, "w") as f:
        json.dump(output, f, indent=2)
    return outfile

# Main
filepath = sys.argv[1] if len(sys.argv) > 1 else "../day6/sales_data.csv"

print(f"Loading {filepath}...")
df, profile = load_and_profile(filepath)

print("Sending to Claude...")
analysis = ask_claude(profile)

print("\n=== ANALYSIS ===")
print(analysis)

outfile = save_output(filepath, profile, analysis)
print(f"\nSaved to {outfile}")