import requests
import json

NOTION_DB_ID = "your_notion_db_id"
NOTION_API_KEY = "secret_xxx"

def post_sentiment_to_notion(sentiment_result):
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    data = {
        "parent": { "database_id": NOTION_DB_ID },
        "properties": {
            "Sentiment": { "title": [{ "text": { "content": sentiment_result["summary"] } }] },
            "Confidence": { "number": sentiment_result["confidence"] },
            "Timestamp": { "date": { "start": sentiment_result["timestamp"] } }
        }
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, data=json.dumps(data))
    print("Sent to Notion:", response.status_code, response.text)