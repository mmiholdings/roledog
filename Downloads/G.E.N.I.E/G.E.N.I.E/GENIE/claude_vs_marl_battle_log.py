
# Claude vs MARL Signal Battle Log

import pandas as pd

df = pd.read_csv("genie_journal.csv")

results = []
for _, row in df.iterrows():
    claude = row.get("claude_direction")
    marl = row.get("strategy")
    pnl = row.get("pnl")

    winner = "Claude" if ((claude == "BUY" and pnl > 0) or (claude == "SELL" and pnl < 0)) else "MARL"
    results.append({"timestamp": row["timestamp"], "claude": claude, "marl": marl, "pnl": pnl, "winner": winner})

battle_df = pd.DataFrame(results)
battle_df.to_csv("claude_vs_marl_battle_log.csv", index=False)
print("🤖 Claude vs MARL journal generated.")
