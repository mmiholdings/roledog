import openai

def audit_genie_log():
    with open("genie.log", "r") as file:
        logs = file.read()

    prompt = f"""
You are GENIE's post-deployment auditor. Summarize this log with:
- What was deployed
- What errors occurred
- What retrained or updated
- Any recommendations for optimization

Log:
{logs}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    audit_genie_log()
