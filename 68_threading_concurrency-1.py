"""Day 16 - File 68: Threading and Concurrency | 11 Programs"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def program_1():
    def task(): print("Task executed in thread")
    t=threading.Thread(target=task); t.start(); t.join()

def program_2():
    def worker(n): print("Worker:",n)
    ts=[threading.Thread(target=worker,args=(i,)) for i in range(5)]
    for t in ts: t.start()
    for t in ts: t.join()

def program_3():
    def greet(name): print("Hello",name)
    t=threading.Thread(target=greet,args=("Aman",)); t.start(); t.join()

def program_4():
    def task(name):
        time.sleep(0.1); print(name,"finished")
    ts=[threading.Thread(target=task,args=(f"Task-{i}",)) for i in range(3)]
    for t in ts: t.start()
    for t in ts: t.join()

def program_5():
    counter=0; lock=threading.Lock()
    def inc():
        nonlocal counter
        for _ in range(1000):
            with lock: counter+=1
    ts=[threading.Thread(target=inc) for _ in range(5)]
    for t in ts: t.start()
    for t in ts: t.join()
    print("Counter:",counter)

def program_6():
    event=threading.Event()
    def waiter():
        print("Waiting..."); event.wait(); print("Event received")
    t=threading.Thread(target=waiter); t.start(); time.sleep(0.1); event.set(); t.join()

def program_7():
    results=[]; lock=threading.Lock()
    def worker(x):
        with lock: results.append(x*x)
    ts=[threading.Thread(target=worker,args=(i,)) for i in range(1,6)]
    for t in ts: t.start()
    for t in ts: t.join()
    print(sorted(results))

def program_8():
    with ThreadPoolExecutor(max_workers=3) as ex:
        print(list(ex.map(lambda x:x*x, range(1,6))))

def program_9():
    def add(a,b): return a+b
    with ThreadPoolExecutor(max_workers=2) as ex:
        fs=[ex.submit(add,10,20),ex.submit(add,30,40),ex.submit(add,50,60)]
        print([f.result() for f in fs])

def program_10():
    texts=["python","threading","concurrency","programming"]
    with ThreadPoolExecutor(max_workers=4) as ex:
        print(list(ex.map(str.upper,texts)))

def program_11():
    def task(n):
        time.sleep(0.05); return f"Task {n} completed"
    with ThreadPoolExecutor(max_workers=3) as ex:
        for result in ex.map(task,range(1,6)): print(result)

if __name__ == "__main__":
    program_1()
