"""
89 - JSON File Manager
A simple CRUD-style JSON storage utility using only the Python standard library.
"""

import json
from pathlib import Path
from typing import Any


class JSONFileManager:
    def __init__(self, filename: str = "data.json"):
        self.path = Path(filename)

    def load(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []

        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def save(self, records: list[dict[str, Any]]) -> None:
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=2, ensure_ascii=False)

    def add(self, record: dict[str, Any]) -> None:
        records = self.load()
        records.append(record)
        self.save(records)

    def find_by_id(self, record_id: int) -> dict[str, Any] | None:
        for record in self.load():
            if record.get("id") == record_id:
                return record
        return None

    def delete_by_id(self, record_id: int) -> bool:
        records = self.load()
        filtered = [record for record in records if record.get("id") != record_id]

        if len(filtered) == len(records):
            return False

        self.save(filtered)
        return True


def main() -> None:
    manager = JSONFileManager("demo_data.json")

    manager.add({"id": 1, "name": "Riya", "role": "Python Developer"})
    manager.add({"id": 2, "name": "Aman", "role": "Backend Developer"})

    print("All records:")
    print(manager.load())

    print("\nFind ID 1:")
    print(manager.find_by_id(1))

    print("\nDelete ID 2:")
    print(manager.delete_by_id(2))

    print("\nRemaining records:")
    print(manager.load())


if __name__ == "__main__":
    main()
