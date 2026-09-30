"""
87 - Asyncio Task Runner
Demonstrates asynchronous tasks, gathering results and exceptions.
"""

import asyncio
import random


async def process_task(task_id: int) -> str:
    delay = random.uniform(0.3, 1.0)
    await asyncio.sleep(delay)

    if task_id == 5:
        raise RuntimeError("Task 5 failed intentionally")

    return f"Task {task_id} completed in {delay:.2f}s"


async def main() -> None:
    tasks = [process_task(i) for i in range(1, 11)]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, Exception):
            print(f"Task error: {result}")
        else:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
