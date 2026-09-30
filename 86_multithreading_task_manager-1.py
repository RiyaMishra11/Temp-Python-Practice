"""
86 - Multithreading Task Manager
Demonstrates ThreadPoolExecutor, task execution and error handling.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random


def process_task(task_id: int) -> str:
    delay = random.uniform(0.3, 1.0)
    time.sleep(delay)

    if task_id == 7:
        raise ValueError("Task 7 failed intentionally")

    return f"Task {task_id} completed in {delay:.2f}s"


def main() -> None:
    tasks = range(1, 11)

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_task, task_id) for task_id in tasks]

        for future in as_completed(futures):
            try:
                print(future.result())
            except Exception as exc:
                print(f"Task error: {exc}")


if __name__ == "__main__":
    main()
