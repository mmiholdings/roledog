
import redis
import json
import time
import subprocess

r = redis.Redis(host='localhost', port=6379)

print("🔁 Redis Trade Trigger Started...")
while True:
    trade_json = r.rpop("trade_queue")
    if trade_json:
        try:
            trade = json.loads(trade_json.decode())
            with open("current_trade.json", "w") as f:
                json.dump(trade, f)
            print(f"📤 Trade Triggered: {trade}")
            subprocess.run(["python3", "genie_trade_copier.py"])
        except Exception as e:
            print(f"❌ Error processing trade: {e}")
    time.sleep(1)
