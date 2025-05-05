
import openai
import pandas as pd
import logging

logging.basicConfig(filename="genie_gpt_review.log", level=logging.INFO)

def review(log_file="trade_log.csv"):
    df = pd.read_csv(log_file)
    sample = df.tail(10).to_string()
    prompt = f"Review this trade log and suggest 3 strategic improvements:\n{sample}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response["choices"][0]["message"]["content"]
    logging.info(f"🧠 GPT Review:\n{result}")
    with open("gpt_trade_review.md", "w") as f:
        f.write(result)
    print("✅ GPT review complete.")

if __name__ == "__main__":
    review()
