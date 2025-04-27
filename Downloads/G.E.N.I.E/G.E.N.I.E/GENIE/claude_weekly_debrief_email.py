
# CRON: Every Friday at 5pm UTC
0 17 * * 5 python3 /home/ec2-user/send_claude_weekly_report.py

# Python: send_claude_weekly_report.py
import smtplib
from email.mime.text import MIMEText
import requests

# Load and send Claude GPT summary
def generate_summary():
    journal = open("genie_journal.csv").read()
    prompt = f"""You're GENIE's institutional trading analyst.
Evaluate Claude's signal accuracy this week from the journal:
{journal}
"""
    response = requests.post("https://your-api.com/claude-eval", json={"prompt": prompt})
    return response.text

def send_email(summary):
    msg = MIMEText(summary)
    msg["Subject"] = "GENIE Claude Weekly Performance Report"
    msg["From"] = "genie@yourdomain.com"
    msg["To"] = "execs@hedgefund.com"

    with smtplib.SMTP("smtp.yourdomain.com") as server:
        server.login("user", "pass")
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())

if __name__ == "__main__":
    send_email(generate_summary())
