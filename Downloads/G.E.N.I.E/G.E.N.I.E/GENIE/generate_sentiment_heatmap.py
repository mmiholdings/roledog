
# Claude Sentiment Heatmap

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("claude_sentiment_log.csv", parse_dates=["date"])
df["day"] = df["date"].dt.date
df["hour"] = df["date"].dt.hour

pivot = df.pivot_table(index="hour", columns="day", values="sentiment", aggfunc="mean")
plt.figure(figsize=(12,6))
sns.heatmap(pivot, cmap="coolwarm", center=0, annot=True)
plt.title("Claude Sentiment Heatmap (Hourly)")
plt.savefig("claude_sentiment_heatmap.png")
