
import pandas as pd
import logging

logging.basicConfig(filename="genie_agent_memory.log", level=logging.INFO)

def track(filepath="agent_performance.csv"):
    df = pd.read_csv(filepath)
    stats = df.groupby("agent").agg({
        "sharpe": ["mean", "min"],
        "pnl": "sum"
    }).round(2)
    logging.info(f"📊 Agent Metrics:\n{stats}")
    print("✅ Memory scores calculated. See logs.")

if __name__ == "__main__":
    track()
