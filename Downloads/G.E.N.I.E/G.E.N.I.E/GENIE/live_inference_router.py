
import argparse
import json
import logging

logging.basicConfig(filename="genie_live_inference.log", level=logging.INFO)

def route_signal(claude_score, predictnow_prob, marl_output):
    confidence = (claude_score * 0.4) + (predictnow_prob * 0.3) + (marl_output * 0.3)
    decision = "BUY" if confidence > 0.6 else "SELL" if confidence < 0.4 else "HOLD"
    signal = {"confidence": round(confidence, 3), "decision": decision}
    logging.info(f"Routed signal: {signal}")
    with open("trade_signal.json", "w") as f:
        json.dump(signal, f)
    print("✅ Signal routed:", signal)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--claude", type=float, required=True)
    parser.add_argument("--predictnow", type=float, required=True)
    parser.add_argument("--marl", type=float, required=True)
    args = parser.parse_args()
    route_signal(args.claude, args.predictnow, args.marl)
