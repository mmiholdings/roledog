
# GPT Auto-Strategy Generation → MARL Training

import requests

def fetch_new_strategy():
    prompt = """
You're an AI quant strategist. Based on recent market activity, suggest a new trading strategy idea for MARL agent training. Include entry logic, exit logic, and reward function guidance.

Constraints:
- Intraday strategy
- Uses sentiment, SmartFlow, and price action
- Avoids overnight exposure
"""

    response = requests.post("https://your-api.com/gpt-strategy", json={"prompt": prompt})
    return response.text

def save_strategy_for_training(strategy_text):
    with open("strategies/auto_generated_strategy.txt", "w") as f:
        f.write(strategy_text)

if __name__ == "__main__":
    strat = fetch_new_strategy()
    save_strategy_for_training(strat)
    print("📊 New strategy fetched and saved for MARL training.")
