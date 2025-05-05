
from flask import Flask, request, jsonify
import subprocess
import time

app = Flask(__name__)

@app.route('/genie-run', methods=['POST'])
def run_genie_module():
    data = request.form
    command = data.get("text", "")
    if command:
        parts = command.strip().split()
        if len(parts) == 2 and parts[0] == "run":
            module = parts[1]
            start = time.time()
            try:
                result = subprocess.run(["python3", f"{module}.py"], capture_output=True, text=True, timeout=120)
                duration = round(time.time() - start, 2)
                return jsonify({
                    "response_type": "in_channel",
                    "text": f"✅ GENIE ran `{module}` in {duration}s",
                    "attachments": [{"text": result.stdout[-1000:]}]
                })
            except Exception as e:
                return jsonify({
                    "response_type": "ephemeral",
                    "text": f"❌ Error: {str(e)}"
                })
    return jsonify({"text": "❗ Format: /genie run <module>"})

if __name__ == "__main__":
    app.run(port=5055)
