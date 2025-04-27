
import openai

def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        logs = f.read()

    prompt = f"""
You are an AI DevOps analyst. Review this CI/CD log and summarize:
- Build success or failure
- Deployment steps
- Errors or crashes

Log:
{logs}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
