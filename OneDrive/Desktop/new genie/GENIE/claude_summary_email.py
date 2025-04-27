import openai
import smtplib
from email.mime.text import MIMEText

with open("agent_performance_weekly.md") as f:
    summary = f.read()

msg = MIMEText(summary)
msg["Subject"] = "GENIE Weekly Agent Performance"
msg["From"] = "genie@yourdomain.com"
msg["To"] = "team@yourdomain.com"

s = smtplib.SMTP("email-smtp.us-east-1.amazonaws.com", 587)
s.starttls()
s.login("SMTP_USERNAME", "SMTP_PASSWORD")
s.sendmail(msg["From"], [msg["To"]], msg.as_string())
s.quit()