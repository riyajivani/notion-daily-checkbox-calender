import requests
from datetime import datetime
import os

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

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
