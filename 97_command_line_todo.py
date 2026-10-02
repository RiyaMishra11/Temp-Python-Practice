"""97 - Command Line Todo Manager"""
import argparse
import json
from pathlib import Path

class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = Path(filename)
        self.todos = self.load()

    def load(self):
        if not self.filename.exists():
            return []
        try:
            return json.loads(self.filename.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []

    def save(self):
        self.filename.write_text(
            json.dumps(self.todos, indent=2),
            encoding="utf-8"
        )

    def add(self, task):
        todo_id = max((x["id"] for x in self.todos), default=0) + 1
        self.todos.append({
            "id": todo_id,
            "task": task,
            "completed": False
        })
        self.save()
        return todo_id

    def complete(self, todo_id):
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                self.save()
                return True
        return False

def main():
    parser = argparse.ArgumentParser(description="Simple Todo Manager")
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add")
    add.add_argument("task")

    complete = sub.add_parser("complete")
    complete.add_argument("id", type=int)

    sub.add_parser("list")

    args = parser.parse_args()
    manager = TodoManager()

    if args.command == "add":
        print("Added todo:", manager.add(args.task))
    elif args.command == "complete":
        print("Completed:", manager.complete(args.id))
    elif args.command == "list":
        for todo in manager.todos:
            mark = "✓" if todo["completed"] else " "
            print(f"[{mark}] {todo['id']}: {todo['task']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
