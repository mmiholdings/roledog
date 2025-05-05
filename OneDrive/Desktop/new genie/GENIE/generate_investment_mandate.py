
# GENIE Investment Mandate Generator

import requests
from datetime import datetime

def generate_mandate():
    journal_data = open("genie_journal.csv").read()
    prompt = f"""
You're an AI portfolio strategist. Based on the trade journal below, current market conditions, and risk trends—write a 1-page Investment Mandate for GENIE.

Include:
- Current market regime (trend, volatility, bias)
- Active strategies and preferred MARL agents
- Asset class focus
- Risk controls (position sizing, volatility exposure)
- Hedging methodology
- Trade filtering rules

DATA:
{journal_data}
"""

    response = requests.post("https://your-api.com/gpt-mandate", json={"prompt": prompt})
    mandate = response.text
    filename = f"mandates/investment_mandate_{datetime.now().date()}.txt"
    with open(filename, "w") as f:
        f.write(mandate)
    print("✅ Investment Mandate saved:", filename)

if __name__ == "__main__":
    generate_mandate()
