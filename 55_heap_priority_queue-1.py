# 55 Heap and Priority Queue - 11 practice programs
import heapq

# 1 Min heap
h=[7,2,9,1,5]; heapq.heapify(h); print("1 Min heap:",h)
# 2 Push
heapq.heappush(h,3); print("2 Push:",h)
# 3 Pop minimum
print("3 Pop:",heapq.heappop(h))
# 4 K smallest
a=[8,1,6,2,9,3,4]; print("4 3 smallest:",heapq.nsmallest(3,a))
# 5 K largest
print("5 3 largest:",heapq.nlargest(3,a))
# 6 Merge sorted lists
print("6 Merge:",list(heapq.merge([1,4,7],[2,5,8],[3,6,9])))
# 7 Priority queue
q=[]; [heapq.heappush(q,x) for x in [(2,"report"),(1,"bug"),(3,"read")]]
print("7 Priority:",[heapq.heappop(q) for _ in range(len(q))])
# 8 Kth largest
a=[10,4,7,20,15,2]; print("8 2nd largest:",heapq.nlargest(2,a)[-1])
# 9 Nearly sorted array
a=[2,1,4,3,6,5]; k=2; h=a[:k+1]; heapq.heapify(h); out=[]
for x in a[k+1:]: out.append(heapq.heappop(h)); heapq.heappush(h,x)
while h: out.append(heapq.heappop(h))
print("9 Nearly sorted:",out)
# 10 Top-k frequent
a=[1,1,1,2,2,3,4,4,4]; freq={}
for x in a: freq[x]=freq.get(x,0)+1
print("10 Top frequent:",heapq.nlargest(2,freq,key=freq.get))
# 11 Running median
low=[]; high=[]; med=[]
for x in [5,15,1,3]:
    heapq.heappush(low,-x); heapq.heappush(high,-heapq.heappop(low))
    if len(high)>len(low): heapq.heappush(low,-heapq.heappop(high))
    med.append((-low[0]+high[0])/2 if len(low)==len(high) else -low[0])
print("11 Running median:",med)
