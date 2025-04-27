
# Aggregate Risky Trades by Weekday

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("genie_journal.csv", parse_dates=["timestamp"])
df["weekday"] = df["timestamp"].dt.day_name()
df["is_risky"] = df["pnl"] < -500

risk_by_day = df.groupby("weekday")["is_risky"].sum().reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

plt.figure(figsize=(10,6))
risk_by_day.plot(kind="bar", color="red")
plt.title("Risky Trades by Weekday (PnL < -$500)")
plt.ylabel("Count")
plt.xlabel("Weekday")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("risky_trades_by_weekday.png")
print("✅ Dashboard generated: Risky Trades by Weekday")
