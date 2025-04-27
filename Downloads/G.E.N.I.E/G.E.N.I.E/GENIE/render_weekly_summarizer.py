
import openai
import subprocess
import datetime

def summarize_render_logs(service="genie-control-center"):
    today = datetime.date.today()
    logs = subprocess.check_output(["render", "logs", service], text=True)

    prompt = f"""
Read the following Render logs and summarize:
- Uptime issues
- Errors
- Successful module triggers
- Overall GENIE performance this week

Render Logs ({today}):
{logs}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response["choices"][0]["message"]["content"]
    with open("render_weekly_summary.md", "w") as f:
        f.write(summary)
    print("✅ Render log summary saved.")
    
if __name__ == "__main__":
    summarize_render_logs()
