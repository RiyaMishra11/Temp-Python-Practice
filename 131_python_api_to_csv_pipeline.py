"""
131 - API to CSV Data Pipeline
Learn: HTTP requests, timeouts, status checks, JSON validation, and CSV export.

Install dependency:
    pip install requests

Run:
    python 131_python_api_to_csv_pipeline.py

Uses JSONPlaceholder's public demo API. Internet access is required.
"""
import csv
import requests
from pathlib import Path
from typing import Any

API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_FILE = Path("api_posts.csv")


def fetch_posts(limit: int = 20) -> list[dict[str, Any]]:
    if limit < 1:
        raise ValueError("limit must be at least 1")

    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    payload = response.json()

    if not isinstance(payload, list):
        raise ValueError("API response should be a JSON list")

    posts = []
    for item in payload[:limit]:
        if not isinstance(item, dict):
            continue
        if not {"userId", "id", "title", "body"}.issubset(item):
            continue
        posts.append({
            "user_id": item["userId"],
            "post_id": item["id"],
            "title": str(item["title"]).replace("\\n", " ").strip(),
            "body": str(item["body"]).replace("\\n", " ").strip(),
        })
    return posts


def save_csv(rows: list[dict[str, Any]], destination: Path) -> None:
    fields = ["user_id", "post_id", "title", "body"]
    with destination.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    try:
        posts = fetch_posts(limit=20)
        save_csv(posts, OUTPUT_FILE)
        print(f"Saved {len(posts)} records to: {OUTPUT_FILE.resolve()}")
        for post in posts[:3]:
            print(f"{post['post_id']}: {post['title']}")
    except requests.RequestException as error:
        print(f"Network/API error: {error}")
    except (ValueError, KeyError) as error:
        print(f"Data error: {error}")


if __name__ == "__main__":
    main()
