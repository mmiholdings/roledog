
# Claude/GPT Plans Tomorrow's Market Strategy

import requests

def generate_trade_plan():
    prompt = """
You're GENIE's head of strategy. Based on current market conditions, sentiment data, and trade journal summaries — what is the recommended trading plan for tomorrow?

Include:
1. Strategy bias (bullish/bearish/neutral)
2. Sector focus
3. Instruments to avoid
4. Risk adjustments
"""
    response = requests.post("https://your-api.com/gpt-plan", json={"prompt": prompt})
    summary = response.text
    with open("daily_trade_plan.txt", "w") as f:
        f.write(summary)
    print("✅ Daily trade plan saved.")

if __name__ == "__main__":
    generate_trade_plan()
