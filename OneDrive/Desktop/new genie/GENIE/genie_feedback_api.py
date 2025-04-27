
import openai
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/genie-feedback", methods=["POST"])
def feedback():
    df = pd.read_csv("agent_performance.csv")
    prompt = f"""You are GENIE's feedback auditor. Below is agent performance data:
{df.to_string(index=False)}

Which agent should be promoted/demoted? Recommend updated weights.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response["choices"][0]["message"]["content"]
    print(result)

    with open("agent_weights.md", "w") as f:
        f.write(result)

    return jsonify({"status": "ok", "message": "Feedback recorded", "summary": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5053)
