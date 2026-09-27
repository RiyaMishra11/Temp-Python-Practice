"""File 75: Heap Algorithms | 11 Programs"""
import heapq

def program_1():
    h=[7,2,9,1,5]; heapq.heapify(h); print(heapq.heappop(h),heapq.heappop(h))

def program_2():
    h=[]
    for x in [30,10,20,5]:heapq.heappush(h,x)
    print(h)

def program_3():
    h=[8,3,6,1,5]; heapq.heapify(h); r=[]
    while h:r.append(heapq.heappop(h))
    print(r)

def program_4():print(heapq.nsmallest(3,[9,4,1,7,3,8,2]))

def program_5():print(heapq.nlargest(3,[9,4,1,7,3,8,2]))

def program_6():
    a=[10,4,7,2,15,8]; k=2
    print("Kth largest:",heapq.nlargest(k,a)[-1])

def program_7():print(list(heapq.merge([1,4,7],[2,5,8],[3,6,9])))

def program_8():
    q=[]
    for item in [(2,"Normal"),(1,"Urgent"),(3,"Low")]:heapq.heappush(q,item)
    while q:print(heapq.heappop(q))

def program_9():
    p=[("Laptop",65000),("Mouse",1200),("Monitor",18000),("Phone",45000)]
    print(heapq.nlargest(2,p,key=lambda x:x[1]))

def program_10():
    values=[5,15,1,3]; low=[]; high=[]
    for x in values:
        heapq.heappush(low,-x) if not low or x<=-low[0] else heapq.heappush(high,x)
        if len(low)>len(high)+1:heapq.heappush(high,-heapq.heappop(low))
        elif len(high)>len(low):heapq.heappush(low,-heapq.heappop(high))
        m=(-low[0]+high[0])/2 if len(low)==len(high) else -low[0]
        print("Added",x,"Median",m)

def program_11():
    q=[]
    for x in [(3,"Backup"),(1,"Fix bug"),(2,"Report"),(1,"Deploy")]:heapq.heappush(q,x)
    while q:print(heapq.heappop(q))

if __name__=="__main__":program_1()
