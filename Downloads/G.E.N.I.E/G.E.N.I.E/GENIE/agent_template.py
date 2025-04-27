import time, json, os
from datetime import datetime
import random

AGENT_NAME = os.getenv("AGENT_NAME", "Reggie")
TICKER = os.getenv("TICKER", "MES")

while True:
    confidence = round(random.uniform(0.7, 1.0), 2)
    entry = round(random.uniform(5200, 5300), 2)
    exit = entry + round(random.uniform(0.5, 2.0), 2)
    pnl = round((exit - entry) * 50, 2)
    signal = {
        "agent": AGENT_NAME,
        "ticker": TICKER,
        "bias": "Bullish" if confidence > 0.8 else "Neutral",
        "confidence": confidence,
        "entry": entry,
        "exit": exit,
        "pnl": pnl,
        "timestamp": datetime.utcnow().isoformat()
    }

    os.makedirs("signals", exist_ok=True)
    with open(f"signals/{AGENT_NAME.lower()}.json", "w") as f:
        json.dump(signal, f, indent=2)
    print(f"[{AGENT_NAME}] Signal sent: {signal}")
    time.sleep(15)