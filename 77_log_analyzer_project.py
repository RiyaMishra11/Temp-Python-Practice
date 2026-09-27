"""File 77: Mini Project - Log Analyzer | 11 Programs"""
from collections import Counter
from datetime import datetime

LOGS=[
"2026-09-27 10:01:12 INFO User login",
"2026-09-27 10:02:05 ERROR Database connection failed",
"2026-09-27 10:03:18 WARNING Disk usage high",
"2026-09-27 10:04:20 INFO User logout",
"2026-09-27 10:05:41 ERROR Timeout while processing request",
"2026-09-27 10:06:30 INFO User login",
"2026-09-27 10:07:15 ERROR Database connection failed"]

def program_1():print(LOGS[0].split(" ",3))

def program_2():print(Counter(x.split()[2] for x in LOGS))

def program_3():print("Errors:",sum(" ERROR " in x for x in LOGS))

def program_4():print([x.split(" ",3)[3] for x in LOGS if " ERROR " in x])

def program_5():
    m=[x.split(" ",3)[3] for x in LOGS if " ERROR " in x]
    print(Counter(m))

def program_6():
    level="WARNING"
    print(*[x for x in LOGS if f" {level} " in x],sep="\n")

def program_7():
    t=datetime.strptime(LOGS[0][:19],"%Y-%m-%d %H:%M:%S")
    print(t,"Hour:",t.hour)

def program_8():
    print(*[x for x in LOGS if "10:03:00"<=x.split()[1]<="10:06:00"],sep="\n")

def program_9():
    c=Counter(x.split()[2] for x in LOGS)
    print("===== SEVERITY REPORT =====")
    for level in ["INFO","WARNING","ERROR"]:print(level,c.get(level,0))

def program_10():
    e=[x.split(" ",3)[3] for x in LOGS if " ERROR " in x]
    print("Most common:",Counter(e).most_common(1)[0])

def program_11():
    levels=Counter();messages=Counter();times=[]
    for line in LOGS:
        p=line.split(" ",3);levels[p[2]]+=1;messages[p[3]]+=1
        times.append(datetime.strptime(p[0]+" "+p[1],"%Y-%m-%d %H:%M:%S"))
    print("===== LOG ANALYZER =====")
    print("Total logs:",len(LOGS))
    print("Levels:",dict(levels))
    print("Most common message:",messages.most_common(1)[0])
    print("First:",min(times),"Last:",max(times))
    print("Error rate:",round(levels["ERROR"]/len(LOGS)*100,2),"%")

if __name__=="__main__":program_11()
