
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/audit-webhook', methods=['POST'])
def audit_webhook():
    data = request.json
    print("🔔 GENIE AUDIT ALERT RECEIVED")
    print(f"Status: {data.get('status')}")
    print(f"Summary: {data.get('summary')}")
    return jsonify({"ok": True, "message": "Audit webhook received"})

if __name__ == '__main__':
    app.run(port=5052)
