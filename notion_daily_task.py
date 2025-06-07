import requests
from datetime import datetime
import os

NOTION_TOKEN = "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"
DATABASE_ID = "220ba6b2eb1ea80e89ecce8e9c5a3a447"
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

data = {
    "parent": {"database_id": DATABASE_ID},
    "properties": {
        "Name": {
            "title": [{"text": {"content": "Daily Check"}}]
        },
        "Date": {
            "date": {"start": datetime.today().strftime("%Y-%m-%d")}
        },
        "Task": {
            "checkbox": False
        }
    }
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
print("Added:", response.status_code, response.text)
