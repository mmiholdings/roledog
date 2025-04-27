
# Ask GENIE Anything - Slack Bot (Claude/GPT Answer Engine)

import os
import requests
from flask import Flask, request

app = Flask(__name__)

SLACK_TOKEN = "xoxb-your-token"
GPT_API = "https://your-api.com/genie-insight"

@app.route("/genie", methods=["POST"])
def genie_bot():
    user_input = request.form.get("text")
    prompt = f"GENIE journal analyst: {user_input}"
    response = requests.post(GPT_API, json={"prompt": prompt}).text

    slack_response = {
        "response_type": "in_channel",
        "text": f"🧠 GENIE SAYS:
{response}"
    }
    return slack_response

if __name__ == "__main__":
    app.run(port=5001)
