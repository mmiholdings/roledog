
import openai

def analyze_strategy(filepath="strategy.py"):
    with open(filepath) as f:
        code = f.read()

    prompt = f"Refactor this trading strategy for performance, clarity, and robustness:\n{code}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    analyze_strategy()
