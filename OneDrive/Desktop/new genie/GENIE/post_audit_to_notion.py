
import requests

def post_to_notion(summary, notion_token, page_id):
    url = "https://api.notion.com/v1/blocks"
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    payload = {
        "parent": { "type": "page_id", "page_id": page_id },
        "children": [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "text": [{
                    "type": "text",
                    "text": {
                        "content": summary
                    }
                }]
            }
        }]
    }
    res = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children", headers=headers, json=payload)
    print(res.status_code, res.text)
