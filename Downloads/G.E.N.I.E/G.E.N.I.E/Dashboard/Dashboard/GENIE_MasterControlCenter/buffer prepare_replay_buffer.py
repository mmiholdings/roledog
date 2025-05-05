import pandas as pd
import json
import os

def generate_buffer():
    df = pd.read_csv("qc_data/mes_sample.csv")
    buffer = []
    for i in range(1, len(df) - 1):
        state = [df.loc[i-1, "close"]]
        action = 1 if df.loc[i+1, "close"] > df.loc[i, "close"] else 0
        reward = df.loc[i+1, "close"] - df.loc[i, "close"]
        next_state = [df.loc[i, "close"]]
        done = False
        buffer.append((state, action, reward, next_state, done))
    with open("buffer/mes_buffer.json", "w") as f:
        json.dump(buffer, f)
    print("✅ Replay buffer saved to buffer/mes_buffer.json")

if __name__ == "__main__":
    os.makedirs("buffer", exist_ok=True)
    generate_buffer()
