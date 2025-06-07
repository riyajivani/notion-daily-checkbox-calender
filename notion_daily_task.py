import requests
from datetime import date, timedelta
import os

NOTION_TOKEN = "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"
DATABASE_ID = "20ba6b2eb1ea80e89ecce8e9c5a3a447"
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def create_checkbox_entry(entry_date):
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": f"Daily Check - {entry_date}"}}]
            },
            "Date": {
                "date": {"start": entry_date}
            },
            "Task": {
                "checkbox": False
            }
        }
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
    print(f"Added: {entry_date} → {response.status_code}")
    if response.status_code != 200:
        print(response.text)

def generate_yearly_entries():
    year = date.today().year
    start = date(year, 1, 1)~
    end = date(year, 12, 31)
    current = start

    while current <= end:
        create_checkbox_entry(current.isoformat())
        current += timedelta(days=1)

generate_yearly_entries()
