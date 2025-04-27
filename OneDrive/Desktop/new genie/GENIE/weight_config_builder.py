
import json
import argparse
import os
from datetime import date
import logging

logging.basicConfig(filename="genie_weight_builder.log", level=logging.INFO)

def build(weights):
    today = date.today().isoformat()
    os.makedirs("configs/weights", exist_ok=True)
    path = f"configs/weights/{today}.json"
    with open(path, "w") as f:
        json.dump(weights, f, indent=2)
    logging.info(f"💾 Weights written: {path}")
    print(f"✅ Weights saved to {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mo", type=float, required=True)
    parser.add_argument("--reggie", type=float, required=True)
    parser.add_argument("--ace", type=float, required=True)
    args = parser.parse_args()
    build({"Mo": args.mo, "Reggie": args.reggie, "Ace": args.ace})
