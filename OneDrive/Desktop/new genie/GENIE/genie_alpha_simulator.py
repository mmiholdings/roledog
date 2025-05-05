
import pandas as pd
import json

def simulate():
    data = pd.read_csv("trade_log.csv")
    weights = [
        {"Mo": 0.4, "Reggie": 0.3, "Ace": 0.3},
        {"Mo": 0.2, "Reggie": 0.5, "Ace": 0.3},
        {"Mo": 0.3, "Reggie": 0.2, "Ace": 0.5}
    ]
    results = []
    for w in weights:
        weighted = (data['reward'] * data['agent'].map(w)).sum()
        results.append({"weights": w, "score": weighted})
    best = max(results, key=lambda x: x["score"])
    with open("alpha_sim_result.json", "w") as f:
        json.dump(best, f, indent=2)
    print("🏁 Best Alpha Playbook:", best)

if __name__ == "__main__":
    simulate()
