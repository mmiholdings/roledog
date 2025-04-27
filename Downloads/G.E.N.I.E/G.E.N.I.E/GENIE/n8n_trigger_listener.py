from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger_workflow():
    subprocess.run([
        "curl", "-X", "POST",
        "https://api.github.com/repos/YOUR_ORG/YOUR_REPO/actions/workflows/genie_infra_deploy.yml/dispatches",
        "-H", "Accept: application/vnd.github.v3+json",
        "-H", "Authorization: token YOUR_GITHUB_PAT",
        "-d", '{"ref":"main"}'
    ])
    return jsonify({"status": "triggered"}), 200

if __name__ == "__main__":
    app.run(port=5055)