import random
import json
import requests
import datetime

def rotate_model_source():
    models = ["Claude-v2", "FinBERT", "GPT-4"]
    chosen = random.choice(models)
    timestamp = datetime.datetime.utcnow().isoformat()
    payload = {
        "model": chosen,
        "timestamp": timestamp
    }
    print(f"[SYNC] Rotating sentiment model to: {chosen}")

    # Notion API push
    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers={
            "Authorization": "Bearer YOUR_NOTION_TOKEN",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "parent": { "database_id": "YOUR_DB_ID" },
            "properties": {
                "Rotation Log": { "title": [{ "text": { "content": f"Model switched to {chosen}" } }] },
                "Timestamp": { "date": { "start": timestamp } }
            }
        })
    )
    print(response.status_code, response.text)