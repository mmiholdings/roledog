
# Plot Claude vs MARL Win Rates Over Time

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("claude_vs_marl_battle_log.csv", parse_dates=["timestamp"])
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["day"] = df["timestamp"].dt.date

daily = df.groupby(["day", "winner"]).size().unstack(fill_value=0)
daily["Claude_win_rate"] = daily["Claude"] / (daily["Claude"] + daily["MARL"])

plt.figure(figsize=(12,6))
plt.plot(daily.index, daily["Claude_win_rate"], label="Claude Win Rate", color="blue", marker="o")
plt.axhline(0.5, linestyle="--", color="gray")
plt.title("Claude vs MARL Daily Win Rate")
plt.ylabel("Claude Win Rate")
plt.xlabel("Date")
plt.legend()
plt.grid()
plt.savefig("claude_vs_marl_win_rate_plot.png")
print("✅ Plot saved: Claude vs MARL Win Rate Over Time")
