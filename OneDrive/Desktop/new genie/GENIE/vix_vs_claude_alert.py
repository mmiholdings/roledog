
# Alert if VIX diverges from Claude Sentiment

import pandas as pd
import requests

def alert_if_divergent():
    df = pd.read_csv("merged_sentiment_vix.csv")
    recent = df.tail(1).iloc[0]
    sentiment = recent['sentiment']
    vix = recent['vix']

    if (sentiment > 0.5 and vix > 22) or (sentiment < -0.5 and vix < 16):
        text = f"⚠️ VIX divergence detected: Claude sentiment = {sentiment}, VIX = {vix}"
        requests.post("https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK", json={"text": text})

if __name__ == "__main__":
    alert_if_divergent()
