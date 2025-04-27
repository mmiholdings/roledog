
import openai
from datetime import datetime

def summarize_deployments():
    with open("ecr_deploy.log", "r") as f:
        logs = f.read()

    prompt = f"""
You are GENIE's post-deployment auditor. Read these ECR deployment logs and summarize:
1. ✅ Which images were pushed this week?
2. ♻️ Were any tags reused or re-deployed?
3. ❌ Any failed pushes or version errors?
4. 📊 Container run success/fail outcomes

Date: {datetime.now().date()}
Logs:
{logs}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    summarize_deployments()
