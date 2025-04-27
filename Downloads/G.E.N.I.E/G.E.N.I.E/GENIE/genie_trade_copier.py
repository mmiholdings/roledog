
import time
import json
import csv
import requests
from datetime import datetime

with open("config.json") as f:
    CONFIG = json.load(f)

def log_trade(broker, status, response_time, trade):
    with open("trade_log.csv", "a", newline="") as logfile:
        writer = csv.writer(logfile)
        writer.writerow([
            datetime.utcnow().isoformat(),
            broker,
            trade["symbol"],
            trade["side"],
            trade["qty"],
            trade["price"],
            status,
            response_time
        ])

def copy_trade(trade):
    brokers = CONFIG["brokers"]
    for broker, settings in brokers.items():
        if not settings["enabled"]:
            continue

        start = time.time()
        try:
            if broker == "alpaca":
                headers = {
                    "APCA-API-KEY-ID": settings["key"],
                    "APCA-API-SECRET-KEY": settings["secret"]
                }
                payload = {
                    "symbol": trade["symbol"],
                    "qty": trade["qty"],
                    "side": trade["side"],
                    "type": "market",
                    "time_in_force": "gtc"
                }
                url = "https://paper-api.alpaca.markets/v2/orders" if settings["paper"] else "https://api.alpaca.markets/v2/orders"
                res = requests.post(url, json=payload, headers=headers)

            elif broker == "ibkr":
                res = {"status": "mocked", "message": "IBKR route logic goes here"}
                time.sleep(1)

            elif broker == "tradovate":
                res = {"status": "mocked", "message": "Tradovate logic here"}
                time.sleep(1)

            elif broker == "nt8":
                res = {"status": "mocked", "message": "NT8 socket plugin route"}
                time.sleep(1)

            else:
                continue

            response_time = round(time.time() - start, 3)
            log_trade(broker, "success", response_time, trade)
            print(f"✅ Routed {trade['side']} {trade['qty']} {trade['symbol']} to {broker}")
        except Exception as e:
            response_time = round(time.time() - start, 3)
            log_trade(broker, "error", response_time, trade)
            print(f"❌ Error routing to {broker}: {e}")

if __name__ == "__main__":
    sample_trade = {
        "symbol": "AAPL",
        "side": "buy",
        "qty": 5,
        "price": 195.43
    }
    copy_trade(sample_trade)
