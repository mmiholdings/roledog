
import pandas as pd
import openai

def suggest_rotation(csv_file="agent_performance.csv"):
    df = pd.read_csv(csv_file)
    recent = df.groupby("agent").tail(1)
    summary = recent.to_string(index=False)

    prompt = f"Given this recent agent performance, which agent should be prioritized or demoted this week?\n{summary}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response["choices"][0]["message"]["content"]
    with open("agent_rotation_suggestion.md", "w") as f:
        f.write(result)
    print("✅ Weekly agent rotation suggestion saved.")

if __name__ == "__main__":
    suggest_rotation()
