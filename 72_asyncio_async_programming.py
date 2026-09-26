"""Day 17 - File 72: Asyncio and Async Programming | 11 Programs"""
import asyncio

async def program_1():
    print("Async task started")
    await asyncio.sleep(0.1)
    print("Async task completed")

async def program_2():
    await asyncio.sleep(0.05)
    return "Async result"

async def program_3():
    async def task(name):
        await asyncio.sleep(0.1)
        print(name, "done")
    await asyncio.gather(task("Task 1"), task("Task 2"), task("Task 3"))

async def program_4():
    for n in range(3,0,-1):
        print(n)
        await asyncio.sleep(0.1)
    print("Go!")

async def program_5():
    loop = asyncio.get_running_loop()
    start = loop.time()
    await asyncio.sleep(0.2)
    print("Elapsed:", round(loop.time()-start,2), "seconds")

async def program_6():
    async def square(n):
        await asyncio.sleep(0.05)
        return n*n
    tasks=[asyncio.create_task(square(i)) for i in range(1,6)]
    print(await asyncio.gather(*tasks))

async def program_7():
    queue=asyncio.Queue()
    async def producer():
        for i in range(1,6):
            await queue.put(i)
        await queue.put(None)
    async def consumer():
        while True:
            item=await queue.get()
            if item is None:
                break
            print("Consumed:",item)
    await asyncio.gather(producer(),consumer())

async def program_8():
    semaphore=asyncio.Semaphore(2)
    async def worker(n):
        async with semaphore:
            print("Start",n)
            await asyncio.sleep(0.1)
            print("Finish",n)
    await asyncio.gather(*(worker(i) for i in range(5)))

async def program_9():
    async def risky():
        await asyncio.sleep(0.05)
        raise ValueError("Something went wrong")
    try:
        await risky()
    except ValueError as e:
        print("Handled:",e)

async def program_10():
    attempts=0
    async def operation():
        nonlocal attempts
        attempts+=1
        if attempts<3:
            raise RuntimeError("Temporary failure")
        return "Success"
    for attempt in range(1,4):
        try:
            print(await operation())
            break
        except RuntimeError as e:
            print("Attempt",attempt,"failed:",e)
            await asyncio.sleep(0.05)

async def program_11():
    async def job(n):
        await asyncio.sleep(0.05*n)
        return f"Job {n} completed"
    results=await asyncio.gather(*(job(i) for i in range(1,6)))
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(program_1())
