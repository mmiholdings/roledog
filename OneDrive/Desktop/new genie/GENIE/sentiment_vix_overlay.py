
# Claude Sentiment vs VIX Overlay

import pandas as pd
import matplotlib.pyplot as plt

# Load historical Claude sentiment
claude = pd.read_csv("claude_sentiment_log.csv")
vix = pd.read_csv("vix_history.csv")  # date, vix

# Merge on date
merged = pd.merge(claude, vix, on="date")

# Plot
plt.figure(figsize=(12,6))
plt.plot(merged["date"], merged["sentiment"], label="Claude Sentiment", color="blue")
plt.plot(merged["date"], merged["vix"], label="VIX", color="red")
plt.axhline(0, linestyle="--", color="gray")
plt.title("Claude Sentiment vs VIX Curve")
plt.legend()
plt.grid()
plt.savefig("claude_vs_vix_overlay.png")
print("✅ Sentiment vs VIX chart generated.")
