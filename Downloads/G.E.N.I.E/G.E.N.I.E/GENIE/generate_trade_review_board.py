
# Claude-Generated Trade Review Board (Weekly)

import pandas as pd
import requests
from datetime import datetime

def generate_review_board():
    df = pd.read_csv("genie_journal.csv", parse_dates=["timestamp"])
    df_last_week = df[df["timestamp"] > (pd.Timestamp.now() - pd.Timedelta(days=7))]

    best_trades = df_last_week.sort_values("pnl", ascending=False).head(3)
    worst_trades = df_last_week.sort_values("pnl").head(3)

    prompt = f"""
You are GENIE's head of trading performance. Review the following trades and write:
1. A brief analysis of why the top 3 trades worked
2. What went wrong with the 3 worst trades
3. A lesson or improvement idea

BEST TRADES:
{best_trades.to_csv(index=False)}

WORST TRADES:
{worst_trades.to_csv(index=False)}
"""

    response = requests.post("https://your-api.com/claude-review", json={"prompt": prompt})
    summary = response.text
    filename = f"trade_reviews/weekly_review_{datetime.now().date()}.txt"

    with open(filename, "w") as f:
        f.write(summary)

    print(f"✅ Weekly Trade Review Board saved to: {filename}")

if __name__ == "__main__":
    generate_review_board()
