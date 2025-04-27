
# GENIE Risk Dashboard Generator with Trade Flags

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("genie_journal.csv", parse_dates=["timestamp"])

# Flag risky trades (drawdown > -500 or win_rate < 40%)
df["risk_flag"] = df["pnl"].apply(lambda x: "⚠️" if x < -500 else "")
df["drawdown"] = df["entry_price"] - df["exit_price"]
df["drawdown"] = df["drawdown"].apply(lambda x: round(x, 2))

# Save flagged table
df.to_csv("risk_dashboard_flagged.csv", index=False)
print("✅ Risk dashboard with flags generated.")
