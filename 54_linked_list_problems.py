# 54 Linked List Problems - 11 practice programs
class Node:
    def __init__(self, data):
        self.data, self.next = data, None

def build(values):
    head = tail = None
    for x in values:
        n = Node(x)
        if head is None: head = tail = n
        else: tail.next, tail = n, n
    return head

def show(head):
    out=[]
    while head: out.append(head.data); head=head.next
    print(out)

# 1 Traverse
head=build([10,20,30,40]); print("1 Traverse:", end=" "); show(head)
# 2 Count nodes
c=0; p=head
while p: c+=1; p=p.next
print("2 Count:",c)
# 3 Search
target=30; p=head
print("3 Search 30:", any((p.data==target for p in iter_nodes(head))))
# 4 Middle node
slow=fast=head
while fast and fast.next: slow,fast=slow.next,fast.next.next
print("4 Middle:",slow.data)
# 5 Reverse
prev=None; p=head
while p:
    nxt=p.next; p.next=prev; prev,p=p,nxt
head=prev; print("5 Reverse:",end=" "); show(head)
# 6 Insert at beginning
n=Node(5); n.next=head; head=n; print("6 Insert beginning:",end=" "); show(head)
# 7 Insert after 20
p=head
while p and p.data!=20: p=p.next
n=Node(25); n.next=p.next; p.next=n; print("7 Insert after 20:",end=" "); show(head)
# 8 Delete 25
dummy=Node(0); dummy.next=head; prev,p=dummy,head
while p:
    if p.data==25: prev.next=p.next; break
    prev,p=p,p.next
head=dummy.next; print("8 Delete 25:",end=" "); show(head)
# 9 Cycle detection
a,b,c=Node(1),Node(2),Node(3); a.next,b.next,c.next=b,c,b
slow=fast=a; cycle=False
while fast and fast.next:
    slow,fast=slow.next,fast.next.next
    if slow is fast: cycle=True; break
print("9 Cycle:",cycle)
# 10 Remove duplicates from sorted list
h=build([1,1,2,2,3,3]); p=h
while p and p.next:
    if p.data==p.next.data: p.next=p.next.next
    else: p=p.next
print("10 Remove duplicates:",end=" "); show(h)
# 11 Merge two sorted lists
x,y=build([1,3,5]),build([2,4,6]); d=Node(0); t=d
while x and y:
    if x.data<=y.data: t.next,x=x,x.next
    else: t.next,y=y,y.next
    t=t.next
t.next=x or y; print("11 Merge:",end=" "); show(d.next)

def iter_nodes(head):
    while head:
        yield head
        head=head.next
