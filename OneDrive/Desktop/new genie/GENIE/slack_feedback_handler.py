
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
API_ENDPOINT = "https://genie-feedback-api.onrender.com/genie-feedback"

@app.route("/slack/feedback", methods=["POST"])
def trigger_feedback():
    text = request.form.get("text")
    payload = {"summary": text}
    response = requests.post(API_ENDPOINT, json=payload)
    return jsonify({
        "response_type": "in_channel",
        "text": "✅ GENIE feedback loop triggered.",
        "attachments": [{"text": response.json().get("summary", "Audit submitted.")}]
    })

if __name__ == "__main__":
    app.run(port=5054)
