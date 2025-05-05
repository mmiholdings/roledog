
import openai
import json

def evaluate_configs(result_file="alpha_sim_result.json"):
    with open(result_file) as f:
        data = json.load(f)

    prompt = f"""
GENIE simulation returned this top-performing weight config:
{json.dumps(data, indent=2)}

Based on this, suggest:
- Which agent is outperforming consistently?
- Should any be dropped or deprioritized?
- What is your confidence level in this config going forward?
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    analysis = response["choices"][0]["message"]["content"]
    with open("claude_config_analysis.md", "w") as f:
        f.write(analysis)
    print("🧠 Claude analysis saved.")

if __name__ == "__main__":
    evaluate_configs()
