
import pandas as pd
import openai

def analyze_agents(log_file="agent_performance.csv"):
    df = pd.read_csv(log_file)
    summary = df.groupby("agent").agg({"sharpe": "mean", "pnl": "sum"}).reset_index()
    prompt = f"Given the agent summary below, recommend new weights or changes:\n{summary.to_string()}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    analyze_agents()
