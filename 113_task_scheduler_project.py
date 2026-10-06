# 113 Task Scheduler Mini Project
from dataclasses import dataclass
from datetime import datetime,timedelta
import heapq

# 1 Create task
@dataclass
class Task:
    title:str
    priority:int=5
    completed:bool=False
task=Task("Learn Python",1)
print("1",task)

# 2 Complete task
task.completed=True
print("2",task)

# 3 Multiple tasks
tasks=[Task("Read",3),Task("Practice",1),Task("Review",2)]
print("3",tasks)

# 4 Sort by priority
print("4",sorted(tasks,key=lambda x:x.priority))

# 5 Filter incomplete
print("5",[t for t in tasks if not t.completed])

# 6 Priority queue
q=[]
for t in tasks: heapq.heappush(q,(t.priority,t.title))
print("6",heapq.heappop(q))

# 7 Scheduled task
@dataclass
class ScheduledTask:
    title:str
    run_at:datetime
scheduled=ScheduledTask("Daily Python",datetime.now()+timedelta(hours=1))
print("7",scheduled)

# 8 Due tasks
now=datetime.now()
due=[ScheduledTask("Past",now-timedelta(minutes=5)),ScheduledTask("Future",now+timedelta(hours=2))]
print("8",[t.title for t in due if t.run_at<=now])

# 9 Task manager
class TaskManager:
    def __init__(self): self.tasks=[]
    def add(self,t): self.tasks.append(t)
    def complete(self,title):
        for t in self.tasks:
            if t.title==title: t.completed=True; return True
        return False
    def pending(self): return [t for t in self.tasks if not t.completed]

m=TaskManager(); m.add(Task("Python",1)); m.add(Task("Git",2)); m.complete("Python")
print("9",m.pending())

# 10 Next pending task
def next_task(tasks):
    pending=[t for t in tasks if not t.completed]
    return min(pending,key=lambda x:x.priority) if pending else None
print("10",next_task(m.tasks))

# 11 Complete scheduler
class Scheduler:
    def __init__(self): self.queue=[]
    def add(self,title,priority): heapq.heappush(self.queue,(priority,title))
    def next(self): return heapq.heappop(self.queue) if self.queue else None

s=Scheduler()
s.add("Backup files",3); s.add("Fix bug",1); s.add("Documentation",2)
print("11")
while s.queue: print("  ",s.next())
