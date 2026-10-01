"""92 - Log File Analyzer"""
from collections import Counter
from pathlib import Path
import re

LOG_PATTERN = re.compile(r"\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b")

class LogAnalyzer:
    def __init__(self, filename):
        self.filename = Path(filename)

    def analyze(self):
        levels = Counter()
        messages = Counter()

        with self.filename.open("r", encoding="utf-8") as file:
            for line in file:
                match = LOG_PATTERN.search(line)
                if match:
                    levels[match.group(1)] += 1
                line = line.strip()
                if line:
                    messages[line] += 1

        return {
            "levels": dict(levels),
            "total_lines": sum(messages.values()),
            "repeated_messages": {
                msg: count for msg, count in messages.items() if count > 1
            },
        }

def main():
    filename = "application.log"
    Path(filename).write_text(
        "2026-10-01 INFO Application started\n"
        "2026-10-01 INFO User logged in\n"
        "2026-10-01 ERROR Database connection failed\n"
        "2026-10-01 WARNING Retrying database connection\n"
        "2026-10-01 ERROR Database connection failed\n",
        encoding="utf-8",
    )

    report = LogAnalyzer(filename).analyze()
    print("Log level counts:", report["levels"])
    print("Total lines:", report["total_lines"])
    print("Repeated messages:", report["repeated_messages"])

if __name__ == "__main__":
    main()
