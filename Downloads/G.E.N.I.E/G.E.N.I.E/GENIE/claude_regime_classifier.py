
# Claude Market Regime Classifier

import requests
import pandas as pd

def classify_market():
    sentiment = pd.read_csv("claude_sentiment_log.csv").tail(7)["sentiment"].mean()
    vix = pd.read_csv("vix_history.csv").tail(7)["vix"].mean()

    prompt = f"""
You are a macroeconomic strategist. Based on:
- 7-day avg sentiment: {sentiment}
- 7-day avg VIX: {vix}

Classify the current market regime as one of:
- Trending Bull
- Ranging Consolidation
- Volatile Distribution
- Capitulation
- Low-Vol Drift

Explain in 3 bullets.
"""

    response = requests.post("https://your-api.com/claude-regime", json={"prompt": prompt})
    print("📊 Market Regime:", response.text)

if __name__ == "__main__":
    classify_market()
