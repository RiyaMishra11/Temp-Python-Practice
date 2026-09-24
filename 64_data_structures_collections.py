# 64 collections module - 11 programs
from collections import Counter,defaultdict,deque,namedtuple,OrderedDict
text="banana"
print("1 Counter:",Counter(text))
nums=[1,2,2,3,3,3,4]
print("2 Common:",Counter(nums).most_common(2))
print("3 Add counters:",Counter("aabbc")+Counter("abcc"))
groups=defaultdict(list)
for cat,item in [("fruit","apple"),("fruit","banana"),("veg","carrot")]: groups[cat].append(item)
print("4 Groups:",dict(groups))
counts=defaultdict(int)
for w in ["python","code","python"]: counts[w]+=1
print("5 Counts:",dict(counts))
q=deque([2,3]);q.appendleft(1);q.append(4)
print("6 Deque:",q,"removed",q.popleft(),q.pop())
q=deque([1,2,3,4,5]);q.rotate(2)
print("7 Rotate:",q)
Student=namedtuple("Student",["name","marks"]);s=Student("Rahul",90)
print("8 Named tuple:",s.name,s.marks)
od=OrderedDict([("a",1),("b",2),("c",3)])
print("9 Ordered dict:",od)
by=defaultdict(list)
for w in ["cat","dog","apple","bat","mango"]: by[len(w)].append(w)
print("10 By length:",dict(by))
def sliding(a,k):
    d=deque();r=[]
    for i,x in enumerate(a):
        while d and d[0]<=i-k:d.popleft()
        while d and a[d[-1]]<=x:d.pop()
        d.append(i)
        if i>=k-1:r.append(a[d[0]])
    return r
print("11 Sliding max:",sliding([1,3,-1,-3,5,3,6,7],3))
