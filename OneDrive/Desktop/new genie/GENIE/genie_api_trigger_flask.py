
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/trigger-audit', methods=['POST', 'GET'])
def trigger():
    subprocess.run(["python3", "export_cloudwatch_logs.py"])
    subprocess.run(["python3", "claude_audit.py"])
    subprocess.run(["python3", "post_audit_to_notion.py"])
    return "✅ GENIE Audit Triggered!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5051)
