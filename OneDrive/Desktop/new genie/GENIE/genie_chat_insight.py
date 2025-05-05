
# GENIE Chat Interface (Ask About Specific Date)

import pandas as pd
import datetime
import openai  # or Claude-compatible Bedrock wrapper

def genie_insight_on(date_query):
    df = pd.read_csv("genie_journal.csv", parse_dates=["timestamp"])
    filtered = df[df["timestamp"].dt.strftime('%A') == date_query]

    if filtered.empty:
        return "No trades on that day."

    prompt = f"""
GENIE Journal:
{filtered.to_csv(index=False)}

Question: What happened on {date_query} and why did we perform well or poorly?

Answer in plain language.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(genie_insight_on("Tuesday"))
