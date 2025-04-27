import requests
import json

NOTION_TOKEN = "secret_xxx"
NOTION_DB_ID = "your_notion_db_id"

def fetch_switch_trigger():
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28"
    }
    response = requests.post(
        "https://api.notion.com/v1/databases/{}/query".format(NOTION_DB_ID),
        headers=headers
    )
    results = response.json().get("results", [])
    for row in results:
        props = row["properties"]
        if props.get("Switch GPT", {}).get("checkbox") == True:
            chosen = props.get("Model", {}).get("select", {}).get("name", "Claude")
            return chosen
    return "Claude"