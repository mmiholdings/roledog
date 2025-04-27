
import argparse
import json

def load_config(volatility, sentiment):
    if volatility > 0.6 and sentiment < -0.3:
        config = {"agent": "Reggie", "stop": "tight", "risk": 0.02}
    elif sentiment > 0.6:
        config = {"agent": "Ace", "stop": "wide", "risk": 0.04}
    else:
        config = {"agent": "Mo", "stop": "normal", "risk": 0.03}

    with open("agent_config.json", "w") as f:
        json.dump(config, f, indent=2)
    print("✅ Config chosen:", config)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--volatility", type=float, required=True)
    parser.add_argument("--sentiment", type=float, required=True)
    args = parser.parse_args()
    load_config(args.volatility, args.sentiment)
