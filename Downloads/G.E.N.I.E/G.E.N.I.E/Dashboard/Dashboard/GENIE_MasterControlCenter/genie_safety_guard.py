
import json
import pandas as pd

def run_guard(log_file="trade_log.csv", max_trades=10, max_drawdown=-1000):
    df = pd.read_csv(log_file)
    recent = df.tail(max_trades)
    total_pnl = recent['reward'].sum()

    flag = False
    reason = ""
    if len(recent) >= max_trades:
        flag = True
        reason = "Exceeded trade limit"
    if total_pnl <= max_drawdown:
        flag = True
        reason = "Drawdown breach"

    output = {"kill": flag, "reason": reason if flag else "OK"}
    with open("kill_signal.json", "w") as f:
        json.dump(output, f, indent=2)
    print("🛡️ Safety check:", output)

if __name__ == "__main__":
    run_guard()
